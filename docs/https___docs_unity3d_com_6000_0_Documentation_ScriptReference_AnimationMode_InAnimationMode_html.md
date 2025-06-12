* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html

#  [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html).InAnimationMode
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
public static bool InAnimationMode(); 
## Declaration
public static bool InAnimationMode([AnimationModeDriver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationModeDriver.html) driver); 
### Parameters
Parameter | Description  
---|---  
driver | An [AnimationModeDriver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationModeDriver.html) object that tests if [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) has been locked specifically for this driver.  
### Description
Checks whether the Editor is in Animation mode.
[InAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html) returns a value of true or false, indicating whether the animation is being controlled by [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html). If [InAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html) returns `true` then [SampleAnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html) can be used to animate the attached object.  
  
**Note:** The script example at [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) shows how [InAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html) can be used.
* * *
