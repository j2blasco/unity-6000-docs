* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html

# TextureWrapMode
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
Wrap mode for textures.
Corresponds to the settings in a [texture inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html). Wrap mode determines how texture is sampled when texture coordinates are outside of the typical 0..1 range. For example, [Repeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Repeat.html) makes the texture tile, whereas [Clamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Clamp.html) makes the texture edge pixels be stretched when outside of of 0..1 range.  
  
Additional resources: [Texture.wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapMode.html), [texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
### Properties
Property | Description  
---|---  
[Repeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Repeat.html) | Tiles the texture, creating a repeating pattern.  
[Clamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Clamp.html) | Clamps the texture to the last pixel at the edge.  
[Mirror](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Mirror.html) | Tiles the texture, creating a repeating pattern by mirroring it at every integer boundary.  
[MirrorOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.MirrorOnce.html) | Mirrors the texture once, then clamps to edge pixels.  
* * *
