* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-spring.html

#  [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html).spring
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
[JointSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html) spring; 
### Description
The spring attempts to reach a target angle by adding spring and damping forces.
The [JointSpring.spring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-spring.html) force attempts to reach the target angle. A larger value makes the spring reach the target position faster.  
  
The [JointSpring.damper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-damper.html) force dampens the angular velocity. A larger value makes the spring reach the goal slower.  
  
The spring reaches for the [JointSpring.targetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-targetPosition.html) angle in degrees relative to the rest angle. The rest angle between the bodies is always zero at the beginning of the simulation.  
  
Additional resources: [useSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-useSpring.html), [JointSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html), [useAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-useAcceleration.html).
```
using UnityEngine;
using System.Collections;  
  

public class HingeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = GetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        // Make the spring reach shoot for a 70 degree angle.
        // This could be used to fire off a catapult.  
  
        JointSpring[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html) hingeSpring = hinge.spring;
        hingeSpring.spring = 10;
        hingeSpring.damper = 3;
        hingeSpring.targetPosition = 70;
        hinge.spring = hingeSpring;
        hinge.useSpring = true;
    }
}

```

Modifying the spring does **not** automatically enable it.  
  
Enabling the [motor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-motor.html) **overrides** the spring, given the spring was enabled. If the motor is again disabled the spring will be restored.
* * *
