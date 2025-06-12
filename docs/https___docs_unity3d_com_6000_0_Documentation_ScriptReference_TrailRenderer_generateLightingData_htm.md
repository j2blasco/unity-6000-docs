* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer-generateLightingData.html

#  [TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html).generateLightingData
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html "Go to TrailRenderer Component in the Manual")
generateLightingData; 
### Description
Configures a trail to generate Normals and Tangents. With this data, Scene lighting can affect the trail via Normal Maps and the Unity Standard Shader, or your own custom-built Shaders.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html) tr;  
  
    void Start()
    {
        tr = GetComponent<TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html)>();
        tr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        tr.generateLightingData = true;
    }
}

```

* * *
