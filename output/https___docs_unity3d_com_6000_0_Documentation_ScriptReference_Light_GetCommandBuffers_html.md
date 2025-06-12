* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.GetCommandBuffers.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).GetCommandBuffers
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
## Declaration
public CommandBuffer[] GetCommandBuffers([Rendering.LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html) evt); 
### Parameters
Parameter | Description  
---|---  
evt | When to execute the command buffer during rendering.  
### Returns
**CommandBuffer[]** Array of command buffers. 
### Description
Get command buffers to be executed at a specified place.
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html), [RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffer.html).
* * *
