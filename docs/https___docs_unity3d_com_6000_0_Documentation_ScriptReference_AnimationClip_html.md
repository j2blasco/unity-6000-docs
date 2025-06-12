* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html

# AnimationClip
class in UnityEngine
/
Inherits from:[Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html "Go to AnimationClip Component in the Manual")
### Description
Stores keyframe based animations.
AnimationClip is used by [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) to play back animations.
### Properties
Property | Description  
---|---  
[empty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-empty.html) | Returns true if the animation clip has no curves and no events.  
[events](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-events.html) | Animation Events for this animation clip.  
[frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-frameRate.html) | Frame rate at which keyframes are sampled. (Read Only)  
[hasGenericRootTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-hasGenericRootTransform.html) | Returns true if the Animation has animation on the root transform.  
[hasMotionCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-hasMotionCurves.html) | Returns true if the AnimationClip has root motion curves.  
[hasMotionFloatCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-hasMotionFloatCurves.html) | Returns true if the AnimationClip has editor curves for its root motion.  
[hasRootCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-hasRootCurves.html) | Returns true if the AnimationClip has root Curves.  
[humanMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-humanMotion.html) | Returns true if the animation contains curve that drives a humanoid rig.  
[legacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-legacy.html) | Set to true if the AnimationClip will be used with the Legacy Animation component ( instead of the Animator ).  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-length.html) | Animation length in seconds. (Read Only)  
[localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-localBounds.html) | AABB of this Animation Clip in local space of Animation component that it is attached too.  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-wrapMode.html) | Sets the default wrap mode used in the animation state.  
### Constructors
Constructor | Description  
---|---  
[AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-ctor.html) | Creates a new animation clip.  
### Public Methods
Method | Description  
---|---  
[AddEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.AddEvent.html) | Adds an animation event to the clip.  
[ClearCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.ClearCurves.html) | Clears all curves from the clip.  
[EnsureQuaternionContinuity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.EnsureQuaternionContinuity.html) | Realigns quaternion keys to ensure shortest interpolation paths.  
[SampleAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.SampleAnimation.html) | Samples an animation at a given time for any animated properties.  
[SetCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.SetCurve.html) | Assigns the curve to animate a specific property.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
