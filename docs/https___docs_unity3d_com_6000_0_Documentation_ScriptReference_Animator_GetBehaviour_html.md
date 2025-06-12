* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBehaviour.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetBehaviour
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
public T GetBehaviour(); 
### Description
Returns the first [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html) that matches type `T` or is derived from `T`. Returns null if none are found.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class RunBehaviour : StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html)
{
    // OnStateUpdate is called at each Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) frame between OnStateEnter and OnStateExit callback
    override public void OnStateUpdate(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform = animator.GetComponent<Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)>();  
  
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) dir = transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1.5f, 0), dir, out hitInfo, 10))
        {
            if (hitInfo.collider.tag == "Obstacle")
            {
                animator.GetBehaviour<SlideBehaviour>().target = transform.position + 1.25f * hitInfo.distance * dir;
                if (hitInfo.distance < 6)
                    animator.SetTrigger("Slide");
            }
        }
    }
}  
  
public class SlideBehaviour : StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) target;  
  
    public float slideMatchTargetStart = 0.11f;
    public float slideMatchTargetStop = 0.40f;  
  
    // OnStateUpdate is called at each Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) frame between OnStateEnter and OnStateExit callback
    override public void OnStateUpdate(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        animator.MatchTarget(target, new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)(), AvatarTarget.Root[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarTarget.Root.html), new MatchTargetWeightMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MatchTargetWeightMask.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 0, 1), 0), slideMatchTargetStart, slideMatchTargetStop);
    }
}

```

* * *
