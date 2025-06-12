* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html

# HideFlags
enumeration
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
Bit mask that controls object destruction, saving and visibility in inspectors.
Additional resources: [Object.hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates a material that is explicitly created & destroyed by the component.
    // Resources.UnloadUnusedAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) will not unload it, and it will not be editable by the inspector.
    private Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) ownedMaterial;
    void OnEnable()
    {
        ownedMaterial = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Diffuse"));
        ownedMaterial.hideFlags = HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html);
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().sharedMaterial = ownedMaterial;
    }  
  
    // Objects created as hide and don't save must be explicitly destroyed by the owner of the object.
    void OnDisable()
    {
        DestroyImmediate(ownedMaterial);
    }
}

```

If you set `HideFlags` to `DontSaveInEditor`, `DontSaveInBuild`, or `HideInHierarchy`, the object is removed internally from the Scene and from from its current physics scene. This includes both 2D and 3D physics scenes. The object also triggers its `OnDisable` and `OnEnable` calls.   
  
You can use these flags to control whether instantiated assets, such as ScriptableObjects and Materials, that have not yet been saved to the project using [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) (that is, they are not persistent) are serialized to the scene or not. 
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.None.html) | A normal, visible object. This is the default.  
[HideInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html) | The object will not appear in the hierarchy.  
[HideInInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInInspector.html) | It is not possible to view it in the inspector.  
[DontSaveInEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSaveInEditor.html) | The object will not be saved to the Scene in the editor.  
[NotEditable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.NotEditable.html) | The object is not editable in the Inspector.  
[DontSaveInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSaveInBuild.html) | The object will not be saved when building a player.  
[DontUnloadUnusedAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontUnloadUnusedAsset.html) | The object will not be unloaded by Resources.UnloadUnusedAssets.  
[DontSave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html) | The object will not be saved to the Scene. It will not be destroyed when a new Scene is loaded. It is a shortcut for HideFlags.DontSaveInBuild | HideFlags.DontSaveInEditor | HideFlags.DontUnloadUnusedAsset.  
[HideAndDontSave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html) | The GameObject is not shown in the Hierarchy, not saved to the Scene, and not unloaded by Resources.UnloadUnusedAssets.  
* * *
