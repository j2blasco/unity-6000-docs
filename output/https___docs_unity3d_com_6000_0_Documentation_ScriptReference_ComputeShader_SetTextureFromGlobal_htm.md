* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTextureFromGlobal.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetTextureFromGlobal
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
public void SetTextureFromGlobal(int kernelIndex, string name, string globalTextureName); 
## Declaration
public void SetTextureFromGlobal(int kernelIndex, int nameID, int globalTextureNameID); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | For which kernel the texture is being set. See [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html).  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Name of the buffer variable in shader code.  
globalTextureName | Global texture property to assign to shader.  
globalTextureNameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
### Description
Set a texture parameter from a global texture property.
This function can either set a regular texture that is read in the compute shader, or an output texture that is written into by the shader. For an output texture, it has to be a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) with random write flag enabled, see [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html).  
  
Buffers and textures are set per-kernel. Use [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html) to find kernel index by function name.  
  
Additional resources: [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html), [SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTexture.html), [Shader.SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html).
```
// Assign the CameraMotionVectorsTexture global texture to a compute texture
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;  
  
public class SampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int renderTargetWidth;
    public int renderTargetHeight;
    ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) myComputeShader;  
  
    void ComputeUsingMotionVector()
    {
        int kKernelIndex = 0;  
  
        myComputeShader.SetTextureFromGlobal(kKernelIndex, "computeTexture", "_CameraMotionVectorsTexture");
        myComputeShader.Dispatch(kKernelIndex, renderTargetWidth, renderTargetHeight, 1);
    }
}

```

* * *
