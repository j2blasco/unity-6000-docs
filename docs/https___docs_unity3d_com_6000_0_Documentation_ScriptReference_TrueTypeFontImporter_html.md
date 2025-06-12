* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.html

# TrueTypeFontImporter
class in UnityEditor
/
Inherits from:[AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html)
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
AssetImporter for importing Fonts.
### Properties
Property | Description  
---|---  
[ascentCalculationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-ascentCalculationMode.html) | Calculation mode for determining font's ascent.  
[characterPadding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-characterPadding.html) | Border pixels added to character images for padding. This is useful if you want to render text using a shader which needs to render outside of the character area (like an outline shader).  
[characterSpacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-characterSpacing.html) | Spacing between character images in the generated texture in pixels. This is useful if you want to render text using a shader which samples pixels outside of the character area (like an outline shader).  
[customCharacters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-customCharacters.html) | A custom set of characters to be included in the Font Texture.  
[fontNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontNames.html) | An array of font names, to be used when includeFontData is set to false.  
[fontReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontReferences.html) | References to other fonts to be used looking for fallbacks.  
[fontRenderingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontRenderingMode.html) | Font rendering mode to use for this font.  
[fontSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontSize.html) | Font size to use for importing the characters.  
[fontTextureCase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontTextureCase.html) | Use this to adjust which characters should be imported.  
[fontTTFName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontTTFName.html) | The internal font name of the TTF file.  
[includeFontData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-includeFontData.html) | If this is enabled, the actual font will be embedded into the asset for Dynamic fonts.  
[shouldRoundAdvanceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-shouldRoundAdvanceValue.html) | Set this property to true if you want to round the internal advance width of the font to the nearest integer.  
### Public Methods
Method | Description  
---|---  
[GenerateEditableFont](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.GenerateEditableFont.html) | Create an editable copy of the font asset at path.  
### Inherited Members
### Properties
Property | Description  
---|---  
[assetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleName.html) | Get or set the AssetBundle name.  
[assetBundleVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleVariant.html) | Get or set the AssetBundle variant.  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetPath.html) | The path name of the asset for this importer. (Read Only)  
[importSettingsMissing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-importSettingsMissing.html) | The value is true when no meta file is provided with the imported asset.  
[userData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-userData.html) | Get or set any user data.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[AddRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html) | Map a sub-asset from an imported asset (such as an FBX file) to an external Asset of the same type.  
[GetExternalObjectMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetExternalObjectMap.html) | Gets a copy of the external object map used by the AssetImporter.  
[RemoveRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html) | Removes an item from the map of external objects.  
[SaveAndReimport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SaveAndReimport.html) | Save asset importer settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SetAssetBundleNameAndVariant.html) | Set the AssetBundle name and variant.  
[SupportsRemappedAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SupportsRemappedAssetType.html) | Checks if the AssetImporter supports remapping the given asset type.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html) | Retrieves the asset importer for the asset at path.  
[GetImportLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetImportLog.html) | Retrieves logs generated during the import of the asset at path.  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
