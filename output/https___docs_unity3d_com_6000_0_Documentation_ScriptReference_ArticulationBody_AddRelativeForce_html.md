* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeForce.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).AddRelativeForce
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
public void AddRelativeForce([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) force, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
force | The force vector in local coordinates.  
mode | The type of force to apply.  
### Description
Applies a `force` to the Articulation Body, relative to its local coordinate system.
You can only apply a force to an active ArticulationBody. If a GameObject is inactive, AddRelativeForce has no effect.  
  
[ForceMode.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html) and [ForceMode.Acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Acceleration.html) modes modify the Linear Velocity Per Second accumulator and [ForceMode.Impulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html) and [ForceMode.VelocityChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.VelocityChange.html) modify the Linear Velocity Per Step accumulator. Mixing these 2 groups of ForceModes doesn't work for Articulation Bodies and will result in only the Linear Velocity Per Second accumulator being applied.  
  
For more information on how ForceMode affects velocity, see [Rigidbody.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html).  
  
Applying a force to an ArticulationBody wakes up that body. If the force size is zero then the ArticulationBody does not wake up.   
Unit of measurement - N (newtons).  
  
Additional resources: [AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForce.html), [AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForceAtPosition.html), [AddRelativeTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeTorque.html).
```
using UnityEngine;
using System.Collections;  
  
// Add a thrust force to push an object in its current forward
// direction (to simulate a rocket motor, say).
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float thrust;
    public ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) ab;
    void Start()
    {
        ab = GetComponent<ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        ab.AddRelativeForce(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * thrust);
    }
}

```

* * *
