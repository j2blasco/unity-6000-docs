* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForce.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).AddForce
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
public void AddForce([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) force, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
force | The force vector to apply.  
mode | The type of force to apply.  
### Description
Applies a force to the [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).
Note that the force accumulates over the duration of a simulation frame. It is only physically applied to the articulation body during the simulation step, after [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html) has been called to scripts. Specifying the [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) `mode` allows the type of force to be changed to an Acceleration, Impulse or Velocity Change.  
  
You can only apply a force to an active ArticulationBody. If a GameObject is inactive, AddForce has no effect. Also, the ArticulationBody must be movable (cannot be immovable).  
  
[ForceMode.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html) and [ForceMode.Acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Acceleration.html) modes modify the Linear Velocity Per Second accumulator and [ForceMode.Impulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html) and [ForceMode.VelocityChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.VelocityChange.html) modify the Linear Velocity Per Step accumulator. Mixing these 2 groups of ForceModes doesn't work for Articulation Bodies and will result in only the Linear Velocity Per Second accumulator being applied.  
  
For more information on how ForceMode affects velocity, see [Rigidbody.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html).  
  
By default the ArticulationBody's state is set to awake when a force is applied, unless the force is [Vector3.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html).   
Unit of measurement - N (newtons).  
  
Additional resources: [AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForceAtPosition.html), [AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeForce.html), [AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddTorque.html).  
  
This example applies a forward force to the GameObject's ArticulationBody.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) m_ArticulationBody;
    public float m_Thrust = 20f;  
  
    void Start()
    {
        //Fetch the ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached
        m_ArticulationBody = GetComponent<ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("Jump"))
        {
            //Apply a force to this ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) in the direction of this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s up-axis
            m_ArticulationBody.AddForce(transform.up * m_Thrust);
        }
    }
}

```

* * *
