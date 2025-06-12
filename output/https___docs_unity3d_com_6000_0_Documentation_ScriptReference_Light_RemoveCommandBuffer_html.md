* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffer.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).RemoveCommandBuffer
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
public void RemoveCommandBuffer([Rendering.LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html) evt, [Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) buffer); 
### Parameters
Parameter | Description  
---|---  
evt | When to execute the command buffer during rendering.  
buffer | The buffer to execute.  
### Description
Remove command buffer from execution at a specified place.
If the same buffer is added multiple times on this light event, all occurrences of it will be removed.  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [RemoveCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffers.html), [RemoveAllCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveAllCommandBuffers.html), [AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html), [GetCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.GetCommandBuffers.html).
* * *
