* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html

# AnimatorJobExtensions
class in UnityEngine.Animations
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
Static class providing extension methods for [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) and the animation C# jobs.
The extension methods in this class can directly be used on an [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).  
  
Additional resources: [IAnimationJobPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJobPlayable.html).
### Static Methods
Method | Description  
---|---  
[AddJobDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.AddJobDependency.html) | Creates a dependency between animator jobs and the job represented by the supplied job handle. To add multiple job dependencies, call this method for each job that need to run before the Animator's jobs.  
[BindCustomStreamProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindCustomStreamProperty.html) | Create a custom property in the AnimationStream to pass extra data to downstream animation jobs in your graph. Custom properties created in the AnimationStream do not exist in the scene.  
[BindSceneProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindSceneProperty.html) | Create a PropertySceneHandle representing the new binding on the Component property of a Transform in the Scene.  
[BindSceneTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindSceneTransform.html) | Create a TransformSceneHandle representing the new binding between the Animator and a Transform in the Scene.  
[BindStreamProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindStreamProperty.html) | Create a PropertyStreamHandle representing the new binding on the Component property of a Transform already bound to the Animator.  
[BindStreamTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindStreamTransform.html) | Create a TransformStreamHandle representing the new binding between the Animator and a Transform already bound to the Animator.  
[CloseAnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.CloseAnimationStream.html) | Close a stream that has been opened using OpenAnimationStream.  
[OpenAnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.OpenAnimationStream.html) | Open a new stream on the Animator.  
[ResolveAllSceneHandles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.ResolveAllSceneHandles.html) | Newly created handles are always resolved lazily on the next access when the jobs are run. To avoid a cpu spike while evaluating the jobs you can manually resolve all handles from the main thread.  
[ResolveAllStreamHandles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.ResolveAllStreamHandles.html) | Newly created handles are always resolved lazily on the next access when the jobs are run. To avoid a cpu spike while evaluating the jobs you can manually resolve all handles from the main thread.  
[UnbindAllSceneHandles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.UnbindAllSceneHandles.html) | Removes all PropertySceneHandles and TransformSceneHandles associated with the Animator instance. Use this method to manage the lifecycle of scene handles when the animated hierarchy changes.  
[UnbindAllStreamHandles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.UnbindAllStreamHandles.html) | Removes all PropertyStreamHandles and TransformStreamHandles associated with the Animator instance. Use this method to manage the lifecycle of stream handles when the animated hierarchy changes.  
* * *
