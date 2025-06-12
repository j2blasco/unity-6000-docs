* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-rightFeetBottomHeight.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).rightFeetBottomHeight
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
rightFeetBottomHeight; 
### Description
Get right foot bottom height.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void LateUpdate()
    {
        if (animator)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rightFootT = animator.GetIKPosition(AvatarIKGoal.RightFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightFoot.html));
            Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rightFootQ = animator.GetIKRotation(AvatarIKGoal.RightFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.RightFoot.html));  
  
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rightFootH = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -animator.rightFeetBottomHeight, 0);  
  
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = rightFootT + rightFootQ * rightFootH;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(pos);
        }
    }
}

```

* * *
