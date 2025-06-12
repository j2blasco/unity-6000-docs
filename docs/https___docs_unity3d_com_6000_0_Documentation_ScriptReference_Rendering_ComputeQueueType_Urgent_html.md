* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.Urgent.html

#  [ComputeQueueType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html).Urgent
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
This queue type would be the choice for compute tasks requiring processing as soon as possible and would be prioritised over the graphics queue.
Note due to the way that Unity internally deferrs it's submission of command buffers to the GPU users should not expect compute shader dispatches sent to Urgent async compute queues to complete and be available on the CPU immediately. On some platforms it is possible for the OS to schedule GPU work that would take priority over urgent async compute tasks.
* * *
