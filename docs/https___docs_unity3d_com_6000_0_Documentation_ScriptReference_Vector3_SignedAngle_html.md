* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SignedAngle.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).SignedAngle
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
## Declaration
public static float SignedAngle([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) from, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) to, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) axis); 
### Parameters
Parameter | Description  
---|---  
from | The vector from which the angular difference is measured.  
to | The vector to which the angular difference is measured.  
axis | A vector around which the other vectors are rotated.  
### Returns
**float** Returns the signed angle between `from` and `to` in degrees. 
### Description
Calculates the signed angle between vectors `from` and `to` in relation to `axis`.
The angle returned is the angle of rotation from the first vector to the second, when treating these first two vector inputs as directions. These two vectors also define the plane of rotation, meaning they are parallel to the plane. This means the axis of rotation around which the angle is calculated is the [cross product](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html) of the first and second vectors (and not the 3rd "axis" parameter). You can use the ["left hand rule"](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html) to determine the axis of rotation, given the two input vectors. The third input (named the “axis” parameter), gives you a way to provide a contextual direction to include in the calculation. This has the result of flipping the sign of the result depending on whether this third vector that you supply falls above or below the plane of rotation defined by the first two input vectors. Therefore the sign of the final result depends on two things: the order in which you supply the "from" and "to" vector, and the direction of the third "axis" vector.  
Note: The angle returned will always be between -180 and 180 degrees, because the method returns the smallest angle between the vectors. That is, it will never return a reflex angle.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) targetDir = target.position - transform.position;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forward = transform.forward;
        float angle = Vector3.SignedAngle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SignedAngle.html)(targetDir, forward, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
        if (angle < -5.0F)
            print("turn right");
        else if (angle > 5.0F)
            print("turn left");
        else
            print("forward");
    }
}

```

Additional resources: [Angle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Angle.html) function.
* * *
