* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessAsset.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPreprocessAsset()
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
Add this function to a subclass to get a notification just before any Asset is imported.
This lets you control the import settings through code.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyModelPostprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessAsset()
    {
        if (assetImporter.importSettingsMissing)
        {
            ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) modelImporter = assetImporter as ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html);
            if (modelImporter != null)
            {
                if (!assetPath.Contains("@"))
                    modelImporter.importAnimation = false;
                modelImporter.materialImportMode = ModelImporterMaterialImportMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialImportMode.None.html);
            }
        }
    }
}

```

* * *
