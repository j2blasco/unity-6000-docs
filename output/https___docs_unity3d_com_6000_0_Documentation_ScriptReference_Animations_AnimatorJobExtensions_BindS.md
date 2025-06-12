* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindStreamTransform.html

#  [AnimatorJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html).BindStreamTransform
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
public static [Animations.TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html) BindStreamTransform([Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform); 
### Parameters
Parameter | Description  
---|---  
animator | The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) instance that calls this method.  
transform | The [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) to bind.  
### Returns
**TransformStreamHandle** Returns the TransformStreamHandle that represents the new binding. 
### Description
Create a TransformStreamHandle representing the new binding between the [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) and a [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) already bound to the [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).
* * *
