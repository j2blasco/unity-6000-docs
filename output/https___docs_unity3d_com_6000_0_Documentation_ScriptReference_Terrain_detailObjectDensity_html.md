* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-detailObjectDensity.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).detailObjectDensity
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
detailObjectDensity; 
### Description
Density of detail objects.
This number goes from 0.0 to 1.0, with 1.0 being the original density, and lower numbers resulting in less detail objects being rendered.  
  
Additional resources: [detailObjectDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-detailObjectDistance.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Terrain.activeTerrain.detailObjectDensity = 0.5f;
    }
}

```

* * *
