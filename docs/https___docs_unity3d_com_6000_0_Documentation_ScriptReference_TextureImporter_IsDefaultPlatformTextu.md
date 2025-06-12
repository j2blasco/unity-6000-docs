* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.IsDefaultPlatformTextureFormatValid.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).IsDefaultPlatformTextureFormatValid
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
public static bool IsDefaultPlatformTextureFormatValid([TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html) textureType, [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) currentFormat); 
### Parameters
Parameter | Description  
---|---  
currentFormat | The TextureImporterType that the importer uses.  
textureType | The TextureImporterFormat to validate.  
### Returns
**bool** Returns true if [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) is valid and can be set. Returns false otherwise. 
### Description
Validates [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) based on the type of the current format ([TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html)) and the default platform.
This method depends on the platforms that are available in the current Unity installation. Because some platforms do not support all formats, these formats cannot be used with the Default Settings. Use this method to check that a format is valid and can be set.
* * *
