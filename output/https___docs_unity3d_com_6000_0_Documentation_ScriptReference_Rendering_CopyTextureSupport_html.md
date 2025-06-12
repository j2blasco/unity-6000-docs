* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.html

# CopyTextureSupport
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
Support for various [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) cases.
Most modern platforms and graphics APIs support quite flexible texture copy (e.g. copy from a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) into a [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) face). However some older systems might not support certain parts of texture copy functionality. This enum indicates support for this. Use [SystemInfo.copyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-copyTextureSupport.html) to check for support before calling [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html).  
  
Direct3D 11, Direct3D 12, and Metal platforms generally support flexible texture copy (all CopyTextureSupport flags are set).  
  
OpenGL supports flexible texture copy since OpenGL 4.3; OpenGL ES supports flexible texture copy since OpenGL ES 3.1 with Android Extension Pack; on earlier versions there's no copy support right now ([CopyTextureSupport.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.None.html)).  
  
Direct3D9 systems have somewhat limited texture copy support (can't copy 3D textures, and can't copy between textures and render textures).  
  
WebGL currently do not have texture copy support ([CopyTextureSupport.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.None.html)).  
  
Additional resources: [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html), [SystemInfo.copyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-copyTextureSupport.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.None.html) | No support for Graphics.CopyTexture.  
[Basic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.Basic.html) | Basic Graphics.CopyTexture support.  
[Copy3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.Copy3D.html) | Support for Texture3D in Graphics.CopyTexture.  
[DifferentTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.DifferentTypes.html) | Support for Graphics.CopyTexture between different texture types.  
[TextureToRT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.TextureToRT.html) | Support for Texture to RenderTexture copies in Graphics.CopyTexture.  
[RTToTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.RTToTexture.html) | Support for RenderTexture to Texture copies in Graphics.CopyTexture.  
* * *
