* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.OpenAnimationStream.html

#  [AnimatorJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html).OpenAnimationStream
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
public static bool OpenAnimationStream([Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, ref [Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream); 
### Parameters
Parameter | Description  
---|---  
animator | The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) instance that calls this method.  
stream | The new stream.  
### Returns
**bool** Returns whether or not the stream has been opened. 
### Description
Open a new stream on the [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).
The stream opened this way must be closed using [CloseAnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.CloseAnimationStream.html).
* * *
