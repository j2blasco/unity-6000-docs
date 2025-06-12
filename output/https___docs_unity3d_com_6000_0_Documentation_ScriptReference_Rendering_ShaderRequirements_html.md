* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.html

# ShaderRequirements
enumeration
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
### Description
Shader features required by a specific shader. Features are bit flags.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.None.html) | No shader requirements.  
[BaseShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.BaseShaders.html) | Indicates that basic shader capability i.e. Shader Model level 2.0 is required.  
[Interpolators10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Interpolators10.html) | Indicates that support for at least 10 interpolators is required.  
[Interpolators32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Interpolators32.html) | Indicates that support for at least 32 interpolators is required.  
[MRT4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.MRT4.html) | Indicates that support for multiple render targets (at least 4) is required i.e. support for fragment shaders that can output at least 4 values.  
[MRT8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.MRT8.html) | Indicates that support for multiple render targets (at least 8) is required i.e. support for fragment shaders that can output at least 8 values.  
[Derivatives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Derivatives.html) | Indicates that support for derivative (ddx/ddy) instructions from the fragment shader stage is required.  
[SampleLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.SampleLOD.html) | Indicates that support for texture sampling from the fragment shader stage with an explicit mipmap level is required.  
[FragCoord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.FragCoord.html) | Indicates that support for pixel position (SV_Position) input to the fragment shader stage is required.  
[FragClipDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.FragClipDepth.html) | Indicates that support for pixel depth (SV_Position.zw) input to the fragment shader stage is required.  
[Interpolators15Integers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Interpolators15Integers.html) | Indicates that support for at least 15 integers and interpolators in total are required. Unity bundles them together because it is extremely unlikely a GPU/API will ever exist that only has part of that.  
[Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Texture2DArray.html) | Indicates that support for 2D array textures (Texture2DArray) is required.  
[Instancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Instancing.html) | Indicates that support for the SV_InstanceID input semantic is required.  
[Geometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Geometry.html) | Indicates that geometry shader stage support is required.  
[CubeArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.CubeArray.html) | Indicates that cubemap array (TextureCubeArray) support is required.  
[Compute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.Compute.html) |  Indicates that compute shader support is required.   
[RandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.RandomWrite.html) | Indicates that support for random-write textures (UAVs) is required.  
[TessellationCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.TessellationCompute.html) | Indicates that support for tessellation using a compute shader for control point processing is required. The Metal graphics API requires this feature for tessellation.  
[TessellationShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.TessellationShaders.html) | Indicates that support for tessellation using hull and domain shader stages is required.  
[SparseTexelResident](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.SparseTexelResident.html) | Indicates that support of sparse textures with sampling instructions that return residency information is requred.  
[FramebufferFetch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.FramebufferFetch.html) | Indicates that framebuffer fetch support is required. This is the ability to have fragment shader color arguments with in/out modifiers.  
[MSAATextureSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.MSAATextureSamples.html) | Indicates that support for MSAA textures (e.g. Texture2DMS) is required.  
[SetRTArrayIndexFromAnyShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.SetRTArrayIndexFromAnyShader.html) | Indicates that support for setting the render target array index (SV_RenderTargetArrayIndex) from all shader stages (not just from the geometry shader stage) is required.  
* * *
