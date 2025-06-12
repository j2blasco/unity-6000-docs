* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterRGBMMode.html

# TextureImporterRGBMMode
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
RGBM encoding mode for HDR textures in [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).
HDR texture data (i.e. coming from .exr or .hdr files) can be encoded into RGBM format by Unity. This setting controls how the encoding is done. Default is "Auto", which means do RGBM encoding when source data is HDR.  
  
RGBM encoding packs [0;8] range into [0;1] with multiplier stored in the alpha channel. Final value is RGB*A*8.  
  
Additional resources: TextureImporterSettings.rgbm.
### Properties
Property | Description  
---|---  
[Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterRGBMMode.Auto.html) | Do RGBM encoding when source data is HDR in TextureImporter.  
[On](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterRGBMMode.On.html) | Do RGBM encoding in TextureImporter.  
[Off](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterRGBMMode.Off.html) | Do not perform RGBM encoding in TextureImporter.  
[Encoded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterRGBMMode.Encoded.html) | Source texture is already RGBM encoded in TextureImporter.  
* * *
