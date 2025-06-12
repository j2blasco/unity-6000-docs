* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetBuffer
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
public void SetBuffer(int kernelIndex, string name, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer); 
## Declaration
public void SetBuffer(int kernelIndex, int nameID, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer); 
## Declaration
public void SetBuffer(int kernelIndex, string name, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
## Declaration
public void SetBuffer(int kernelIndex, int nameID, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | For which kernel the buffer is being set. See [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html).  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Name of the buffer variable in shader code.  
buffer | Buffer to set.  
### Description
Sets an input or output compute buffer.
Buffers and textures are set per-kernel. Use [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html) to find kernel index by function name.  
  
Setting a compute buffer to a kernel will leave the append/consume counter value unchanged. To set or reset the value, use [ComputeBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetCounterValue.html) or [GraphicsBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetCounterValue.html).  
  
Additional resources: [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloat.html), [SetFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloats.html), [SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInt.html), [SetInts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInts.html), [SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBool.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrix.html), [SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrixArray.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTexture.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVector.html), [SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVectorArray.html).
* * *
