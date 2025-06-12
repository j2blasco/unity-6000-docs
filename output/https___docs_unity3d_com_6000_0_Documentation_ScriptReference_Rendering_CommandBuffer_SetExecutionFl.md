* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetExecutionFlags.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetExecutionFlags
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
public void SetExecutionFlags([Rendering.CommandBufferExecutionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBufferExecutionFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
flags | The flags to set.  
### Description
Set flags describing the intention for how the command buffer will be executed.
Setting execution flags to any value other than none allows exceptions to be thrown when issuing commands that are not compatible with the intended method of execution. For example, command buffers intended for use with async compute cannot contain commands that are used purely for rendering. This method can only be called against empty command buffers, so call it immediately after construction or after calling [CommandBuffer.Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.Clear.html).
* * *
