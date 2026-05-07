---
name: renameVariable
description: Rename a variable safely in the current code context.
argument-hint: oldName, newName, and optional scope (selection/file/project)
---
Rename a variable in the specified code scope.

Inputs:
- Old variable name: {{oldName}}
- New variable name: {{newName}}
- Scope: {{scope}} (selection, current file, or project)

Requirements:
1. Rename only the intended symbol and all of its references within the given scope.
2. Do not rename unrelated variables, parameters, methods, or classes with similar names.
3. Preserve existing behavior, formatting style, and code structure.
4. Update usages consistently so the code remains valid.
5. If the rename could cause shadowing or conflicts, propose a safe alternative and explain why.

Output:
- Apply the rename directly.
- Summarize what was renamed and where.