* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html

# GraphicsBuffer
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
GPU graphics data buffer, for working with geometry or compute shader data.
[ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) programs often need to read or write arbitrary data from or to memory buffers, and some rendering algorithms need a lower level access or control over geometry data than what is provided by the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) class. You can use `GraphicsBuffer` for these cases. You create the buffers from C# scripts, and then fill them with data using either C# scripts or compute shader programs.  
  
A graphics buffer is similar to an array in C#, in that it has a number of elements ([count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-count.html)) of the same size ([stride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-stride.html)). You must supply the intended buffer usage ([target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-target.html)) when you create a GraphicsBuffer; for example, you must pass [GraphicsBuffer.Target.Index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) for the buffer to be usable as a geometry index buffer.  
  
When you have finished working with the buffer, you must manually release the GPU memory. You can do this using C# dispose pattern, or by calling [Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Release.html).  
  
Additional resources: [Graphics.RenderPrimitivesIndexed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexed.html), [Graphics.RenderPrimitivesIndexedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexedIndirect.html), [Graphics.CopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Shader.SetGlobalBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalBuffer.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html).
### Properties
Property | Description  
---|---  
[bufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-bufferHandle.html) | The internal handle of this GraphicsBuffer. Only valid until the buffer is disposed of. (Read Only)  
[count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-count.html) | Number of elements in the buffer (Read Only).  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-name.html) | The debug label for the graphics buffer (setter only).  
[stride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-stride.html) | Size of one element in the buffer. For index buffers, this must be either 2 or 4 bytes (Read Only).  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-target.html) | Target, which specifies the intended target(s) of this GraphicsBuffer (Read Only).  
[usageFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-usageFlags.html) | The flags that specify how this GraphicsBuffer can be used or updated (Read Only).  
### Constructors
Constructor | Description  
---|---  
[GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-ctor.html) | Create a Graphics Buffer.  
### Public Methods
Method | Description  
---|---  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.GetData.html) | Read data values from the buffer into an array. The array can only use blittable types.  
[GetNativeBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.GetNativeBufferPtr.html) | Retrieve a native (underlying graphics API) pointer to the buffer.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IsValid.html) | Returns true if this graphics buffer is valid, or false otherwise.  
[LockBufferForWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.LockBufferForWrite.html) | Begins a write operation to the buffer  
[Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Release.html) | Release a Graphics Buffer.  
[SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetCounterValue.html) | Sets counter value of append/consume buffer.  
[SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetData.html) | Set the buffer with values from an array.  
[UnlockBufferAfterWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UnlockBufferAfterWrite.html) | Ends a write operation to the buffer  
### Static Methods
Method | Description  
---|---  
[CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.CopyCount.html) | Copy the counter value of a GraphicsBuffer into another buffer.  
* * *
