* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.ApplyTextureType.html

#  [TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html).ApplyTextureType
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
**Obsolete** ApplyTextureType(TextureImporterType, bool) is deprecated, use ApplyTextureType(TextureImporterType).
## Declaration
public void ApplyTextureType([TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html) type, bool applyAll); 
### Parameters
Parameter | Description  
---|---  
type | Texture type. See [TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html).  
applyAll | If `false`, change only specific properties. Exactly which, depends on _type_.  
### Description
Configure parameters to import a texture for a purpose of _type_ , as described [here](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html).
* * *
