* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.Depth.html

#  [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html).Depth
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
A depth render texture format.
Depth format is used to render high precision "depth" value into a render texture. Which format is actually used depends on platform support and on the number of depth bits you request through the constructor.  
  
You can also set an exact depth-stencil format with [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html) or a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) constructor that takes [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html). Use [SystemInfo.IsFormatSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.IsFormatSupported.html) to check your platform supports this.  
  
When writing shaders that use or render into a depth texture, care must be taken to ensure that they work both on OpenGL and on Direct3D, see [depth textures documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture.html).  
  
Note that not all graphics cards support depth textures. Use [SystemInfo.SupportsRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRenderTextureFormat.html) to check for support.  
  
Additional resources: [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) class, [SystemInfo.SupportsRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRenderTextureFormat.html).
* * *
