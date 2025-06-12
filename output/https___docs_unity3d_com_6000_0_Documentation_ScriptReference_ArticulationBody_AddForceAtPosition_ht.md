* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForceAtPosition.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).AddForceAtPosition
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
public void AddForceAtPosition([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) force, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
force | The force vector in world coordinates.  
position | A position in world coordinates.  
mode | The type of force to apply.  
### Description
Applies a `force` at a specific `position`, resulting in applying a torque and force on the object.
For realistic effects, `position` should be approximately in the range of the surface of the Articulation Body. This is ideal for simulating explosions. To create realistic explosions, apply forces over several frames instead of just one. Note that when `position` is far away from the center of the Articulation Body, the applied torque will be unrealistically large.  
  
You can only apply a force to an active ArticulationBody. If a GameObject is inactive, AddForceAtPosition has no effect.  
  
[ForceMode.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html) mode modifies the Linear Velocity Per Second and Angular Velicity Per Second accumulators and [ForceMode.Impulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html) mode modifies the Linear Velocity Per Step and Angular Velocity Per Step accumulators. Mixing these 2 ForceModes doesn't work for Articulation Bodies and will result in only the Linear Velocity Per Second accumulator being applied.  
  
For more information on how ForceMode affects velocity, see [Rigidbody.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html).  
  
Applying a force to an ArticulationBody wakes up that body. If the force size is zero then the ArticulationBody does not wake up.   
Unit of measurement - N (newtons).  
  
**This method does not support**[ForceMode.Acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Acceleration.html)**and**[ForceMode.VelocityChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.VelocityChange.html)**.**  
  
Additional resources: [AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForce.html), [AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeForce.html), [AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddTorque.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ApplyForce(ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) body)
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = body.transform.position - transform.position;
        body.AddForceAtPosition(direction.normalized, transform.position);
    }
}

```

* * *
