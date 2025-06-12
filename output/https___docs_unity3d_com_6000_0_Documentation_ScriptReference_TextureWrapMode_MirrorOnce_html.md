* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.MirrorOnce.html

#  [TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html).MirrorOnce
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
Mirrors the texture once, then clamps to edge pixels.
This effectively mirrors the texture around zero UV coordinates, and repeats edge pixel values when outside of [-1..1] range.  
  
This mode is called "mirror and clamp to edge" in graphics APIs like Vulkan, Metal and OpenGL. This feature is not always supported when using OpenGL ES and Vulkan graphics APIs, specifically on ARM and Qualcomm GPUs platforms. Check [SystemInfo.supportsTextureWrapMirrorOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsTextureWrapMirrorOnce.html) to figure out whether the system is capable..  
  
Additional resources: [Texture.wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapMode.html), [texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html), [SystemInfo.supportsTextureWrapMirrorOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsTextureWrapMirrorOnce.html).
* * *
