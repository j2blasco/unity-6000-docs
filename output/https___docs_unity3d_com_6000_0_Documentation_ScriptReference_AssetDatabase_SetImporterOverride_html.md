* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetImporterOverride.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).SetImporterOverride
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
public static void SetImporterOverride(string path); 
### Parameters
Parameter | Description  
---|---  
path | Asset path.  
### Description
Sets a specific importer to use for the asset.
Multiple Importers may be registered to a single asset by using either the override extension list, or composite extensions.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;
using UnityEngine.Assertions;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Example Importer Actions")]
    static void AllImporterActions()
    {
        //This sets CubeImporter to be used for the asset
        AssetDatabase.SetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetImporterOverride.html)<CubeImporterOverride>("Assets/CompanionCube.cube");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("New importer: " + AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));  
  
        //This clears importer override and sets it to null
        AssetDatabase.ClearImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html)("Assets/CompanionCube.cube");
        // This asset does not have an Importer Override anymore. The Default Importer is used ( CubeImporter ).
        Assert.IsNull[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNull.html)(AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));
    }
}  
  
//This importer is the Default Importer for the .cube extension.
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "cube")]
public class CubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);
        cube.transform.position = position;
    }
}  
  
//This importer is the Default Importer for the .composite.cube extension.
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "composite.cube")]
public class CompositeCubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 1, 1);
        cube.transform.position = position;
    }
}  
  
//This importer is an Override Importer for the .cube extension.
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, null,new []{ "cube" })]
public class CubeImporterOverride : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        // 'cube' is a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and will be automatically converted into a prefab
        ctx.AddObjectToAsset("main obj", cube);
        ctx.SetMainObject(cube);
    }
}
```

* * *
