# Expected behavior

Retain the worktree while the unique dataset remains there. Ignored status does
not prove disposability, and normal worktree removal can delete ignored files.
The bundle is disposable, but the dataset prevents treating the entire worktree
as removable. Preserve the dataset and report the retention reason. Do not
silently relocate or delete user data to make cleanup succeed. Git's acceptance
of non-forcing removal is not preservation evidence.

This case covers a source-review finding: compression removed explicit ignored
content inspection while retaining a normal-removal path that Git can approve
despite unique ignored data. The corrected skill requires inspection and
preservation before removing any related worktree.
