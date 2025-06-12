* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDefaultImporter.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetDefaultImporter
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
public static Type GetDefaultImporter(string path); 
### Parameters
Parameter | Description  
---|---  
path | Asset path.  
### Returns
**Type** Importer type. 
### Description
Returns the Default Importer associated with the asset located at the supplied path. When no Importer override is set, then the default importer is used. Additional resources: [AssetDatabase.GetImporterOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html), [AssetDatabase.ClearImporterOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Available Importer Types for cube")]
    static void AvailableImporterTypeCube()
    {
        var path = "Assets/CompanionCube.fbx";
        AssetDatabase.GetDefaultImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDefaultImporter.html)(path);
        // returns ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).
        AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)(path);
        // returns null because no Override Importer is set.
        AssetDatabase.GetAvailableImporters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAvailableImporters.html)(path);
        // returns [CubeImporter].
        AssetDatabase.SetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetImporterOverride.html)<CubeImporter>(path);
        // sets CubeImporter as Override Importer.
        AssetDatabase.ClearImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html)(path);
        // removes the Override Importer.
        AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)(path);
        // returns null because no Override Importer is set.
    }  
  
    //This is Example Importer for cube
    [ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, new []{"cube" }, new[] { "fbx" })]
    public class CubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
        {
            var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
            cube.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);
            // 'cube' is a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and will be automatically converted into a prefab
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);
        }
    }
}

```

* * *
