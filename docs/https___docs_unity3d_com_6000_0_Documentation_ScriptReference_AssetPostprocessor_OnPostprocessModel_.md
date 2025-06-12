* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessModel.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessModel(GameObject)
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
Add this function to a subclass to get a notification when a model has completed importing.
This lets you modify the imported Game Object, Meshes, AnimationClips referenced by it. Please note that the GameObjects, AnimationClips and Meshes only exist during the import and will be destroyed immediately afterwards.  
  
This function is called before the final Prefab is created and before it is written to disk, thus you have full control over the generated game objects and components.  
  
Any references to game objects or meshes will become invalid after the import has been completed. Thus it is not possible to create a new Prefab in a different file from OnPostprocessModel that references meshes in the imported fbx file.  
  
`root` is the root game object of the imported model.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Adds a mesh collider to each game object that contains collider in its name
public class Example : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPostprocessModel(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) g)
    {
        Apply(g.transform);
    }  
  
    void Apply(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t)
    {
        if (t.name.ToLower().Contains("collider"))
            t.gameObject.AddComponent<MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html)>();  
  
        // Recurse
        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) child in t)
            Apply(child);
    }
}

```

* * *
