* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings.html

# TextureImporterPlatformSettings
class in UnityEditor
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
Stores platform specifics settings of a [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).
Additional resources: TextureImporter.
### Properties
Property | Description  
---|---  
[allowsAlphaSplitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-allowsAlphaSplitting.html) | Allows Alpha splitting on the imported texture when needed (for example ETC1 compression for textures with transparency).  
[androidETC2FallbackOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-androidETC2FallbackOverride.html) | Override for ETC2 decompression fallback on Android devices that don't support ETC2.  
[compressionQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-compressionQuality.html) | The quality of Crunch texture compression. The range is 0 through 100. A higher quality means larger textures and longer compression times.  
[crunchedCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-crunchedCompression.html) | Use crunch compression when available.  
[format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-format.html) | Format of imported texture.  
[ignorePlatformSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-ignorePlatformSupport.html) | Ignores platform support checks for the selected texture format.  
[maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-maxTextureSize.html) | Maximum texture size.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-name.html) | Name of the build target.  
[overridden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-overridden.html) | Set to true in order to override the Default platform parameters by those provided in the TextureImporterPlatformSettings structure.  
[resizeAlgorithm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-resizeAlgorithm.html) | For Texture to be scaled down choose resize algorithm. ( Applyed only when Texture dimension is bigger than Max Size ).  
[textureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings-textureCompression.html) | Compression of imported texture.  
### Public Methods
Method | Description  
---|---  
[CopyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings.CopyTo.html) | Copy parameters into another TextureImporterPlatformSettings object.  
* * *
