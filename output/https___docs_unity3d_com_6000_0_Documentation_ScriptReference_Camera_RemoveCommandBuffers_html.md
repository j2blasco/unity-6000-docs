* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveCommandBuffers.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).RemoveCommandBuffers
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public void RemoveCommandBuffers([Rendering.CameraEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html) evt); 
### Parameters
Parameter | Description  
---|---  
evt | When to execute the command buffer during rendering.  
### Description
Remove command buffers from execution at a specified place.
This function removes all command buffers set on the specified camera event. This API is only available with the Built-in renderer.  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveCommandBuffer.html), [RemoveAllCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveAllCommandBuffers.html).
* * *
