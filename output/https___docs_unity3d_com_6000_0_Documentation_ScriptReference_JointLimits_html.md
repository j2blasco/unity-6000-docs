* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits.html

# JointLimits
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
JointLimits is used by the [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) to limit the joints angle.
Additional resources: [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html).
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
        limits.max = 90;
        limits.bounciness = 0;
        limits.bounceMinVelocity = 0;
        hinge.limits = limits;
    }
}

```

### Properties
Property | Description  
---|---  
[bounceMinVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-bounceMinVelocity.html) | The minimum impact velocity which will cause the joint to bounce.  
[bounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-bounciness.html) | Determines the size of the bounce when the joint hits it's limit. Also known as restitution.  
[contactDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-contactDistance.html) | Distance inside the limit value at which the limit will be considered to be active by the solver.  
[max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-max.html) | The upper angular limit (in degrees) of the joint.  
[min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits-min.html) | The lower angular limit (in degrees) of the joint.  
* * *
