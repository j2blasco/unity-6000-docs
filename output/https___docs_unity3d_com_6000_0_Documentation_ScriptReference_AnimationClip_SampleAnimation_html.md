* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.SampleAnimation.html

#  [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html).SampleAnimation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html "Go to AnimationClip Component in the Manual")
## Declaration
public void SampleAnimation([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, float time); 
### Parameters
Parameter | Description  
---|---  
go | The animated game object.  
time | The time to sample an animation.  
### Description
Samples an animation at a given time for any animated properties.
It is recommended to use the [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) interface instead for performance reasons. This will sample `animation` at the given `time`. Any component properties that are animated in the clip will be replaced with the sampled value. Most of the time you want to use [Animation.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Play.html) instead. SampleAnimation is useful when you need to jump between frames in an unordered way or based on some special input.  
  
Additional resources: [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html).  
  

* * *
