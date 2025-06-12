* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).LookRotation
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) LookRotation([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forward, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) upwards = Vector3.up); 
### Parameters
Parameter | Description  
---|---  
forward | The direction to look in.  
upwards | The vector that defines in which direction up is.  
### Description
Creates a rotation with the specified `forward` and `upwards` directions.
Z axis will be aligned with `forward`, X axis aligned with cross product between `forward` and `upwards`, and Y axis aligned with cross product between Z and X.  
  
Returns identity if the magnitude of `forward` is zero.   
If `forward` and `upwards` are colinear, or if the magnitude of `upwards` is zero, the result is the same as [Quaternion.FromToRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html) with `fromDirection` set to the positive Z-axis (0, 0, 1) and `toDirection` set to the normalized `forward` direction.
```
// You can also use transform.LookAt  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relativePos = target.position - transform.position;  
  
        // the second argument, upwards, defaults to Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html)
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(relativePos, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
        transform.rotation = rotation;
    }
}

```

Additional resources: [SetLookRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.SetLookRotation.html).
* * *
