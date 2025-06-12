* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html

# AnimationHumanStream
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
The humanoid stream of animation data passed from one [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) to another.
The AnimationHumanStream structure is passed through the animation [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) structures, like [AnimationClipPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.html) and [AnimationMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html). They can be modified when used with an [IAnimationJobPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJobPlayable.html), like the [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html).  
  
The Playables implementing [IAnimationJobPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJobPlayable.html) take a custom C# job, which must implement [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html), and the AnimationHumanStream is then passed to its callbacks during the animation processing pass.  
  
Additional resources: [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html), [AnimationStream.isHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-isHumanStream.html), and AnimationStream.AsHuman().
### Properties
Property | Description  
---|---  
[bodyLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-bodyLocalPosition.html) | The position of the body center of mass relative to the root.  
[bodyLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-bodyLocalRotation.html) | The rotation of the body center of mass relative to the root.  
[bodyPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-bodyPosition.html) | The position of the body center of mass in world space.  
[bodyRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-bodyRotation.html) | The rotation of the body center of mass in world space.  
[humanScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-humanScale.html) | The scale of the Avatar. (Read Only)  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-isValid.html) | Returns true if the stream is valid; false otherwise. (Read Only)  
[leftFootHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-leftFootHeight.html) | The left foot height from the floor. (Read Only)  
[leftFootVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-leftFootVelocity.html) | The left foot velocity from the last evaluated frame. (Read Only)  
[rightFootHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-rightFootHeight.html) | The right foot height from the floor. (Read Only)  
[rightFootVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-rightFootVelocity.html) | The right foot velocity from the last evaluated frame. (Read Only)  
### Public Methods
Method | Description  
---|---  
[GetGoalLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalLocalPosition.html) | Returns the position of this IK goal relative to the root.  
[GetGoalLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalLocalRotation.html) | Returns the rotation of this IK goal relative to the root.  
[GetGoalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalPosition.html) | Returns the position of this IK goal in world space.  
[GetGoalPositionFromPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalPositionFromPose.html) | Returns the position of this IK goal in world space computed from the stream current pose.  
[GetGoalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalRotation.html) | Returns the rotation of this IK goal in world space.  
[GetGoalRotationFromPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalRotationFromPose.html) | Returns the rotation of this IK goal in world space computed from the stream current pose.  
[GetGoalWeightPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalWeightPosition.html) | Returns the position weight of the IK goal.  
[GetGoalWeightRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetGoalWeightRotation.html) | Returns the rotation weight of the IK goal.  
[GetHintPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetHintPosition.html) | Returns the position of this IK Hint in world space.  
[GetHintWeightPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetHintWeightPosition.html) | Returns the position weight of the IK Hint.  
[GetMuscle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.GetMuscle.html) | Returns the muscle value.  
[ResetToStancePose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.ResetToStancePose.html) | Reset the current pose to the stance pose (T Pose).  
[SetGoalLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetGoalLocalPosition.html) | Sets the position of this IK goal relative to the root.  
[SetGoalLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetGoalLocalRotation.html) | Sets the rotation of this IK goal relative to the root.  
[SetGoalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetGoalPosition.html) | Sets the position of this IK goal in world space.  
[SetGoalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetGoalRotation.html) | Sets the rotation of this IK goal in world space.  
[SetGoalWeightPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetGoalWeightPosition.html) | Sets the position weight of the IK goal.  
[SetGoalWeightRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetGoalWeightRotation.html) | Sets the rotation weight of the IK goal.  
[SetHintPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetHintPosition.html) | Sets the position of this IK hint in world space.  
[SetHintWeightPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetHintWeightPosition.html) | Sets the position weight of the IK Hint.  
[SetLookAtBodyWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetLookAtBodyWeight.html) | Sets the LookAt body weight.  
[SetLookAtClampWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetLookAtClampWeight.html) | Sets the LookAt clamp weight.  
[SetLookAtEyesWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetLookAtEyesWeight.html) | Sets the LookAt eyes weight.  
[SetLookAtHeadWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetLookAtHeadWeight.html) | Sets the LookAt head weight.  
[SetLookAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetLookAtPosition.html) | Sets the look at position in world space.  
[SetMuscle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SetMuscle.html) | Sets the muscle value.  
[SolveIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.SolveIK.html) | Execute the IK solver.  
* * *
