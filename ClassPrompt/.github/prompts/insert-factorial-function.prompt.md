---
name: insert-factorial
description: "Insert a factorial function into the current file or selected code, matching the file's language and style"
argument-hint: "Optional: where to insert it"
agent: agent
---
Insert a factorial function into the current file, using this selected code as context if present: ${selection}

Requirements:
- Infer the language, naming style, formatting, and conventions from the active file.
- Prefer a simple iterative implementation unless nearby code strongly suggests recursion.
- If a factorial function already exists, reuse or update it instead of adding a duplicate.
- Add imports, type hints, docstrings, or comments only when the file already uses them or the language requires them.
- Keep the change minimal and avoid unrelated edits.

Behavior:
- Insert the function near the selection, unless the file structure clearly suggests a better location.
- If the location is ambiguous, ask one brief question before editing.
- If no code file is open, ask for the language and target file first.

When done:
- State where the function was inserted.
- Note any assumptions about placement or style.
- Say whether existing logic was reused.