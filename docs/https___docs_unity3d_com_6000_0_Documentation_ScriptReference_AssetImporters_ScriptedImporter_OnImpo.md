* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.OnImportAsset.html

#  [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html).OnImportAsset
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
public void OnImportAsset([AssetImporters.AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx); 
### Parameters
Parameter | Description  
---|---  
ctx | This argument contains all the contextual information needed to process the import event and is also used by the custom importer to store the resulting Unity Asset.  
### Description
This method must by overriden by the derived class and is called by the Asset pipeline to import files.
```
using UnityEngine;
using UnityEditor.AssetImporters;
using System.IO;  
  
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "cube")]
public class CubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public float m_Scale = 1;  
  
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        var position = JsonUtility.FromJson[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html)<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(File.ReadAllText(ctx.assetPath));  
  
        cube.transform.position = position;
        cube.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(m_Scale, m_Scale, m_Scale);  
  
        // 'cube' is a a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and will be automatically converted into a Prefab
        // (Only the 'Main Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)' is elligible to become a Prefab.)
        ctx.AddObjectToAsset("main obj", cube);
        ctx.SetMainObject(cube);  
  
        var material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        ctx.DependsOnCustomDependency("StandardShaderDependencyHash");  
  
        material.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);  
  
        // Assets must be assigned a unique identifier string consistent across imports
        ctx.AddObjectToAsset("my Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)", material);  
  
        // Assets that are not passed into the context as import outputs must be destroyed
        var tempMesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        DestroyImmediate(tempMesh);
    }
}

```

To use the Shader.Find() function in the above example, you need to write a custom dependency for the shader you want to find and regularly update it. This prevents the Shader.Find() function from bypassing other means of dependency checking. The below code is an example of how you might write a custom dependency for this purpose.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
static class ShaderDependencyUpdater
{
    [InitializeOnLoadMethod]
    static void ShaderDependencyInit()
    {
        EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) += ShaderDependencyUpdate;
    }
    static void ShaderDependencyUpdate()
    {
        var shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard");
        AssetDatabase.TryGetGUIDAndLocalFileIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(shader, out var guid, out long id);
        var hash = new Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)();
        hash.Append(guid);
        hash.Append(id);
        AssetDatabase.RegisterCustomDependency[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RegisterCustomDependency.html)("StandardShaderDependencyHash", hash);
    }
}
```

* * *
