* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddTorque.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).AddTorque
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
## Declaration
public void AddTorque([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) torque, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
torque | The torque to apply.  
mode | The type of torque to apply.  
### Description
Add torque to the articulation body.
You can only apply a torque to an active ArticulationBody. If a GameObject is inactive, AddTorque has no effect.  
  
[ForceMode.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html) and [ForceMode.Acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Acceleration.html) modes modify the Angular Velocity Per Second accumulator and [ForceMode.Impulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html) and [ForceMode.VelocityChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.VelocityChange.html) modify the Angular Velocity Per Step accumulator. Mixing these 2 groups of ForceModes doesn't work for Articulation Bodies and will result in only the Angular Velocity Per Second accumulator being applied.  
  
For more information on how ForceMode affects angular velocity, see [Rigidbody.AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddTorque.html).  
  
Applying a torque to an ArticulationBody wakes up that body. If the torque size is zero then the ArticulationBody does not wake up.   
Unit of measurement - Nm (Newtonmeters).  
  
Additional resources: [AddRelativeTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeTorque.html), [AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForce.html).
```
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) an object around its Y (upward) axis in response to
// left/right controls.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float torque;
    public ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) ab;  
  
    void Start()
    {
        ab = GetComponent<ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        float turn = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal");
        ab.AddTorque(transform.up * torque * turn);
    }
}

```

* * *
