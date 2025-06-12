* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).enableRandomWrite
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
enableRandomWrite; 
### Description
Enable random access write into this render texture on Shader Model 5.0 level shaders.
Shader Model 5.0 level pixel or compute shaders can write into arbitrary locations of some textures, called "unordered access views" in [UsingDX11GL3Features](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html). Set this flag before creating your render texture to enable this capability.  
  
When a texture has this flag set, it can be written into as one RWTexture* resources in HLSL or image resources in GLSL. It can also be set as random access write target for pixel shaders using [Graphics.SetRandomWriteTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRandomWriteTarget.html).  
  
Use [SystemInfo.SupportsRandomWriteOnRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRandomWriteOnRenderTextureFormat.html) to validate if a given format can be used as this depends on the graphics API/hardware/driver.  
  
Additional resources: [Graphics.SetRandomWriteTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRandomWriteTarget.html), [UsingDX11GL3Features](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html) [SystemInfo.SupportsRandomWriteOnRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRandomWriteOnRenderTextureFormat.html).
* * *
