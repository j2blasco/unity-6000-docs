* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.SetPositionsSelf.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).SetPositionsSelf
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
public bool SetPositionsSelf(Vector3[] positions, bool checkForDuplicatePositions); 
### Parameters
Parameter | Description  
---|---  
checkForDuplicatePositions | Whether to check for duplicate light probe positions at the cost of performance.  
positions | The positions to set.  
### Returns
**bool** `true` when the positions were successfully set. Otherwise `false`. 
### Description
Sets the positions of the baked light probes stored in this `LightProbes` object.
When you change the positions of baked light probes using this method, you must call [LightProbes.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html) or [LightProbes.TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html) to fully apply the changes.  
  
Setting duplicate light probe positions will lead to incorrect behavior, such as black light probes appearing..  
  
The following script additively loads a scene containing baked light probes and moves the probes:
```
using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class MoveLightProbesExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(LoadSceneAndMoveLightProbes());
    }  
  
    IEnumerator LoadSceneAndMoveLightProbes()
    {
        // Fully load a scene containing light probes additively.
        Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) additiveScene = SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("AdditiveScene", new LoadSceneParameters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneParameters.html)(LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html)));
        yield return null;  
  
        // Get the light probes for the scene.
        LightProbes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html) lightProbes = LightProbes.GetInstantiatedLightProbesForScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInstantiatedLightProbesForScene.html)(additiveScene);  
  
        // Move the light probes slightly.
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions = lightProbes.GetPositionsSelf();
        for (int i = 0; i < positions.Length; i++)
        {
            positions[i] += Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html);
        }
        lightProbes.SetPositionsSelf(positions, true);  
  
        // Tetrahedralize to apply the changes to light probe positions.
        LightProbes.TetrahedralizeAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html)();
    }
}

```

Additional resources: [LightProbes.countSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-countSelf.html).
* * *
