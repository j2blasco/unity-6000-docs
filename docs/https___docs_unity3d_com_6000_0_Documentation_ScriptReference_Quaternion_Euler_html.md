* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).Euler
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) Euler(float x, float y, float z); 
### Description
Returns a rotation that rotates z degrees around the z axis, x degrees around the x axis, and y degrees around the y axis; applied in that order.
For more information, see [Rotation and Orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // A rotation 30 degrees around the y-axis
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(0, 30, 0);
    }
}

```

* * *
## Declaration
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) Euler([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) euler); 
### Description
Returns a rotation that rotates z degrees around the z axis, x degrees around the x axis, and y degrees around the y axis.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // A rotation 30 degrees around the y-axis
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rotationVector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 30, 0);
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(rotationVector);
    }
}

```

* * *
