* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.SearchAndRemapMaterials.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).SearchAndRemapMaterials
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
public bool SearchAndRemapMaterials([ModelImporterMaterialName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialName.html) nameOption, [ModelImporterMaterialSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialSearch.html) searchOption); 
### Parameters
Parameter | Description  
---|---  
nameOption | The name matching option.  
searchOption | The search type option.  
### Returns
**bool** Returns false if the source file is empty or invalid. Returns true otherwise. 
### Description
Search the project for matching materials and use them instead of the internal materials.
Unity uses the naming convention specified by nameOption to find and match Material assets in your project and maps them to the model. Use the search option to specify if you want the search to be done project wide, locally or recursive up from the model's location.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MaterialRemapper : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessModel()
    {
        ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) modelImporter = assetImporter as ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html);
        modelImporter.SearchAndRemapMaterials(ModelImporterMaterialName.BasedOnMaterialName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialName.BasedOnMaterialName.html), ModelImporterMaterialSearch.Everywhere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialSearch.Everywhere.html));
    }
}

```

* * *
