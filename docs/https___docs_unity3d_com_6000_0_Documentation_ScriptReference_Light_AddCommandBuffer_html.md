* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).AddCommandBuffer
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
public void AddCommandBuffer([Rendering.LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html) evt, [Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) buffer); 
## Declaration
public void AddCommandBuffer([Rendering.LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html) evt, [Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) buffer, [Rendering.ShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.html) shadowPassMask); 
### Parameters
Parameter | Description  
---|---  
evt | When to execute the command buffer during rendering.  
buffer | The buffer to execute.  
shadowPassMask | A mask specifying which shadow passes to execute the buffer for.  
### Description
Add a command buffer to be executed at a specified place.
Multiple command buffers can be set to execute at the same light event (or even the same buffer can be added multiple times). To remove command buffer from execution, use [RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffer.html).  
  
Passing a shadow pass mask allows detailed control over which shadow passes will execute the buffer.  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [ShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.html), [RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffer.html), [GetCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.GetCommandBuffers.html).
* * *
