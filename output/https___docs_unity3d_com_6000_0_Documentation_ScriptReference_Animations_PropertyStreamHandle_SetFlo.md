* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.SetFloat.html

#  [PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html).SetFloat
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
public void SetFloat([Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream, float value); 
### Parameters
Parameter | Description  
---|---  
stream | The [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) that holds the animated values.  
value | The new float property value.  
### Description
Sets the float property value into a stream.
If the property is not a float, the method will throw an `InvalidOperationException`.
* * *
