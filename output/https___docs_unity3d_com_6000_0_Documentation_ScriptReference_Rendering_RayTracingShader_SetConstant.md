* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetConstantBuffer.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetConstantBuffer
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
name | The name of the constant buffer in shader code.  
buffer | The buffer to bind as constant buffer.  
offset | The offset in bytes from the beginning of the ComputeBuffer or GraphicsBuffer to bind. Must be a multiple of [SystemInfo.constantBufferOffsetAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-constantBufferOffsetAlignment.html), or 0 if that value is 0.  
size | The number of bytes to bind.  
### Description
Binds a constant buffer created through a ComputeBuffer or a GraphicsBuffer.
Use this method to override all of the shader parameters in the given constant buffer with the contents of the given ComputeBuffer or GraphicsBuffer.  
  
When using a ComputeBuffer as parameter, it must have been created with a [ComputeBufferType.Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Constant.html) flag. Similarly, when a GraphicsBuffer is used as parameter, it must have been created with a [GraphicsBuffer.Target.Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Constant.html) flag. The data layout of the constant buffer must match exactly with the data provided in the ComputeBuffer or GraphicsBuffer.  
  
If the obove conditions are not met, the buffer might not be bound correctly and so regular parameters will be picked up. Alternatively visual artifacts might occur.  
  
After this function has been called with a non-null ComputeBuffer or GraphicsBuffer, you can no longer manually set the value of a variable inside the overridden constant buffer. Calls to [RayTracingShader.SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetFloat.html) and similar where the given property name ID points to a variable inside the overridden constant buffer will have no effect.  
  
Only shaders defined in the .raytrace file can access the constant buffer you designate as the argument for this method. To make this buffer accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalConstantBuffer.html) method instead.
* * *
