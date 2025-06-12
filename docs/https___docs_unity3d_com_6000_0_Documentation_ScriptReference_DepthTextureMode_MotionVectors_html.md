* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DepthTextureMode.MotionVectors.html

#  [DepthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DepthTextureMode.html).MotionVectors
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
Specifies whether motion vectors should be rendered (if possible).
When set, the camera renders another pass (after opaque but before Image Effects): First, a full screen pass is rendered to reconstruct screen-space motion from the camera movement, then, any moving objects have a custom pass to render their object-specific motion. The buffer uses the [RenderTextureFormat.RGHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGHalf.html) format, so this feature only works on platforms where this format is supported.  
  
Motion vectors capture the per-pixel, screen-space motion of objects from one frame to the next. Use this velocity to reconstruct previous positions, calculate blur for motion blur, or implement temporal anti-aliasing.  
  
To access the generated motion vectors, you can simple read the texture sampler: sampler2D_half _CameraMotionVectorsTexture in any opaque Image Effect.  
  
Additional resources: [Renderer.motionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-motionVectorGenerationMode.html), [Camera.depthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-depthTextureMode.html), [SkinnedMeshRenderer.skinnedMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-skinnedMotionVectors.html), [PassType.MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.MotionVectors.html), [SystemInfo.supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMotionVectors.html).
* * *
