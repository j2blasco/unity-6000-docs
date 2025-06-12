* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPositionWeight.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetIKPositionWeight
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
public void SetIKPositionWeight([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal, float value); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is set.  
value | The translative weight.  
### Description
Sets the translative weight of an IK goal (0 = at the original animation before IK, 1 = at the goal).
An IK goal is a target position and rotation for a specific body part. Unity can calculate how to move the part toward the target from the starting point (ie, the current position and rotation obtained from the animation).  
  
This function sets a weight value in the range 0..1 to determine how far between the start and goal positions the IK will aim. The position itself is set separately using [SetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) objToPickUp;
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void OnAnimatorIK(int layerIndex)
    {
        // Retrieves the value of the parameter "RightHandReach" that must be created in the AnimatorController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).
        float reach = animator.GetFloat("RightHandReach");  
  
        // Sets IK Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) and IK Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) Weight.
        animator.SetIKPositionWeight(AvatarIKGoal.RightHand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightHand.html), reach);
        animator.SetIKPosition(AvatarIKGoal.RightHand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightHand.html), objToPickUp.position);
    }
}

```

Additional resources: [SetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html), [SetIKRotationWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotationWeight.html).
* * *
