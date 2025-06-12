* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorIK.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnAnimatorIK(int)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Parameters
Parameter | Description  
---|---  
layerIndex | The index of the layer on which the IK solver is called.  
### Description
Callback for setting up animation IK (inverse kinematics).
OnAnimatorIK() is called by the Animator Component immediately before it updates its internal IK system. This callback can be used to set the positions of the IK goals and their respective weights.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float leftFootPositionWeight;
    float leftFootRotationWeight;
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) leftFootObj;  
  
    private Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void OnAnimatorIK(int layerIndex)
    {
        animator.SetIKPositionWeight(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), leftFootPositionWeight);
        animator.SetIKRotationWeight(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), leftFootRotationWeight);
        animator.SetIKPosition(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), leftFootObj.position);
        animator.SetIKRotation(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), leftFootObj.rotation);
    }
}

```

Additional resources: [Animator.SetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html), [Animator.SetIKPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPositionWeight.html), [Animator.SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html), [Animator.SetIKRotationWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotationWeight.html).
* * *
