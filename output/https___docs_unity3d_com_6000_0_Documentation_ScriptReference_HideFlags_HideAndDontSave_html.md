* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html

#  [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html).HideAndDontSave
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
The GameObject is not shown in the Hierarchy, not saved to the Scene, and not unloaded by [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).
This is most commonly used for GameObjects which are created by a script and are purely under the script's control.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates a Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) that is explicitly created & destroyed by the component.
    // Resources.UnloadUnusedAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) will not unload it, and it will not be editable by the Inspector.
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
* * *
