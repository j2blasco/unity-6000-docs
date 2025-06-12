* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html

# AnimationScriptPlayable
struct in UnityEngine.Animations
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
Leave feedback
  

Implements interfaces:[IAnimationJobPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJobPlayable.html), [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html)
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
A [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) that can run a custom, multi-threaded animation job.
This playable allows to create a custom C# job that will give read and write access to the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) during the animation process pass in the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html). The C# job must implement the interface [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html).  
  
NOTE: You can use [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html) methods with AnimationScriptPlayable objects.  
  
Additional resources: [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html), and [AnimationScriptPlayable.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html).
### Public Methods
Method | Description  
---|---  
[GetJobData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.GetJobData.html) | Gets the job data contained in the playable.  
[GetProcessInputs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.GetProcessInputs.html) | Returns whether the playable inputs will be processed or not.  
[SetJobData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.SetJobData.html) | Sets a new job data in the playable.  
[SetProcessInputs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.SetProcessInputs.html) | Sets the new value for processing the inputs or not.  
### Static Methods
Method | Description  
---|---  
[Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html) | Creates an AnimationScriptPlayable in the PlayableGraph.  
* * *
