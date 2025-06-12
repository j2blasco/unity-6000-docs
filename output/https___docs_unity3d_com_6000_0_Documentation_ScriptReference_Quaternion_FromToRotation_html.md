* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).FromToRotation
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) FromToRotation([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) fromDirection, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) toDirection); 
### Parameters
Parameter | Description  
---|---  
fromDirection | A non-unit or unit vector representing a direction axis to rotate.  
toDirection | A non-unit or unit vector representing the target direction axis.  
### Returns
**Quaternion** A unit quaternion which rotates from `fromDirection` to `toDirection`. 
### Description
Creates a rotation from `fromDirection` to `toDirection`.
Use this method to rotate a transform so that one of its axes, such as the y-axis, follows the target direction, `toDirection`, in world space.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Sets the rotation so that the transform's y-axis goes along the global y-axis and the transform's z-axis goes along the global z-axis
        transform.rotation *= Quaternion.FromToRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html)(transform.up, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
        transform.rotation *= Quaternion.FromToRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html)(transform.forward, Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));
    }
}

```

* * *
