* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor.html

# JointMotor
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
The JointMotor is used to motorize a joint.
For example the [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) can be told to rotate at a given speed and force. The joint will then attempt to reach the velocity with the given maximum force.  
Additional resources: [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = GetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        // Make the hinge motor rotate with 90 degrees per second and a strong force.
        JointMotor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor.html) motor = hinge.motor;
        motor.force = 100;
        motor.targetVelocity = 90;
        motor.freeSpin = false;
        hinge.motor = motor;
    }
}

```

### Properties
Property | Description  
---|---  
[force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor-force.html) | The motor will apply a force.  
[freeSpin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor-freeSpin.html) | If freeSpin is enabled the motor will only accelerate but never slow down.  
[targetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor-targetVelocity.html) | The motor will apply a force up to force to achieve targetVelocity.  
* * *
