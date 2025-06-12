* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).rotation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation; 
### Description
A [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) that stores the rotation of the Transform in world space.
[Transform.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) stores a [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html). You can use [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) to rotate a GameObject or provide the current rotation. Do not attempt to edit/modify [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html). [Transform.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) is less than 180 degrees.  
  
[Transform.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) has no gimbal lock.  
  
To rotate a [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), use [Transform.Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Rotate.html), which uses Euler Angles.  
  
If you want to match values you see in the Inspector, use the [Quaternion.eulerAngles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-eulerAngles.html) property on the returned [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).
```
using UnityEngine;  
  
// Transform.rotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) example.  
  
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) using a Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).
// Tilt the cube using the arrow keys. When the arrow keys are released
// the cube will be rotated back to the center using Slerp.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float smooth = 5.0f;
    float tiltAngle = 60.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Smoothly tilts a transform towards a target rotation.
        float tiltAroundZ = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") * tiltAngle;
        float tiltAroundX = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical") * tiltAngle;  
  
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the cube by converting the angles into a quaternion.
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) target = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(tiltAroundX, 0, tiltAroundZ);  
  
        // Dampen towards the target rotation
        transform.rotation = Quaternion.Slerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Slerp.html)(transform.rotation, target,  Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * smooth);
    }
}

```

In the above example, the [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) is described by a quaternion. For more advice, see [Rotation and Orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html).
* * *
