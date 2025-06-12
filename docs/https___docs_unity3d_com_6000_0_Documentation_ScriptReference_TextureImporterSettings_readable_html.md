* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-readable.html

#  [TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html).readable
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
readable; 
### Description
Is texture data readable from scripts.
Texture has to be set as "readable" in order for [Texture2D.GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixel.html), [Texture2D.GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels.html) and similar functions to work. Textures are **not** set as readable by default.  
  
When texture is not readable, it consumes much less memory, because a system-memory copy does not have to be kept around after texture is uploaded to the graphics API.
* * *
