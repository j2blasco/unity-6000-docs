* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapPixelError.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).heightmapPixelError
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
heightmapPixelError; 
### Description
An approximation of how many pixels the terrain will pop in the worst case when switching lod.
A higher value reduces the number of polygons drawn.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Terrain.activeTerrain.heightmapPixelError = 10;
    }
}

```

* * *
