* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html

# AnimationStream
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
The stream of animation data passed from one [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) to another.
The AnimationStream structure is passed through the animation [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) structures, like [AnimationClipPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.html) and [AnimationMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html). They can be modified when used with an [IAnimationJobPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJobPlayable.html), like the [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html).  
  
The Playables implementing [IAnimationJobPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJobPlayable.html) take a custom C# job, which must implement [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html), and the AnimationStream is then passed to its callbacks during the animation processing pass.  
  
Additional resources: [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html), [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html), [TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html), [PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html), [TransformSceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html), and [PropertySceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html).
### Properties
Property | Description  
---|---  
[angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-angularVelocity.html) | Gets or sets the avatar angular velocity for the evaluated frame.  
[deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-deltaTime.html) | Gets the delta time for the evaluated frame. (Read Only)  
[inputStreamCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-inputStreamCount.html) | Gets the number of input streams. (Read Only)  
[isHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-isHumanStream.html) | Returns true if the stream is from a humanoid avatar; false otherwise. (Read Only)  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-isValid.html) | Returns true if the stream is valid; false otherwise. (Read Only)  
[rootMotionPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-rootMotionPosition.html) | Gets the root motion position for the evaluated frame. (Read Only)  
[rootMotionRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-rootMotionRotation.html) | Gets the root motion rotation for the evaluated frame. (Read Only)  
[velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream-velocity.html) | Gets or sets the avatar velocity for the evaluated frame.  
### Public Methods
Method | Description  
---|---  
[AsHuman](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.AsHuman.html) | Gets the same stream, but as an AnimationHumanStream.  
[CopyAnimationStreamMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.CopyAnimationStreamMotion.html) | Deep copies motion from a source animation stream to the current animation stream.  
[GetInputStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.GetInputStream.html) | Gets the AnimationStream of the playable input at index.  
[GetInputWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.GetInputWeight.html) | Gets the weight of the Playable connected at a specific input index.  
* * *
