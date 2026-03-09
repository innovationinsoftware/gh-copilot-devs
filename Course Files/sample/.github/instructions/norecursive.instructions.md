---
description: Describe when these instructions should be loaded
# applyTo: 'Describe when these instructions should be loaded' # when provided, instructions will automatically be added to the request context when the pattern matches an attached file
---

# No Recursive Instructions
- Do not use recursive instructions. Recursive instructions are instructions that reference themselves, either directly or indirectly. This can lead to infinite loops and can cause the model to generate irrelevant or nonsensical responses.
- prefer non-recursive function because of stack overflow and performance issues. Recursive functions can lead to stack overflow if the recursion depth is too large, and they can be less efficient than iterative solutions due to the overhead of function calls.
- no exceptions to this rule. All instructions must be non-recursive, regardless of the context or use case.