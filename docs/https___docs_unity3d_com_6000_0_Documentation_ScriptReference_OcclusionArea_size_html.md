* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea-size.html

#  [OcclusionArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html).size
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size; 
### Description
Size that the occlusion area will have.
```
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(OcclusionArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html)))]
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Sets an Occlusion area of 10 units in x, 20 units in y and 30 units in z
    void Start()
    {
        transform.GetComponent<OcclusionArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html)>().size = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(10, 20, 30);
    }
}

```

* * *
