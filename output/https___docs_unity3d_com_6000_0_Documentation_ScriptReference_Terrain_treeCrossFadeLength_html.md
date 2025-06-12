* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeCrossFadeLength.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).treeCrossFadeLength
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
treeCrossFadeLength; 
### Description
Total distance delta that trees will use to transition from billboard orientation to mesh orientation.
Decreasing this value makes the transition happen faster. Setting it to 0 will produce a visible pop when switching from mesh to billboard representation.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Terrain.activeTerrain.treeCrossFadeLength = 20;
    }
}

```

* * *
