* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer-ctor.html

# ComputeBuffer Constructor
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
public ComputeBuffer(int count, int stride); 
## Declaration
public ComputeBuffer(int count, int stride, [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html) type); 
## Declaration
public ComputeBuffer(int count, int stride, [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html) type, [ComputeBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.html) usage); 
### Parameters
Parameter | Description  
---|---  
count | Number of elements in the buffer.  
stride | Size of one element in the buffer, in bytes. Must be a multiple of 4 and less than 2048, and match the size of the buffer type in the shader. See [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) for cross-platform compatibility information.  
type | Type of the buffer, default is [ComputeBufferType.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Default.html) (structured buffer).  
usage | Usage mode of the buffer, default is ComputeBufferModeImmutable.  
### Description
Create a Compute Buffer.
Use [Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.Release.html) to release the buffer when no longer needed.  
  
Additional resources: [SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) class, [Shader.SetGlobalBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalBuffer.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html), [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).
* * *
