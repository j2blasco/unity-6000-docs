* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.IsPlatformTextureFormatValid.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).IsPlatformTextureFormatValid
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
## Declaration
public static bool IsPlatformTextureFormatValid([TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html) textureType, [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target, [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) currentFormat); 
### Parameters
Parameter | Description  
---|---  
textureType | The TextureImporterType that the importer uses.  
target | The platform that the setting targets, referred to as the BuilTarget.  
currentFormat | The TextureImporterFormat to validate.  
### Returns
**bool** Returns true if [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) is valid and can be set. Returns false otherwise. 
### Description
Validates [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) based on a specified import type ([TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html)) and a specified build target ([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html).).
[TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) is not available for all platforms based on the [TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html) of a given Texture. Use this method to check that the format set with SetPlatformTextureSettings is a valid format.
* * *
