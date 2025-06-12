* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SharedBetweenAnimatorsAttribute.html

# SharedBetweenAnimatorsAttribute
class in UnityEngine
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
The SharedBetweenAnimatorsAttribute specifies that this StateMachineBehaviour is instantiated only once and shared by all Animator instances. This attribute reduces the memory footprint for each controller instance.
You choose which StateMachineBehaviour uses this attribute. If your StateMachineBehaviour changes a member variable, this affects all other Animator instances that use it. Additional resources: [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html) class.
```
using UnityEngine;  
  
[SharedBetweenAnimators]
public class AttackBehaviour : StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html)
{
    public override void OnStateEnter(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnStateEnter");
    }
}

```

* * *
