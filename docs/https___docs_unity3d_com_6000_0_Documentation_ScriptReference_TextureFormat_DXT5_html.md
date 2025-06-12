* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT5.html

#  [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html).DXT5
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
Compressed color with alpha channel texture format.
DXT5 (BC3) format compresses textures to 8 bits per pixel, and is widely supported on PC and console platforms.  
  
It is a good format to compress most of RGBA textures. For RGB (without alpha) textures, [DXT1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT1.html) is better. When targeting DX11-class hardware, use [BC7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.BC7.html) as compression quality is often better.  
  
Additional resources: [Texture2D.format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-format.html), [texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html).
* * *
