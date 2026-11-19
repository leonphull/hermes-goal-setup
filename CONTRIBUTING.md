# Contributing

Thank you for your help. Keep changes small and clear.

1. **Open an issue first** for a large change. Describe the problem in one or two sentences.
2. **Write in the house style.** Use BLUF and short, active sentences. See [output-style/OUTPUT-STYLE.md](output-style/OUTPUT-STYLE.md).
3. **Do not add secrets.** Do not add credentials, tokens, real Notion IDs, calendar IDs, endpoints or personal data. Use placeholders such as `<LOCAL_ENDPOINT>`.
4. **Keep templates passive.** Nothing in this repo must start, connect or write on its own.
5. **Run the tests** before you open a pull request:

   ```sh
   python3 -B calendar/test_review_slots.py
   ```

6. **Describe the change** in the pull request: what changed, why, and how you verified it.

By contributing, you agree that your contribution is licensed under the [MIT License](LICENSE).
