* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTexture.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetTexture
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
public void SetTexture(int kernelIndex, string name, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
## Declaration
public void SetTexture(int kernelIndex, int nameID, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
## Declaration
public void SetTexture(int kernelIndex, string name, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture, int mipLevel); 
## Declaration
public void SetTexture(int kernelIndex, int nameID, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture, int mipLevel); 
## Declaration
public void SetTexture(int kernelIndex, string name, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) texture, int mipLevel, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
## Declaration
public void SetTexture(int kernelIndex, int nameID, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) texture, int mipLevel, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | For which kernel the texture is being set. See [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html).  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Name of the buffer variable in shader code.  
texture | Texture to set.  
mipLevel | Optional mipmap level of the read-write texture.  
element | Optional parameter that specifies the type of data to set from the RenderTexture.  
### Description
Set a texture parameter.
This function can either set a regular texture that is read in the compute shader, or an output texture that is written into by the shader. For an output texture, it has to be a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) with random write flag enabled, see [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html).  
  
Please note that the mipLevel parameter is ignored unless the shader specifies a read-write (unordered access) texture.  
  
Buffers and textures are set per-kernel. Use [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html) to find kernel index by function name.  
  
By specifying a `RenderTextureSubElement`, you can indicate which type of data to set from the RenderTexture. The possible options are: [RenderTextureSubElement.Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Color.html), [RenderTextureSubElement.Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Depth.html), and [RenderTextureSubElement.Stencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Stencil.html).  
  
Additional resources: [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html), Additional resources: [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloat.html), [SetFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloats.html), [SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInt.html), [SetInts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInts.html), [SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBool.html), [SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrix.html), [SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrixArray.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVector.html), [SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVectorArray.html)., [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html), [RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html).
* * *
