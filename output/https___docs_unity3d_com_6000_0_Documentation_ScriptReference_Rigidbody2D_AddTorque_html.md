* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddTorque.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).AddTorque
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
## Declaration
public void AddTorque(float torque, [ForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html) mode = ForceMode2D.Force); 
### Parameters
Parameter | Description  
---|---  
torque | Torque to apply.  
mode | The force mode to use.  
### Description
Apply a torque at the rigidbody's centre of mass.
Applying torque to the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) changes the [angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularVelocity.html) only. This change is scaled (divided) by the rotational [inertia](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-inertia.html). Therefore, a larger [inertia](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-inertia.html) results in smaller changes to [angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularVelocity.html), and a smaller [inertia](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-inertia.html) results in larger changes to [angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularVelocity.html).  
  
When applying torque either as a force or an impulse, you can use any value to get the required change in [angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularVelocity.html). However, if you require a specific change in degrees, then you must first convert the `torque` value into radians by multiplying with [Mathf.Deg2Rad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html) then multiplying by the [inertia](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-inertia.html).  
  
The following example demonstrates this as an impulse:  
  
Additional resources: [AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForce.html), [AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForceAtPosition.html).
```
using UnityEngine;  
  
public class TorqueRotationExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Add an impulse which produces a change in angular velocity (specified in degrees).
    public void AddTorqueImpulse(float angularChangeInDegrees)
    {
        var body = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
        var impulse = (angularChangeInDegrees * Mathf.Deg2Rad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html)) * body.inertia;  
  
        body.AddTorque(impulse, ForceMode2D.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Impulse.html));
    }
}

```

* * *
