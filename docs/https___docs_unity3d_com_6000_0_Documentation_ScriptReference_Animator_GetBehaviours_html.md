* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBehaviours.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetBehaviours
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
public T[] GetBehaviours(); 
### Description
Returns all [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html) that match type `T` or are derived from `T`. Returns null if none are found.
```
using UnityEngine;
using System.Collections;  
  
// An example StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html).
public class BreathBehaviour : StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html)
{
    public bool  fastBreath;  
  
    // OnStateUpdate is called at each Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) frame between OnStateEnter and OnStateExit callback
    override public void OnStateUpdate(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        animator.SetBool("FastBreath", fastBreath);
    }
}  
  

public class RunBehaviour : StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html)
{
    // OnStateUpdate is called at each Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) frame between OnStateEnter and OnStateExit callback
    override public void OnStateUpdate(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        BreathBehaviour[] breathBehaviours = animator.GetBehaviours<BreathBehaviour>();
        for (int i = 0; i < breathBehaviours.Length; i++)
            breathBehaviours[i].fastBreath = true;
    }
}

```

* * *
