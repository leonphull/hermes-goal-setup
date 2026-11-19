// The final button is the only action that queues and submits feedback.
(() => {
  const box = document.querySelector('[data-rv-decision]');
  if (!box) return;
  const button = box.querySelector('[data-rv-send]');
  const state = box.querySelector('[data-rv-state]');
  const copy = box.querySelector('[data-rv-copy]');
  const note = box.querySelector('[data-rv-note]');
  const chosen = () => box.querySelector('input[type=radio]:checked');
  let sending = false;
  let submitted = false;

  function refresh() {
    button.disabled = sending || submitted || !chosen();
  }

  box.addEventListener('input', () => {
    if (!submitted && !sending) {
      state.textContent = '';
      copy.hidden = true;
    }
    refresh();
  });
  window.addEventListener('message', () => setTimeout(refresh, 0));
  refresh();

  button.addEventListener('click', async () => {
    const option = chosen();
    if (sending || submitted || !option) return;
    const scope = box.dataset.rvDecision;
    const revision = box.dataset.rvRevision;
    const data = { scope, revision, choice: option.value, note: note.value };
    const message = `Decision [${scope}, ${revision}]: ${data.choice}` +
      (data.note ? `\nNote: ${data.note}` : '');
    const bridge = window.lavish;
    if (typeof bridge?.queuePrompt !== 'function' || typeof bridge?.sendQueuedPrompts !== 'function') {
      copy.value = message;
      copy.hidden = false;
      state.textContent = 'Not sent. Copy the text into the chat.';
      copy.select();
      return;
    }
    sending = true;
    refresh();
    try {
      await bridge.queuePrompt(message, { queueKey: `rv-${scope}`, tag: 'decision', data, element: box });
      await bridge.sendQueuedPrompts();
      submitted = true;
      state.textContent = 'Submitted. Waiting for confirmation from the agent.';
    } catch {
      state.textContent = 'Delivery not confirmed. Check the session before you send again.';
      submitted = true;
    } finally {
      sending = false;
      refresh();
    }
  });
})();
