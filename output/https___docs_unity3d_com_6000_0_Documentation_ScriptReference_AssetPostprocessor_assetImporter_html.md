* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor-assetImporter.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).assetImporter
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
[AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html) assetImporter; 
### Description
Reference to the asset importer.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Set the scale of all the imported models to  "globalScaleModifier"
// and dont generate materials for the imported objects  
  
public class CustomImportSettings : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    float globalScaleModifier  = 0.0028f;  
  
    void OnPreprocessModel()
    {
        ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) importer = (ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html))assetImporter;
        importer.globalScale = globalScaleModifier;
        importer.materialImportMode = ModelImporterMaterialImportMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialImportMode.None.html);
    }
}

```

* * *
