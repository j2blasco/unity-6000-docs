* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea-center.html

#  [OcclusionArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html).center
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionArea.html "Go to OcclusionArea Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center; 
### Description
Center of the occlusion area relative to the transform.
```
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(OcclusionArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html)))]
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Sets the center of the occlusion area to the center of the transform
    void Start()
    {
        transform.GetComponent<OcclusionArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html)>().center = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
    }
}

```

* * *
