* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.ToAngleAxis.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).ToAngleAxis
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
## Declaration
public void ToAngleAxis(out float angle, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) axis); 
### Description
Converts a rotation to angle-axis representation (angles in degrees).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Extracts the angle - axis rotation from the transform rotation  
  
        float angle = 0.0f;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) axis = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        transform.rotation.ToAngleAxis(out angle, out axis);
    }
}

```

* * *
