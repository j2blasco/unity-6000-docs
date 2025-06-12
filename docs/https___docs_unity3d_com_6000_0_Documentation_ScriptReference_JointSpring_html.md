* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html

# JointSpring
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
JointSpring is used add a spring force to [HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) and [PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = GetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        // Make the spring reach shoot for a 70 degree angle.
        // This could be used to fire off a catapult.  
  
        JointSpring[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html) spring = hinge.spring;
        spring.spring = 10;
        spring.damper = 3;
        spring.targetPosition = 70;
        hinge.spring = spring;
    }
}

```

### Properties
Property | Description  
---|---  
[damper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-damper.html) | The damper force uses to dampen the spring.  
[spring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-spring.html) | The spring forces used to reach the target position.  
[targetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-targetPosition.html) | The target position the joint attempts to reach.  
* * *
