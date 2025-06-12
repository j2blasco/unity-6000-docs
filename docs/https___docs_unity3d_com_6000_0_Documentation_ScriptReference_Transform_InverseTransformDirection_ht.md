* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).InverseTransformDirection
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) InverseTransformDirection([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction); 
### Description
Transforms a `direction` from world space to local space. The opposite of [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html).
This operation is not affected by scale or position of the transform. The transformed vector has the same length as the original.  
  
If you need the inverse operation to transform from local space to world space you can use [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html)  
  
You should use [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html) if the vector represents a position in space rather than a direction.  
  
If you need to transform many directions at once consider using [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html) instead as it is much faster than repeatedly calling this function.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // transform the world forward into local space:
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relative;
        relative = transform.InverseTransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(relative);
    }
}

```

Additional resources:[Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html), [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html).
* * *
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) InverseTransformDirection(float x, float y, float z); 
### Description
Transforms the direction `x`, `y`, `z` from world space to local space. The opposite of [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html).
This operation is not affected by scale or position of the transform. The transformed vector has the same length as the original.  
  
If you need the inverse operation to transform from local space to world space you can use [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html)  
  
You should use [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html) if the vector represents a position in space rather than a direction.  
  
If you need to transform many directions at once consider using [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html) instead as it is much faster than repeatedly calling this function.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // transform the world forward into local space:
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relative;
        relative = transform.InverseTransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(relative);
    }
}

```

Additional resources:[Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html), [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html).
* * *
