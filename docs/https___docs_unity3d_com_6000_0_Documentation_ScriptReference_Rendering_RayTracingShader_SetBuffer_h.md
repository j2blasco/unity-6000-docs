* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetBuffer.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetBuffer
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
public void SetBuffer(string name, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer); 
## Declaration
public void SetBuffer(int nameID, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer); 
## Declaration
public void SetBuffer(string name, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
## Declaration
public void SetBuffer(int nameID, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
## Declaration
public void SetBuffer(string name, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) bufferHandle); 
## Declaration
public void SetBuffer(int nameID, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) bufferHandle); 
### Parameters
Parameter | Description  
---|---  
nameID | The ID of the buffer name in shader code. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
name | The name of the buffer in shader code.  
buffer | The buffer to bind.  
bufferHandle | The handle of the buffer to bind.  
### Description
Binds an input or output compute buffer.
Only shaders defined in the .raytrace file can access the buffer you designate as the argument for this method. To make this buffer accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalBuffer.html) method instead.
* * *
