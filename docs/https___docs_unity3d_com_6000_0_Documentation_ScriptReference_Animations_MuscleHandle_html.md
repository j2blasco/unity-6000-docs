* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.html

# MuscleHandle
struct in UnityEngine.Animations
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
Handle for a muscle in the [AnimationHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html).
MuscleHandle can only be used on [AnimationHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html), otherwise an `InvalidOperationException` is thrown.
```
using UnityEngine;
using UnityEngine.Animations;
using UnityEngine.Playables;  
  
public struct MuscleHandleExampleJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public MuscleHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.html) muscleHandle;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream) {}
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        AnimationHumanStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html) humanStream = stream.AsHuman();  
  
        // Get a muscle value.
        float muscleValue = humanStream.GetMuscle(muscleHandle);  
  
        // Set a muscle value.
        humanStream.SetMuscle(muscleHandle, muscleValue);
    }
}  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)))]
public class MuscleHandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();
        var output = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(graph, "output", GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>());  
  
        var job = new MuscleHandleExampleJob();
        job.muscleHandle = new MuscleHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.html)(HumanPartDof.LeftArm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPartDof.LeftArm.html), ArmDof.HandDownUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.HandDownUp.html));  
  
        var scriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(graph, job);
        output.SetSourcePlayable(scriptPlayable);  
  
        graph.Evaluate(1.0f);  
  
        graph.Destroy();
    }
}

```

### Static Properties
Property | Description  
---|---  
[muscleHandleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle-muscleHandleCount.html) | The total number of DoF parts in a humanoid. (Read Only)  
### Properties
Property | Description  
---|---  
[dof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle-dof.html) | The muscle human sub-part. (Read Only)  
[humanPartDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle-humanPartDof.html) | The muscle human part. (Read Only)  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle-name.html) | The name of the muscle. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[MuscleHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle-ctor.html) | The different constructors that creates the muscle handle.  
### Static Methods
Method | Description  
---|---  
[GetMuscleHandles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.GetMuscleHandles.html) | Fills the array with all the possible muscle handles on a humanoid.  
* * *
