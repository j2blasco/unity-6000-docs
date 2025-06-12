* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.SetProcessInputs.html

#  [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html).SetProcessInputs
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
public void SetProcessInputs(bool value); 
### Parameters
Parameter | Description  
---|---  
value | The new value for processing the inputs or not.  
### Description
Sets the new value for processing the inputs or not.
In some cases, like for custom mixers, it is wanted to have full control over which inputs are processed or not. This method allows to set that: when set to `true` (the default value), all the inputs are processed before processing the current [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html); when set to `false`, the playable inputs aren't processed and the user can force to process specific inputs using [AnimationStream.GetInputStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.GetInputStream.html) on the `stream` provided with the methods in [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html).  
  
Additional resources: [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html).
* * *
