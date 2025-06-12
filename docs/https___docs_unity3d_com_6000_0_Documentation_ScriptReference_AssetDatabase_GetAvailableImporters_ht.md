* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAvailableImporters.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetAvailableImporters
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
public static Type[] GetAvailableImporters(string path); 
### Parameters
Parameter | Description  
---|---  
path | The Asset path.  
### Returns
**Type[]** Returns an array of importer types that can handle the specified Asset. 
### Description
Gets the importer types associated with a given Asset path.
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
        Type[] CubeTypes = AssetDatabase.GetAvailableImporters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAvailableImporters.html)("Assets/CompanionCube.cube");
        for (int i = 0; i < CubeTypes.Length; i++)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Available Importer Type for cube: " + CubeTypes[i]);
        }
    }  
  
    //This is Example Importer for cube
    [ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "cube")]
    public class CubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
        {
            var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
            var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);
            cube.transform.position = position;
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);
        }
    }
}
```

* * *
