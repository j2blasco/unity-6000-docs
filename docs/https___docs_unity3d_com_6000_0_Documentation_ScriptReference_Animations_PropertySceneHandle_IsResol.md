* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.IsResolved.html

#  [PropertySceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html).IsResolved
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
stream | The [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) managing this handle.  
### Returns
**bool** Returns `true` if the handle is resolved, `false` otherwise. 
### Description
Returns whether or not the handle is resolved.
A PropertySceneHandle is resolved if it is valid, and if it is bound to the property. A PropertySceneHandle can become unresolved if the property doesn't exist anymore (e.g. the component has been removed).  
  
Additional resources: [Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.Resolve.html), and [IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.IsValid.html).
* * *
