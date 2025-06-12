* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Clamp.html

#  [TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html).Clamp
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
Clamps the texture to the last pixel at the edge.
This is useful for preventing wrapping artifacts when mapping an image onto an object and you don't want the texture to tile. UV coordinates will be clamped to the range 0...1. When UVs are larger than 1 or smaller than 0, the last pixel at the border will be used.  
  
This mode is called "clamp to edge" in graphics APIs like Vulkan, Metal and OpenGL.  
  
Additional resources: [Texture.wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapMode.html), [texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
* * *
