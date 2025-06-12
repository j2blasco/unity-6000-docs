* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ExtractAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ExtractAsset
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
public static string ExtractAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) asset, string newPath); 
### Parameters
Parameter | Description  
---|---  
asset | The sub-asset to extract.  
newPath | The file path of the new Asset.  
### Returns
**string** An empty string if Unity has successfully extracted the Asset, or an error message if not. 
### Description
Creates an external Asset from an object (such as a Material) by extracting it from within an imported asset (such as an FBX file).
**NOTE:** The feature is currently only available for materials embedded in model assets.  
  
All file paths are relative to the project folder. For example: "Assets/Materials/myMaterial.mat".  
  
Method throws **ArgumentNullException** when the Asset is _null_ and **ArgumentException** when the file path is _null or empty_.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Extractor
{
    public static void ExtractFromAsset(Object subAsset, string destinationPath)
    {
        string assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(subAsset);  
  
        AssetDatabase.ExtractAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ExtractAsset.html)(subAsset, destinationPath);  
  
        AssetDatabase.WriteImportSettingsIfDirty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.WriteImportSettingsIfDirty.html)(assetPath);
        AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(assetPath, ImportAssetOptions.ForceUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.ForceUpdate.html));
    }
}

```

* * *
