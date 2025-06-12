* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html

#  [AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html).AddRemap
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
## Declaration
public void AddRemap([AssetImporter.SourceAssetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SourceAssetIdentifier.html) identifier, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) externalObject); 
### Parameters
Parameter | Description  
---|---  
identifier | The identifier of the sub-asset.  
externalObject | The object to be mapped to the internal object. Can belong to another Prefab or Asset, but not the Asset that is being changed.  
### Description
Map a sub-asset from an imported asset (such as an FBX file) to an external Asset of the same type.
Apply changes by writing the metadata and reimporting the Asset. Instances of the Asset automatically use the mapped object once you have reimported the Asset.  
  
If the type of the external asset does not match the type of the sub-asset, or if the reference is null, instances of the Asset will continue to use the internal asset without producing an error.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Extractor
{
    public static void ExtractFromAsset(Object subAsset, string destinationPath)
    {
        string assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(subAsset);  
  
        var clone = Object.Instantiate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html)(subAsset);
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(clone, destinationPath);  
  
        var assetImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath);
        assetImporter.AddRemap(new AssetImporter.SourceAssetIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SourceAssetIdentifier.html)(subAsset), clone);  
  
        AssetDatabase.WriteImportSettingsIfDirty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.WriteImportSettingsIfDirty.html)(assetPath);
        AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(assetPath, ImportAssetOptions.ForceUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.ForceUpdate.html));
    }
}

```

Additional resources: [AssetImporter.RemoveRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html).
* * *
