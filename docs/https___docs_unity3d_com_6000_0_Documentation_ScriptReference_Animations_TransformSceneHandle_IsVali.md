* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.IsValid.html

#  [TransformSceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html).IsValid
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
public bool IsValid([Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream); 
### Parameters
Parameter | Description  
---|---  
stream | The AnimationStream that manages this handle.  
### Returns
**bool** Whether this is a valid handle. 
### Description
Returns whether this is a valid handle.
A TransformSceneHandle may be invalid if, for example, the transform binded to this handle is deleted or if you didn't use the correct function to create it.  
  
Additional resources: [AnimatorJobExtensions.BindSceneTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindSceneTransform.html).
* * *
