* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapMaximumLOD.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).heightmapMaximumLOD
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
heightmapMaximumLOD; 
### Description
Limits the Terrain's maximum rendering resolution.
Use on low-end graphics cards to block the highest level of detail for Terrain. A value of 0 for this property allows the terrain to be shown at the highest detail. A value of 1 reduces the maximum triangle count to one-fourth of its current value and halves the width and height of the heightmap resolution. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Terrain.activeTerrain.heightmapMaximumLOD = 1;
    }
}

```

* * *
