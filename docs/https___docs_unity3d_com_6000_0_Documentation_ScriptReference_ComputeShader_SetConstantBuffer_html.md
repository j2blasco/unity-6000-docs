* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetConstantBuffer.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetConstantBuffer
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html "Go to ComputeShader Component in the Manual")
## Declaration
public void SetConstantBuffer(int nameID, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer, int offset, int size); 
## Declaration
public void SetConstantBuffer(string name, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer, int offset, int size); 
## Declaration
public void SetConstantBuffer(int nameID, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer, int offset, int size); 
## Declaration
public void SetConstantBuffer(string name, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer, int offset, int size); 
### Parameters
Parameter | Description  
---|---  
nameID | The ID of the property name for the constant buffer in shader code. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
name | The name of the buffer to bind as constant buffer.  
buffer | The buffer to bind as constant buffer.  
offset | The offset in bytes from the beginning of the ComputeBuffer to bind. Must be a multiple of [SystemInfo.constantBufferOffsetAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-constantBufferOffsetAlignment.html), or 0 if that value is 0.  
size | The number of bytes to bind.  
### Description
Sets a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) as a named constant buffer for the ComputeShader.
You can use this method to override all of the parameters in a compute shader constant buffer with the contents of a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).  
  
To use this method, the following must be true: 
  * The [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) must have been created with a corresponding [ComputeBufferType.Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Constant.html) or [GraphicsBuffer.Target.Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Constant.html) flag.
  * All the shader variants for this Material must use the same constant buffer layout for the given constant buffer.
  * The data layout of the constant buffer must match exactly the data provided in the buffer.


If the above conditions are not met, the buffer might not be bound correctly and so regular parameters will be picked up. Alternatively visual artifacts might occur.  
  
The data layout of the constant buffer may be different depending on the graphics API. This means `SetConstantBuffer` might overwrite data or set variables to the wrong values. See [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) for more information.  
  
After this function has been called with a non-null ComputeBuffer or GraphicsBuffer, you can no longer manually set the value of a variable inside the overridden constant buffer. Calls to [ComputeShader.SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloat.html) and similar where the given property name ID points to a variable inside the overridden constant buffer will have no effect.  
  
Constant buffers are bound to all kernels in a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).
* * *
