* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.CopyCount.html

#  [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).CopyCount
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
## Declaration
public static void CopyCount([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) dst, int dstOffsetBytes); 
## Declaration
public static void CopyCount([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) dst, int dstOffsetBytes); 
## Declaration
public static void CopyCount([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) dst, int dstOffsetBytes); 
### Parameters
Parameter | Description  
---|---  
src | The source GraphicsBuffer.  
dst | The destination GraphicsBuffer.  
dstOffsetBytes | The destination buffer offset in bytes.  
### Description
Copy the counter value of a GraphicsBuffer into another buffer.
Append/consume buffers (see [GraphicsBuffer.Target.Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Append.html) and counter buffers [GraphicsBuffer.Target.Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Counter.html)) keep track of the number of elements in them with a special counter variable. CopyCount takes such a buffer as `src`, and copies its counter value into `dst` buffer at given byte offset.  
  
This is most commonly used in conjunction with [Graphics.RenderPrimitivesIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndirect.html), to render an arbitrary number of primitives without reading their count back to the CPU.  
  
The `src` buffer must have been created with a usage target of [GraphicsBuffer.Target.Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Append.html) or [GraphicsBuffer.Target.Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Counter.html).  
  
On DirectX 11 and 12, the `dst` buffer must have been created with a usage target of [GraphicsBuffer.Target.Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html) or [GraphicsBuffer.Target.IndirectArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.IndirectArguments.html). For other graphics APIs, there is no such restriction.  
  
Additional resources: [SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetCounterValue.html).
* * *
