* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html

# ComputeQueueType
enumeration
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
Describes the desired characteristics with respect to prioritisation and load balancing of the queue that a command buffer being submitted via [Graphics.ExecuteCommandBufferAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBufferAsync.html) or [[ScriptableRenderContext.ExecuteCommandBufferAsync] should be sent to.
### Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.Default.html) | This queue type would be the choice for compute tasks supporting or as optimisations to graphics processing. CommandBuffers sent to this queue would be expected to complete within the scope of a single frame and likely be synchronised with the graphics queue via GPUFences. Dispatches on default queue types would execute at a lower priority than graphics queue tasks.  
[Background](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.Background.html) | Background queue types would be the choice for tasks intended to run for an extended period of time, e.g for most of a frame or for several frames. Dispatches on background queues would execute at a lower priority than gfx queue tasks.  
[Urgent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.Urgent.html) | This queue type would be the choice for compute tasks requiring processing as soon as possible and would be prioritised over the graphics queue.  
* * *
