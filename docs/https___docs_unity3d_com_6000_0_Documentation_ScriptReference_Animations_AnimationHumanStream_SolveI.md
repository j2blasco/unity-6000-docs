* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SolveIK.html

#  [AnimationHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html).SolveIK
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
public void SolveIK(); 
### Description
Execute the IK solver.
The humanoid IK solver is executed using the IK goal position, rotation, and weight currently set in the [AnimationHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html).
```
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public struct IKJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public TransformSceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html) effector;
    public PropertySceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html) positionWeight;
    public PropertySceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html) rotationWeight;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream) {}  
  
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        AnimationHumanStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html) humanStream = stream.AsHuman();
        if (effector.IsValid(stream) && positionWeight.IsValid(stream) && rotationWeight.IsValid(stream))
        {
            humanStream.SetGoalPosition(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), effector.GetPosition(stream));
            humanStream.SetGoalRotation(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), effector.GetRotation(stream));
            humanStream.SetGoalWeightPosition(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), positionWeight.GetFloat(stream));
            humanStream.SetGoalWeightRotation(AvatarIKGoal.LeftFoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.LeftFoot.html), rotationWeight.GetFloat(stream));
        }  
  
        humanStream.SolveIK();
    }
}

```

* * *
