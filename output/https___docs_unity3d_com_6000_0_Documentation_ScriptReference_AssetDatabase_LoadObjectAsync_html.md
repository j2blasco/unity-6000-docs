* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadObjectAsync.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).LoadObjectAsync
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
public static [AssetDatabaseLoadOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabaseLoadOperation.html) LoadObjectAsync(string assetPath, long localId); 
### Parameters
Parameter | Description  
---|---  
assetPath | Path of the asset to load.  
localId | The local identifier of the object that you want to load. This allows you to load a specific object and its dependencies as opposed to the entire asset.  
### Returns
**AssetDatabaseLoadOperation** A UnityEditor.AssetDatabaseLoadOperation which you can use to track the progress of the operation. 
### Description
Loads a specific Object and its dependencies from an Asset file asynchronously.
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".  
  
Additional resources: [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html), [GlobalObjectId.targetObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetObjectId.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections;  
  
public class MyPlayer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public IEnumerator Start()
    {
        // This will load all objects in the fbx and return a single Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) object.
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) m = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Assets/test.fbx");  
  
        AssetDatabase.TryGetGUIDAndLocalFileIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(m, out string guid, out long localId);  
  
        // At some point after the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) may or may not have unloaded we can reload just the mesh
        AssetDatabaseLoadOperation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabaseLoadOperation.html) op = AssetDatabase.LoadObjectAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadObjectAsync.html)("Assets/test.fbx", localId);  
  
        // yield until the operation is completed
        while (!op.isDone)
            yield return null;  
  
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) reloadedMesh = (Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html))op.LoadedObject;
    }
}
```

* * *
