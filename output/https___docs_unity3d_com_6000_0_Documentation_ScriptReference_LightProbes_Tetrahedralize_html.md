* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).Tetrahedralize
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
public static void Tetrahedralize(); 
### Description
Synchronously tetrahedralize the currently loaded LightProbe positions.
Call this function to tetrahedralize the currently loaded LightProbe positions. You should generally only call this function upon receiving a [LightProbes.needsRetetrahedralization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-needsRetetrahedralization.html) event.
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class TetrahedralizeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Additively load a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) containing light probes
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("ExampleScene", LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html));  
  
        // Force Unity to synchronously regenerate the tetrahedral tesselation for all loaded Scenes
        LightProbes.Tetrahedralize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html)();
    }
}

```

Additional resources: [LightProbes.TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html), [Light Probes in the Unity Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html), [Lightmapping.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Tetrahedralize.html).
* * *
