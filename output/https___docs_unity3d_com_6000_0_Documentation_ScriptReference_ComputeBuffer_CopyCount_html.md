* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html

#  [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html).CopyCount
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
public static void CopyCount([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) dst, int dstOffsetBytes); 
### Parameters
Parameter | Description  
---|---  
src | Append/consume buffer to copy the counter from.  
dst | A buffer to copy the counter to.  
dstOffsetBytes | Target byte offset in `dst`.  
### Description
Copy counter value of append/consume buffer into another buffer.
Append/consume and counter buffers (see [ComputeBufferType.Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Append.html), [ComputeBufferType.Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Counter.html)) keep track of the number of elements in them with a special counter variable. CopyCount takes a buffer as `src`, and copies its counter value into `dst` buffer at given byte offset.  
  
This is most commonly used in conjunction with [Graphics.DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirect.html), to render arbitrary number of primitives without reading their count back to the CPU.  
  
On DX11 there is a restriction on the `dst` buffer - it must have been created with [ComputeBufferType.Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Raw.html) or [ComputeBufferType.IndirectArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.IndirectArguments.html) type. On other platforms `dst` can be any type.  
  
Additional resources: [SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetCounterValue.html).
* * *
