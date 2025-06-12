* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloat.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetFloat
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
public void SetFloat(string name, float val); 
## Declaration
public void SetFloat(int nameID, float val); 
### Parameters
Parameter | Description  
---|---  
name | Variable name in shader code.  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
val | Value to set.  
### Description
Set a float parameter.
Constant buffers are shared between all kernels in a single compute shader asset. Therefore this function affects all kernels in this ComputeShader.  
  
Additional resources: [SetFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloats.html), [SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInt.html), [SetInts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInts.html), [SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBool.html), [SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrix.html), [SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrixArray.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTexture.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVector.html), [SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVectorArray.html).
* * *
