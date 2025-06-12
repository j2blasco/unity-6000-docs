* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).InverseTransformPoint
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
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) InverseTransformPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Description
Transforms `position` from world space to local space.
This function is essentially the opposite of [Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html) which is used to convert from local to world space.  
  
Note that the returned position is affected by scale. Use [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html) if you are dealing with direction vectors rather than positions.  
  
If you need to transform many points at once consider using [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html) instead as it is much faster than repeatedly calling this function.
```
// Calculate the transform's position relative to the camera.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) cam;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) cameraRelative;  
  
    void Start()
    {
        cam = Camera.main.transform;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) cameraRelative = cam.InverseTransformPoint(transform.position);  
  
        if (cameraRelative.z > 0)
            print("The object is in front of the camera");
        else
            print("The object is behind the camera");
    }
}

```

Additional resources:[Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html), [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html), [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html), [Transform.InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html).
* * *
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) InverseTransformPoint(float x, float y, float z); 
### Description
Transforms the position `x`, `y`, `z` from world space to local space.
This function is essentially the opposite of [Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html) which is used to convert from local to world space.  
  
Note that the returned position is affected by scale. Use [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html) if you are dealing with direction vectors rather than positions.  
  
If you need to transform many points at once consider using [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html) instead as it is much faster than repeatedly calling this function.
```
// Calculate the world origin relative to this transform.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relativePoint = transform.InverseTransformPoint(0, 0, 0);  
  
        if (relativePoint.z > 0)
            print("The world origin is in front of this object");
        else
            print("The world origin is behind this object");
    }
}

```

Additional resources:[Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html), [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html), [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html), [Transform.InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html).
* * *
