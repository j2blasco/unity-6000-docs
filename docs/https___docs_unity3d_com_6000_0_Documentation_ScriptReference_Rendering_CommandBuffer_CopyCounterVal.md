* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyCounterValue.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).CopyCounterValue
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
public void CopyCounterValue([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) dst, uint dstOffsetBytes); 
## Declaration
public void CopyCounterValue([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) dst, uint dstOffsetBytes); 
## Declaration
public void CopyCounterValue([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) dst, uint dstOffsetBytes); 
## Declaration
public void CopyCounterValue([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) dst, uint dstOffsetBytes); 
### Parameters
Parameter | Description  
---|---  
src | Append/consume buffer to copy the counter from.  
dst | A buffer to copy the counter to.  
dstOffsetBytes | Target byte offset in `dst` buffer.  
### Description
Adds a command to copy [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) counter value.
Note: this command can not be used on [LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html) command buffers.  
  
Additional resources: [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html) and [GraphicsBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.CopyCount.html).
* * *
