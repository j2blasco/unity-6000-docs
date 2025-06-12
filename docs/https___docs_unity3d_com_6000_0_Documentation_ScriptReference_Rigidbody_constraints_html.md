* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-constraints.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).constraints
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
[RigidbodyConstraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html) constraints; 
### Description
Controls which degrees of freedom are allowed for the simulation of this Rigidbody.
By default this is set to [RigidbodyConstraints.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.None.html), allowing rotation and movement along all axes. In some cases, you may want to constrain a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to only move or rotate along some axes, for example when developing 2D games. You can use the bitwise OR operator to combine multiple constraints.  
  
Note that position constraints are applied in World space, and rotation constraints are applied in the inertia space (relative to [Rigidbody.inertiaTensorRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-inertiaTensorRotation.html)).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Attach a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) by clicking the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Hierarchy.html) and
//clicking the **Add Component** button. Search for Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) in the field and select
//it when shown.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;  
  
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        //This locks the RigidBody so that it does not move or rotate in the Z axis.
        m_Rigidbody.constraints = RigidbodyConstraints.FreezePositionZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePositionZ.html) | RigidbodyConstraints.FreezeRotationZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotationZ.html);
    }
}

```

* * *
