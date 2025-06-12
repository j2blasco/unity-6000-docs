* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html

# AnimationUtility
class in UnityEditor
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
Editor utility functions for modifying animation clips.
### Static Properties
Property | Description  
---|---  
[onCurveWasModified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility-onCurveWasModified.html) | Called when an animation curve, in an animation clip, is modified.  
### Static Methods
Method | Description  
---|---  
[CalculateTransformPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.CalculateTransformPath.html) | Retrieves the path from the root Transform to the target Transform.  
[EditorCurveBindingsToGenericBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.EditorCurveBindingsToGenericBindings.html) | Converts EditorCurveBinding to GenericBinding.  
[GetAnimatableBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetAnimatableBindings.html) | Retrieves the animatable bindings for a specific GameObject.  
[GetAnimatedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetAnimatedObject.html) | Retrieves the animated object that the binding points to.  
[GetAnimationClips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetAnimationClips.html) | Retrieves an array of animation clips associated with a GameObject or component. GetAnimationClips(Animation) is obsolete and has been replaced with GetAnimationClips(GameObject).  
[GetAnimationEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetAnimationEvents.html) | Retrieves all animation events associated with an animation clip.  
[GetCurveBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetCurveBindings.html) | Retrieves the float curve bindings in an animation clip.  
[GetDiscreteIntValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetDiscreteIntValue.html) | Retrieves the discrete integer value that the binding points to.  
[GetEditorCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetEditorCurve.html) | Retrieves the float curve that the binding points to.  
[GetFloatValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetFloatValue.html) | Retrieves the float value that the binding points to.  
[GetKeyBroken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetKeyBroken.html) | Retrieves the broken tangent flag for a specfic keyframe.  
[GetKeyLeftTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetKeyLeftTangentMode.html) | Retrieves the left tangent mode of the keyframe at a specific index.  
[GetKeyRightTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetKeyRightTangentMode.html) | Retrieves the right tangent mode of the keyframe at a specific index.  
[GetObjectReferenceCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetObjectReferenceCurve.html) | Retrieves the object reference curve that the binding points to.  
[GetObjectReferenceCurveBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetObjectReferenceCurveBindings.html) | Retrieves the object reference curve bindings stored in the animation clip.  
[GetObjectReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetObjectReferenceValue.html) | Retrieves the object value that the binding points to.  
[SetAdditiveReferencePose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetAdditiveReferencePose.html) | Sets the additive reference pose from referenceClip at time for animation clip clip.  
[SetAnimationClips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetAnimationClips.html) | Sets the array of animation clips to be referenced in the Animation component.  
[SetAnimationEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetAnimationEvents.html) | Replaces all animation events in the animation clip.  
[SetEditorCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetEditorCurve.html) | Adds, modifies, or removes an editor float curve in an animation clip.  
[SetEditorCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetEditorCurves.html) | Adds, modifies, or removes multiple editor float curves in an animation clip.  
[SetKeyBroken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyBroken.html) | Change the specified keyframe broken tangent flag.  
[SetKeyLeftTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyLeftTangentMode.html) | Change the specified keyframe tangent mode.  
[SetKeyRightTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyRightTangentMode.html) | Change the specified keyframe tangent mode.  
[SetObjectReferenceCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetObjectReferenceCurve.html) | Adds, modifies, or removes an object reference curve in an animation clip.  
[SetObjectReferenceCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetObjectReferenceCurves.html) | Adds, modifies, or removes object references curve in an animation clip.  
### Delegates
Delegate | Description  
---|---  
[OnCurveWasModified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.OnCurveWasModified.html) | Triggered when an animation curve, in an animation clip, has been modified.  
* * *
