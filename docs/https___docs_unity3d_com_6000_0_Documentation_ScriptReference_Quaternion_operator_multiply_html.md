* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-operator_multiply.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).operator *
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
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) operator *([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) lhs, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rhs); 
### Parameters
Parameter | Description  
---|---  
lhs | Left-hand side quaternion.  
rhs | Right-hand side quaternion.  
### Description
Combines rotations `lhs` and `rhs`.
Rotating by the product `lhs` * `rhs` is the same as applying the two rotations in sequence: `lhs` first and then `rhs`, relative to the reference frame resulting from `lhs` rotation. Note that this means rotations are not commutative, so `lhs` * `rhs` does not give the same rotation as `rhs` * `lhs`.
```
using UnityEngine;
using System.Collections;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float rotateSpeed = 90;  
  
    // Applies a rotation of 90 degrees per second around the local Y axis
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float angle = rotateSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
        transform.rotation *= Quaternion.AngleAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.AngleAxis.html)(angle, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
    }
}

```

* * *
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) operator *([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
### Description
Rotates the point `point` with `rotation`.
```
using UnityEngine;
using System.Collections;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        //Creates an array of three points forming a triangle
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] points = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[]
        {
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1, -1, 0),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, -1, 0),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1, 0)
        };  
  
        //Creates a Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation of 5 degrees around the Z axis
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.AngleAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.AngleAxis.html)(5, Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));  
  
        //Loop through the array of Vector3s and apply the rotation
        for (int n = 0; n < points.Length; n++)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rotatedPoint = rotation * points[n];
            //Output the new rotation values
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Point " + n + " rotated: " + rotatedPoint);
        }
    }
}

```

* * *
