An operator starts a run from discovered jobs. The run accepts its first
completed job, publishes accepted progress to one draft pull request, and
resumes that accepted progress safely after a process restart. The service then
repairs concrete orchestration or CI defects and reruns the affected work.
Finally, it audits the exact candidate and marks that candidate ready.

The complete workflow must then be proven in a disposable repository on a real
hosting service. Creating that repository requires explicit authorization, and
none has been provisioned.
