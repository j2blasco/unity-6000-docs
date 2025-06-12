* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController-ctor.html

# AnimatorOverrideController Constructor
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
## Declaration
public AnimatorOverrideController(); 
### Description
Creates an empty Animator Override Controller.
* * *
## Declaration
public AnimatorOverrideController([RuntimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeAnimatorController.html) controller); 
### Parameters
Parameter | Description  
---|---  
controller | Runtime Animator Controller to override.  
### Description
Creates an Animator Override Controller that overrides **controller**.
Although the Animator Override Controller doesn't support nested Animator Override Controller, this constructor will find the right controller for you.
```
using UnityEngine;  
  
public class SwapWeapon : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    protected Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;
    protected AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html) animatorOverrideController;  
  
    public void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        animatorOverrideController = new AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html)(animator.runtimeAnimatorController);
        animator.runtimeAnimatorController = animatorOverrideController;
    }
}

```

* * *
