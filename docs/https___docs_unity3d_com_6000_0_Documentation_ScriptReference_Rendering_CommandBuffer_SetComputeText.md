* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeTextureParam.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetComputeTextureParam
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
public void SetComputeTextureParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rt); 
## Declaration
public void SetComputeTextureParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rt); 
## Declaration
public void SetComputeTextureParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rt, int mipLevel); 
## Declaration
public void SetComputeTextureParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rt, int mipLevel); 
## Declaration
public void SetComputeTextureParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rt, int mipLevel, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
## Declaration
public void SetComputeTextureParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) rt, int mipLevel, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
### Parameters
Parameter | Description  
---|---  
computeShader |  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) to set parameter for.  
kernelIndex | Which kernel the texture is being set for. See [ComputeShader.FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html).  
name | Name of the texture variable in shader code.  
nameID | Property name ID. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
rt | Texture value or identifier to set, see [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html).  
mipLevel | Optional mipmap level of the read-write texture.  
element | Optional parameter that specifies the type of data to set from the RenderTexture.  
### Description
Adds a command to set a texture parameter on a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).
Textures and buffers are set per-kernel. Use [ComputeShader.FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html) to find kernel index by function name. Please note that the mipLevel parameter is ignored unless the shader specifies a read-write (unordered access) texture.  
  
By specifying a `RenderTextureSubElement`, you can indicate which type of data to set from the RenderTexture. The possible options are: [RenderTextureSubElement.Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Color.html), [RenderTextureSubElement.Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Depth.html), and [RenderTextureSubElement.Stencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Stencil.html).  
  
Additional resources: [DispatchCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DispatchCompute.html), [SetComputeFloatParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParam.html), [SetComputeFloatParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParams.html), [SetComputeIntParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeIntParam.html), [SetComputeIntParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeIntParams.html), [SetComputeMatrixParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeMatrixParam.html), [SetComputeMatrixArrayParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeMatrixArrayParam.html), [SetComputeVectorParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorParam.html), [SetComputeVectorArrayParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorArrayParam.html), [SetComputeBufferParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeBufferParam.html), [RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html).
* * *
