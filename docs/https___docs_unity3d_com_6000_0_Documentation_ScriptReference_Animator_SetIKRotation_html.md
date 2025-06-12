* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetIKRotation
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
public void SetIKRotation([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) goalRotation); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is set.  
goalRotation | The rotation of the goal in world space which should follow Unity's world coordinates convention (see below).  
### Description
Sets the rotation of an IK goal.
An IK goal is a specified target position and rotation for a specific body part. Unity calculates how to move the body part towards this target from a starting point. This starting point could be, for example, the current position and rotation obtained from an animation.  
  
This function sets the IK goal rotation in world space. When specifying the IK goal rotation, it should follow Unity's world coordinates convention: • The `X-Axis` is parallel to the palm of the hand (or sole of the foot), pointing sideways to the right of the hand (or foot).  
• The `Y-Axis` is perpendicular to the top of the hand (or foot), pointing upwards.  
• The `Z-Axis` is parallel to the palm of the hand (or sole of the foot), pointing forwards toward the fingers (or toes).  
  
  
It is recommended that the bone orientation of the avatar skeleton pose should also follow Unity's world coordinates convention. If your avatar skeleton pose follows a different convention, the bone rotation applied to the corresponding `GameObject` might differ from the IK goal rotation.  
  
In addition, you can set a weight value to set the amount of influence that the IK goal rotation has over the starting rotation. Use the `SetIKRotationWeight` method to set a weight value between 0..1 where a weight of 0 means no influence and a weight of 1 means full influence.   
  
The following code example demonstrates how to use the `SetIKRotation` method and `SetIKRotationWeight` method. 
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
Additional resources: [SetIKRotationWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotationWeight.html), [SetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html).
* * *
