* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-inertiaTensor.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).inertiaTensor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inertiaTensor; 
### Description
The inertia tensor of this body, defined as a diagonal matrix in a reference frame positioned at this body's center of mass and rotated by [Rigidbody.inertiaTensorRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-inertiaTensorRotation.html).
Inertia tensor is a rotational analog of mass: the larger the inertia component about a particular axis is, the more torque that is required to achieve the same angular acceleration about that axis.  
  
Zero is not a valid inertia tensor component. Therefore, the physics system interprets zeros as infinite values instead. So, for example, a body with (0, 1, 1) inertia tensor is impossible to rotate around X.  
  
Note that the rotational Constraints [RigidbodyConstraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html) of Rigidbody are actually implemented by setting the inertia tensor components about the locked degrees of freedom to zero.  
  
If you don't set the inertia tensor from a script, it is calculated automatically from all colliders attached to the Rigidbody. To reset the inertia tensor to the automatically computed value, call [Rigidbody.ResetInertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.ResetInertiaTensor.html).
```
// Expose tensor of inertia to allow adjustment from
// the inspector.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) tensor;
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rb.inertiaTensor = tensor;
    }
}

```

* * *
