* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddRelativeTorque.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).AddRelativeTorque
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
## Declaration
public void AddRelativeTorque([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) torque, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
torque | Torque vector in local coordinates.  
### Description
Adds a torque to the rigidbody relative to its coordinate system.
Force can be applied only to an active rigidbody. If a GameObject is inactive, AddRelativeTorque has no effect.  
  
Wakes up the Rigidbody by default. If the torque size is zero then the Rigidbody will not be woken up.  
  
For more information on how ForceMode affects angular velocity, see [Rigidbody.AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddTorque.html).  
  
Additional resources: [AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddTorque.html), [AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddRelativeForce.html).
```
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) an object around its Y (upward) axis in response to
// left/right controls.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float torque;
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        float turn = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal");
        rb.AddRelativeTorque(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * torque * turn);
    }
}

```

* * *
## Declaration
public void AddRelativeTorque(float x, float y, float z, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
x | Size of torque along the local x-axis.  
y | Size of torque along the local y-axis.  
z | Size of torque along the local z-axis.  
### Description
Adds a torque to the rigidbody relative to its coordinate system.
Force can be applied only to an active rigidbody. If a GameObject is inactive, AddRelativeTorque has no effect.  
  
Wakes up the Rigidbody by default. If the torque size is zero then the Rigidbody will not be woken up.
* * *
