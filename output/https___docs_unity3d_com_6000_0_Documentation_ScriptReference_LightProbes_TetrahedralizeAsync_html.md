* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).TetrahedralizeAsync
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
public static void TetrahedralizeAsync(); 
### Description
Asynchronously tetrahedralize all currently loaded LightProbe positions.
Call this function to asynchronously calculate a Delaunay tetrahedralization of all currently loaded LightProbe positions, and update the [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html) object with the result. Note that Unity does not raise an event when this asynchronous method completes.  
  
Call this method after you load a Scene with [LoadSceneMode.Additive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html), or unload a Scene with [SceneManager.UnloadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html). Note that updating the tetrahedral tessellation is CPU-intensive. For more information, see [Light Probes and Scene loading](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html).
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class TetrahedralizeAsyncExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Additively load a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) containing light probes
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("ExampleScene", LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html));  
  
        // Force Unity to asynchronously regenerate the tetrahedral tesselation for all loaded Scenes
        LightProbes.TetrahedralizeAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html)();
    }
}

```

Additional resources: [LightProbes.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html), [Light Probes in the Unity Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html), [Lightmapping.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Tetrahedralize.html).
* * *
