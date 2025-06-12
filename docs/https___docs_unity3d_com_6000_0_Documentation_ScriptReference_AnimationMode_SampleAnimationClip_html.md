* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html

#  [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html).SampleAnimationClip
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
public static void SampleAnimationClip([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, float time); 
### Parameters
Parameter | Description  
---|---  
gameObject | The root [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) for the animation.  
clip | The [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) to sample.  
time | The time at which to sample.  
### Returns
**void** Returns true when the Editor is in Animation mode. Returns false otherwise. 
### Description
Samples the [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) for the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and also records modified properties when in Animation mode.
If this method returns true, you can use [SampleAnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html) to animate the attached object.  
  
**Note:** The script example for [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) demonstrates how to use [InAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html).
* * *
