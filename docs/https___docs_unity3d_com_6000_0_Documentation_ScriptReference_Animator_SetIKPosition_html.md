* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetIKPosition
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
public void SetIKPosition([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) goalPosition); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is set.  
goalPosition | The position in world space.  
### Description
Sets the position of an IK goal.
An IK goal is a target position and rotation for a specific body part. Unity can calculate how to move the part toward the target from the starting point (ie, the current position and rotation obtained from the animation).  
  
This function sets the position of the ultimate goal in world space; the actual point in space where the body part ends up is also influenced by a weight parameter that specifies how far between the start and the goal the IK should aim (a value in the range 0..1).  
  
This function should always be called in [MonoBehaviour.OnAnimatorIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorIK.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) objToPickUp;
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void OnAnimatorIK(int layerIndex)
    {
        float reach = animator.GetFloat("RightHandReach");
        animator.SetIKPositionWeight(AvatarIKGoal.RightHand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightHand.html), reach);
        animator.SetIKPosition(AvatarIKGoal.RightHand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightHand.html), objToPickUp.position);
    }
}

```

Additional resources: [SetIKPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPositionWeight.html), [SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html).
* * *
