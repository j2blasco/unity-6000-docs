* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html

#  [AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html).RemoveRemap
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
public bool RemoveRemap([AssetImporter.SourceAssetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SourceAssetIdentifier.html) identifier); 
### Parameters
Parameter | Description  
---|---  
identifier | The identifier of the sub-asset.  
### Returns
**bool** Returns true if an element was removed, otherwise false. 
### Description
Removes an item from the map of external objects.
Apply changes by writing the metadata and reimporting the Asset.  
  
The external Asset referenced in the map is not affected in any way by this method.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Extractor
{
    public static void RemoveExternalObjectMapping(string assetPath, AssetImporter.SourceAssetIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SourceAssetIdentifier.html) subAssetIdentifier)
    {
        var assetImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath);
        assetImporter.RemoveRemap(subAssetIdentifier);  
  
        AssetDatabase.WriteImportSettingsIfDirty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.WriteImportSettingsIfDirty.html)(assetPath);
        AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(assetPath, ImportAssetOptions.ForceUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.ForceUpdate.html));
    }
}

```

Additional resources: [AssetImporter.AddRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html).
* * *
