* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.AngleAxis.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).AngleAxis
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) AngleAxis(float angle, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) axis); 
### Description
Creates a rotation which rotates `angle` degrees around `axis`.
For more information see [Rotation and Orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html). The magnitude of the axis parameter is not applied.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Sets the transform's current rotation to a new rotation that rotates 30 degrees around the y-axis(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html))
        transform.rotation = Quaternion.AngleAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.AngleAxis.html)(30, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
    }
}

```

* * *
