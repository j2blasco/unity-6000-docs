* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-motor.html

#  [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html).motor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HingeJoint.html "Go to HingeJoint Component in the Manual")
[JointMotor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor.html) motor; 
### Description
The motor will apply a force up to a maximum force to achieve the target velocity in degrees per second.
The motor tries to reach [JointMotor.targetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor-targetVelocity.html) angular velocity in degrees per second. The motor will only be able to reach `targetVelocity`, if [JointMotor.force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor-force.html) is sufficiently large. If the joint is spinning faster than `targetVelocity` the motor will brake. A negative `targetVelocity` will make the motor spin in the opposite direction.  
  
The `force` is the maximum torque the motor can exert. If it is zero the motor is disabled.  
  
The motor will brake when it is spinning faster than `targetVelocity` only, if [JointMotor.freeSpin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor-freeSpin.html) is false. If `freeSpin` is true the motor will not brake.  
  
Additional resources: [useMotor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-useMotor.html), [JointMotor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var hinge = GetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        // Make the hinge motor rotate with 90 degrees per second and a strong force.
        var motor = hinge.motor;
        motor.force = 100;
        motor.targetVelocity = 90;
        motor.freeSpin = false;
        hinge.motor = motor;
        hinge.useMotor = true;
    }
}

```

Modifying the motor does **not** automatically enable the motor.  
  
Enabling the motor **overrides** the [spring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-spring.html), given the spring was enabled. If the motor is again disabled the spring will be restored.
* * *
