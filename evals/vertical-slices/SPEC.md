An operator starts a run from discovered work. The run accepts its first
completed child, publishes accepted progress to one draft pull request, and
resumes that accepted progress safely after a process restart. The controller
then repairs concrete controller or CI defects and reruns the affected work.
Finally, it audits the exact candidate and marks that candidate ready.

The complete workflow must then be proven in a disposable Epic on a real
hosting service. Creating that Epic requires explicit authorization, and no
disposable repository has been provisioned.
