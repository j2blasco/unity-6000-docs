* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessModel.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPreprocessModel()
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
Add this function to a subclass to get a notification just before a model (.fbx, .mb file etc.) is imported.
This lets you control the import settings through code.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Disable import of materials if the file contains
// the @ sign marking it as an animation.
public class Example : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessModel()
    {
        if (assetPath.Contains("@"))
        {
            ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) modelImporter = assetImporter as ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html);
            modelImporter.materialImportMode = ModelImporterMaterialImportMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialImportMode.None.html);
        }
    }
}

```

* * *
