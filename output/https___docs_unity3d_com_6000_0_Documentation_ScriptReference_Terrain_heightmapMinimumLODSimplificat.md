* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapMinimumLODSimplification.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).heightmapMinimumLODSimplification
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
heightmapMinimumLODSimplification; 
### Description
Limits how simplified the rendered terrain can be.
Sets the lowest level of simplification for the Terrain. Also affects areas that are outside of the camera frustum. Use this property to correct a situation where Terrain that is outside of the camera's view casts an overly simplified shadow inside the camera's view. A value of 0 means there's no limit on reducing the Terrain's level of detail. Each increment of the value quadruples the minimum number of triangles used to render the Terrain. A high value can reduce performance because of high culling time.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Terrain.activeTerrain.heightmapMinimumLODSimplification = 2;
    }
}

```

* * *
