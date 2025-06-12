* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotationWeight.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetIKRotationWeight
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public void SetIKRotationWeight([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal, float value); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is set.  
value | The rotational weight.  
### Description
Sets the rotational weight of an IK goal (0 = rotation before IK, 1 = rotation at the IK goal).
An IK goal is a target position and rotation for a specific body part. Unity can calculate how to move the part toward the target from the starting point (ie, the current position and rotation obtained from the animation).  
  
This function sets a weight value in the range 0..1 to determine how far between the start and goal rotations the IK will aim. The goal itself is set separately using [SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) objToAimAt;
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void OnAnimatorIK(int layerIndex)
    {
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) handRotation = Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(objToAimAt.position - transform.position);
        animator.SetIKRotationWeight(AvatarIKGoal.RightHand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightHand.html), 1.0f);
        animator.SetIKRotation(AvatarIKGoal.RightHand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightHand.html), handRotation);
    }
}

```

Additional resources: [SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html), [SetIKPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPositionWeight.html).
* * *
