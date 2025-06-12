* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.html

# BuiltinRenderTextureType
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
Built-in temporary render textures produced during camera's rendering.
When camera is rendering the Scene, in some cases it can produce temporary render textures in the process (e.g. depth textures, deferred G-buffer etc.). This enum indicates these temporary render textures.  
  
BuiltinRenderTextureType can be used as a [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) in some functions of [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html).
### Properties
Property | Description  
---|---  
[PropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.PropertyName.html) | A globally set property name.  
[BufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.BufferPtr.html) | The raw RenderBuffer pointer to be used.  
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.RenderTexture.html) | The given RenderTexture.  
[CurrentActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.CurrentActive.html) | Currently active render target.  
[CameraTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.CameraTarget.html) | Target texture of currently rendering camera.  
[Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.Depth.html) | Camera's depth texture.  
[DepthNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.DepthNormals.html) | Camera's depth+normals texture.  
[ResolvedDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.ResolvedDepth.html) | Resolved depth buffer from deferred.  
[GBuffer0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer0.html) | Deferred shading G-buffer #0 (typically diffuse color).  
[GBuffer1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer1.html) | Deferred shading G-buffer #1 (typically specular + roughness).  
[GBuffer2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer2.html) | Deferred shading G-buffer #2 (typically normals).  
[GBuffer3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer3.html) | Deferred shading G-buffer #3 (typically emission/lighting).  
[Reflections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.Reflections.html) | Reflections gathered from default reflection and reflections probes.  
[MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.MotionVectors.html) | Motion Vectors generated when the camera has motion vectors enabled.  
[GBuffer4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer4.html) | Deferred shading G-buffer #4 (typically occlusion mask for static lights if any).  
[GBuffer5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer5.html) | G-buffer #5 Available.  
[GBuffer6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer6.html) | G-buffer #6 Available.  
[GBuffer7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.GBuffer7.html) | G-buffer #7 Available.  
* * *
