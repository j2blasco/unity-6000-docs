* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html

# RigidbodyConstraints
enumeration
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
### Description
Use these flags to constrain motion of Rigidbodies.
Additional resources: [Rigidbody.constraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-constraints.html). This enables you to freeze positions and rotations on all axes.
```
//This example shows how RigidbodyConstraints[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html) is used to freeze the position and rotation of a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) in the z axis at start-up.
//It also shows what happens when these constraints are removed, when you press the space key
//Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to see it in action  
  
using UnityEngine;  
  
public class RigidBodyConstraitsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_ZAxis;  
  
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        //This locks the RigidBody so that it does not move or rotate in the z axis (can be seen in Inspector).
        m_Rigidbody.constraints = RigidbodyConstraints.FreezePositionZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePositionZ.html) | RigidbodyConstraints.FreezeRotationZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotationZ.html);
        //Set up vector for moving the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) in the z axis
        m_ZAxis = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 5);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press space to remove the constraints on the RigidBody
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Remove all constraints
            m_Rigidbody.constraints = RigidbodyConstraints.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.None.html);
        }  
  
        //Press the right arrow key to move positively in the z axis if the constraints are removed
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.RightArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightArrow.html)))
        {
            //If the constraints are removed, the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) moves along the z axis
            //If the constraints are there, no movement occurs
            m_Rigidbody.velocity = m_ZAxis;
        }  
  
        //Press the left arrow key to move negatively in the z axis if the constraints are removed
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.LeftArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftArrow.html)))
        {
            m_Rigidbody.velocity = -m_ZAxis;
        }
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.None.html) | No constraints.  
[FreezePositionX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePositionX.html) | Freeze motion along the X-axis.  
[FreezePositionY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePositionY.html) | Freeze motion along the Y-axis.  
[FreezePositionZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePositionZ.html) | Freeze motion along the Z-axis.  
[FreezeRotationX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotationX.html) | Freeze rotation along the X-axis.  
[FreezeRotationY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotationY.html) | Freeze rotation along the Y-axis.  
[FreezeRotationZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotationZ.html) | Freeze rotation along the Z-axis.  
[FreezePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePosition.html) | Freeze motion along all axes.  
[FreezeRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotation.html) | Freeze rotation along all axes.  
[FreezeAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeAll.html) | Freeze rotation and motion along all axes.  
* * *
