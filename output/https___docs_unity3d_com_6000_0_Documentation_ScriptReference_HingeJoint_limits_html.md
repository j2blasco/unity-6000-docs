* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-limits.html

#  [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html).limits
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
[JointLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits.html) limits; 
### Description
Limit of angular rotation (in degrees) on the hinge joint.
The joint will be limited so that the angle is always between [JointLimits.min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-min.html) and [JointLimits.max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-max.html). The joint angle is in degrees relative to the rest angle. The rest angle between the bodies is always zero at the beginning of the simulation.  
  
Additional resources: [useLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint-useLimits.html), [JointLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set the hinge limits for a door.
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = GetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        JointLimits[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits.html) limits = hinge.limits;
        limits.min = 0;
        limits.bounciness = 0;
        limits.bounceMinVelocity = 0;
        limits.max = 90;
        hinge.limits = limits;
        hinge.useLimits = true;
    }
}

```

Modifying the limits does **not** automatically enable the limits.
* * *
