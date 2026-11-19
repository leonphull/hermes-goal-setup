"""Offline tests for the exported review-slot policy."""

import json
import unittest
from datetime import datetime, timedelta
from pathlib import Path

from review_slots import pick_slot


def at(value):
    return datetime.fromisoformat(value)


class ReviewSlotTests(unittest.TestCase):
    def setUp(self):
        self.policy = json.loads(Path(__file__).with_name('review-policy.json').read_text())
        self.now = at('2026-01-10T10:00+01:00')
        self.finished_by = at('2026-01-10T10:08+01:00')

    def pick(self, free, reserved=()):
        return pick_slot(policy=self.policy, now=self.now, finished_by=self.finished_by,
                         free=free, reserved=reserved)

    def test_round_up_and_exact_fit_including_buffer(self):
        free = [(self.now, at('2026-01-10T11:00+01:00'))]
        slot = self.pick(free)
        self.assertEqual([d.isoformat(timespec='minutes') for d in slot], [
            '2026-01-10T10:30+01:00', '2026-01-10T10:50+01:00', '2026-01-10T11:00+01:00'])

    def test_buffer_must_be_free(self):
        self.assertIsNone(self.pick([(self.now, at('2026-01-10T10:59+01:00'))]))

    def test_reservation_avoids_overlap(self):
        free = [(self.now, at('2026-01-10T12:00+01:00'))]
        held = [(at('2026-01-10T10:45+01:00'), at('2026-01-10T11:10+01:00'))]
        self.assertEqual(self.pick(free, held)[0], at('2026-01-10T11:15+01:00'))

    def test_never_suggest_past_or_time_outside_window(self):
        self.finished_by = at('2026-01-10T06:00+01:00')
        self.now = at('2026-01-10T07:02+01:00')
        self.assertEqual(self.pick([(self.finished_by, at('2026-01-10T09:00+01:00'))])[0],
                         at('2026-01-10T08:00+01:00'))
        self.now = at('2026-01-10T19:31+01:00')
        self.assertIsNone(self.pick([(self.finished_by, at('2026-01-10T23:00+01:00'))]))

    def test_three_days_including_start_day(self):
        day_three = (at('2026-01-12T09:00+01:00'), at('2026-01-12T10:00+01:00'))
        day_four = tuple(d + timedelta(days=1) for d in day_three)
        self.assertEqual(self.pick([day_four, day_three])[0], day_three[0])
        self.assertIsNone(self.pick([day_four]))

    def test_dst_change_keeps_local_window(self):
        self.now = at('2026-03-28T19:30+01:00')
        self.finished_by = self.now
        free = [(at('2026-03-29T05:00+00:00'), at('2026-03-29T07:00+00:00'))]
        self.assertEqual(self.pick(free)[0].isoformat(timespec='minutes'), '2026-03-29T08:00+02:00')

    def test_naive_inputs_are_rejected(self):
        self.now = self.now.replace(tzinfo=None)
        with self.assertRaises(ValueError):
            self.pick([])


if __name__ == '__main__':
    unittest.main(verbosity=2)
