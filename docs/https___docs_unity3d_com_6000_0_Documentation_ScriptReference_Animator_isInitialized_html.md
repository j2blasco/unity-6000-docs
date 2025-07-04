* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-isInitialized.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).isInitialized
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
isInitialized; 
### Description
Returns whether the animator is initialized successfully.
See [Animator.Rebind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.Rebind.html) to manually initialize the animator.
```
using UnityEngine;  
  
public class CheckAndRebind : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    void Start()
    {
        animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        if (!animator.isInitialized)
            animator.Rebind();
    }
}

```

* * *
