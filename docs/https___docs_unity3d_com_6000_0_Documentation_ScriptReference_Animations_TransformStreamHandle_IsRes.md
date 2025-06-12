* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.IsResolved.html

#  [TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html).IsResolved
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
public bool IsResolved([Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream); 
### Parameters
Parameter | Description  
---|---  
stream | The [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) that holds the animated values.  
### Returns
**bool** Returns `true` if the handle is resolved, `false` otherwise. 
### Description
Returns whether this handle is resolved.
A TransformStreamHandle is resolved if it is valid, if it has the same bindings version than the one in the stream, and if it is bound to the transform in the stream. A TransformStreamHandle can become unresolved if the animator bindings have changed or if the transform had been destroyed.  
  
Additional resources: [Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.Resolve.html), and [IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.IsValid.html).
* * *
