* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetImporterOverride
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
public static Type GetImporterOverride(string path); 
### Parameters
Parameter | Description  
---|---  
path | Asset path.  
### Returns
**Type** Importer type. 
### Description
Returns the type of the override importer.
Returns null if there isn't one.
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
        AssetDatabase.SetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetImporterOverride.html)<CubeImporter>("Assets/CompanionCube.cube");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("New importer: " + AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));  
  
        //This clears importer override and sets it to null
        AssetDatabase.ClearImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html)("Assets/CompanionCube.cube");
        Assert.IsNull[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNull.html)(AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));
    }
}  
  
//This is Example Importer
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "cube")]
public class CubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public float m_Scale = 1;
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);
        cube.transform.position = position;
        cube.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(m_Scale, m_Scale, m_Scale);
        // 'cube' is a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and will be automatically converted into a prefab
        ctx.AddObjectToAsset("main obj", cube);
        ctx.SetMainObject(cube);
        var material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        material.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        ctx.AddObjectToAsset("my Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)", material);
        var tempMesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
    }
}
```

* * *
