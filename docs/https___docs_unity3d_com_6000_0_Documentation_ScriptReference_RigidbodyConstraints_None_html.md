* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.None.html

#  [RigidbodyConstraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html).None
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
No constraints.
```
//This example shows how RigidbodyConstraints[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html) is used to freeze the position and rotation of a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) in the z axis at start-up.
//It also shows what happens when these constraints are removed, when you press the space key
//Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to see it in action  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
* * *
