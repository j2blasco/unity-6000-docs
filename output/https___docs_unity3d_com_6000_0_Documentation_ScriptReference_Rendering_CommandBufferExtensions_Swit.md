* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBufferExtensions.SwitchOutOfFastMemory.html

#  [CommandBufferExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBufferExtensions.html).SwitchOutOfFastMemory
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
## Declaration
public static void SwitchOutOfFastMemory([Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cmd, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rid, bool copyContents); 
### Parameters
Parameter | Description  
---|---  
rid | The render target to remove from fast GPU memory.  
copyContents | When this value is true, Unity copies the existing contents of the render target when it removes it from fast GPU memory. When this value is false, Unity does not copy the existing contents of the render target when it removes it from fast GPU memory. Set this value to true if you plan to add to the existing contents, and set it to false if you plan to overwrite or clear the existing contents. Where possible, set this value to false for better performance.  
### Description
Adds a command to remove a given render target from fast GPU memory.
On certain console platforms, you can put render targets in fast GPU memory for improved rendering performance.  
  
On platforms that do not support fast GPU memory, this function does nothing.  
  
On platforms that support fast GPU memory, the results of this function depend on the state of the render target at the time that the graphics API executes this command. If the render target is in fast GPU memory, Unity removes the render target from fast GPU memory. If the render target is not in fast GPU memory, Unity does nothing. There is no performance cost in this case.  
  
Additional resources: [CommandBufferExtensions.SwitchIntoFastMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBufferExtensions.SwitchIntoFastMemory.html)
* * *
