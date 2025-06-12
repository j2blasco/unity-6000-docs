* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.CrossFade.html

#  [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html).CrossFade
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html "Go to Animation Component in the Manual")
## Declaration
public void CrossFade(string animation, float fadeLength = 0.3F, [PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) mode = PlayMode.StopSameLayer); 
### Description
Fades in the animation with the name `animation` over a period of time defined by `fadeLength`.
If the mode is set to [PlayMode.StopSameLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.StopSameLayer.html), animations on the same layer as `animation` are faded out while `animation` is faded in. if the mode is set to [PlayMode.StopAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.StopAll.html), all animations are out while `animation` is faded in.  
  
If the animation is not set to be looping, it will be stopped and rewound after playing.  
  

* * *
