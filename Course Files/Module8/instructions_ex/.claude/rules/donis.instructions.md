---
description: TypeScript coding rules for files under src/
paths:
  - "src/**/*.ts"
  - "src/**/*.tsx"
---

When working on TypeScript/React code in src/, follow these rules:

- Prefer explicit types for public functions and exported values.
- Do not use `any` unless absolutely necessary; prefer `unknown` + narrowing.
- Use `const` by default; avoid `let` unless reassignment is required.
- Keep functions small and single-purpose.
- For React components, prefer function components and hooks.
- Add/adjust tests when changing behavior (keep tests minimal and readable).
- When refactoring, preserve existing public APIs unless asked to change them.