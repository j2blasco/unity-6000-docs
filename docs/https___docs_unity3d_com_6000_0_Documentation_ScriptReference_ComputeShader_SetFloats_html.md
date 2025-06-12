* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloats.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetFloats
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
public void SetFloats(string name, params float[] values); 
## Declaration
public void SetFloats(int nameID, params float[] values); 
### Parameters
Parameter | Description  
---|---  
name | Array variable name in the shader code.  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
values | Value array to set.  
### Description
Set multiple consecutive float parameters at once.
This function can be used to set float vector, float array or float vector array values. For example, float4 myArray[4] in the compute shader can be filled by passing 16 floats. See [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) for information on data layout rules and cross-platform compatibility.  
  
This API feeds raw data to the constant buffer, so the provided data must follow the HLSL constant buffer data layout rules. This means that the the array elements must be aligned on float4; for example, float4 data requires no padding, float3 data needs one float padding for each element, float2 data needs two floats, and so on.  
  
Constant buffers are shared between all kernels in a single compute shader asset. Therefore this function affects all kernels in this ComputeShader.  
  
Additional resources: [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloat.html), [SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInt.html), [SetInts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInts.html), [SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBool.html), [SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrix.html), [SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrixArray.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTexture.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVector.html), [SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVectorArray.html).
* * *
