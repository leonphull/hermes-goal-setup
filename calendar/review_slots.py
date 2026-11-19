"""Select a review slot from caller-supplied intervals. No I/O."""

from datetime import datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo


EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def utc(value):
    if not isinstance(value, datetime) or value.utcoffset() is None:
        raise ValueError("Expected a timezone-aware datetime.")
    return value.astimezone(timezone.utc)


def intervals_utc(intervals):
    pairs = [(utc(left), utc(right)) for left, right in intervals]
    if any(left >= right for left, right in pairs):
        raise ValueError("Every interval must have a positive duration.")
    merged = []
    for left, right in sorted(pairs):
        if merged and left <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(right, merged[-1][1]))
        else:
            merged.append((left, right))
    return merged


def blocks_without_reservations(left, right, reserved):
    cursor = left
    for start, end in reserved:
        if end <= cursor:
            continue
        if start >= right:
            break
        if cursor < start:
            yield cursor, start
        cursor = max(cursor, end)
        if cursor >= right:
            return
    if cursor < right:
        yield cursor, right


def round_up(value, grid):
    ticks, remainder = divmod(value - EPOCH, grid)
    return EPOCH + (ticks + bool(remainder)) * grid


def positive_int(policy, key, minimum=1):
    value = policy[key]
    if type(value) is not int or value < minimum:
        raise ValueError(f"Invalid policy field: {key}")
    return value


def pick_slot(*, policy, now, finished_by, free, reserved=()):
    """Return start/end/buffer_end in the policy timezone, or None.

    `free` must already account for applicable calendar conflicts. `reserved`
    supplies the held intervals (including buffer) of other open runs.
    All input intervals are half-open and all datetimes must carry an offset.
    """
    tz = ZoneInfo(policy['timezone'])
    window_start = time.fromisoformat(policy['window_start'])
    window_end = time.fromisoformat(policy['window_end'])
    if window_start.tzinfo or window_end.tzinfo or window_start >= window_end:
        raise ValueError("Expected an increasing local daytime window.")
    review = timedelta(minutes=positive_int(policy, 'review_minutes'))
    buffer = timedelta(minutes=positive_int(policy, 'buffer_minutes', 0))
    grid = timedelta(minutes=positive_int(policy, 'grid_minutes'))
    lead = timedelta(minutes=positive_int(policy, 'after_finish_minutes', 0))
    horizon = positive_int(policy, 'search_days')
    earliest = max(utc(now), utc(finished_by) + lead)
    first_day = earliest.astimezone(tz).date()
    free = intervals_utc(free)
    reserved = intervals_utc(reserved)

    for offset in range(horizon):
        day = first_day + timedelta(days=offset)
        window_left = utc(datetime.combine(day, window_start, tz))
        window_right = utc(datetime.combine(day, window_end, tz))
        for left, right in free:
            left = max(left, earliest, window_left)
            right = min(right, window_right)
            if left >= right:
                continue
            for block_left, block_right in blocks_without_reservations(left, right, reserved):
                start = round_up(block_left, grid)
                end = start + review
                if end + buffer <= block_right:
                    return tuple(value.astimezone(tz) for value in (start, end, end + buffer))
    return None
