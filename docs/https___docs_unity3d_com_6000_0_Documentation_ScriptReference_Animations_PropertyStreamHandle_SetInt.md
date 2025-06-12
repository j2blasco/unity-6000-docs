* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.SetInt.html

#  [PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html).SetInt
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
public void SetInt([Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream, int value); 
### Parameters
Parameter | Description  
---|---  
stream | The [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) that holds the animated values.  
value | The new integer property value.  
### Description
Sets the integer property value into a stream.
If the property is not an integer, the method will throw an `InvalidOperationException`.
* * *
