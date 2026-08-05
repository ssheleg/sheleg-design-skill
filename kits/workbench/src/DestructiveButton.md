---
category: Signature
---

The pack names three button kinds and the spine carries two, so this is the
third: a red-border ghost that fills to `--danger-weak` on hover and keeps its
label in `--danger` throughout. Use it for the actions a screen cannot take
back — deleting a workspace, revoking a key, dropping a table.

**The confirm step is part of the component, not the caller's problem.** The
first click swaps the label to `confirmLabel` (default `"Confirm"`) and arms
the button; the second fires `onClick`. Put behind the caller, that step is
optional, and the one screen that forgets it is the one that deletes something.
Moving focus away disarms it — a button left armed behind you is the exact
failure this is here to prevent. No timer and no animation are involved, so it
behaves identically under `prefers-reduced-motion`.

It deliberately has no `size` and no `variant`. A destructive action that needs
to be large or quiet is a design problem upstream of this component.

```tsx
<DestructiveButton confirmLabel="Delete — confirm" onClick={deleteWorkspace}>
  Delete workspace
</DestructiveButton>
```
