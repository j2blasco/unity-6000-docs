* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-sRGBTexture.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).sRGBTexture
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
sRGBTexture; 
### Description
Whether this texture stores data in sRGB (also called gamma) color space.
This setting is only relevant when your project uses [Linear color space](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html). It determines whether the GPU converts data from sRGB color space to linear color space when it samples the texture in a shader.  
  
Non-HDR textures that contain color data typically store their data as sRGB values. This data requires conversion, so this value should be `true`.  
  
HDR textures and textures that store data other than color (for example, normal maps) typically store their data as linear values. This data does not require conversion, so this value should be `false`. This value should also be `false` for legacy IMGUI textures.  
  
Unity marks various textures that typically store linear data (normal maps, other non-color textures, and HDR data) as "linear" by default.  
  
This flag corresponds to "sRGB (Color Texture)" option in [class-TextureImporter](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).  
  
Additional resources: [Color space](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html), [PlayerSettings.colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-colorSpace.html).
* * *
