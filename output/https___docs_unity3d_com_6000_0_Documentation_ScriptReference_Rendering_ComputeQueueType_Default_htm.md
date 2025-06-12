* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.Default.html

#  [ComputeQueueType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html).Default
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
This queue type would be the choice for compute tasks supporting or as optimisations to graphics processing. CommandBuffers sent to this queue would be expected to complete within the scope of a single frame and likely be synchronised with the graphics queue via GPUFences. Dispatches on default queue types would execute at a lower priority than graphics queue tasks.
* * *
