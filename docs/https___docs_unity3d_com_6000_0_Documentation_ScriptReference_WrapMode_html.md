* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.html

# WrapMode
enumeration
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
### Description
Determines how time is treated outside of the keyframed range of an [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) or [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).
The WrapMode that the animation system uses for a specific animation is determined this way:  
You can set the WrapMode of an [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) in the import settings of the clip. This is the recommended way to control the WrapMode.  
When an [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) is created, it inherits its WrapMode from the [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) it is created from, but you can also change it from code.  
If the WrapMode of an [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) is set to Default, the animation system will use the WrapMode from the [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) component.
### Properties
Property | Description  
---|---  
[Once](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.Once.html) | When time reaches the end of the animation clip, the clip will automatically stop playing and time will be reset to beginning of the clip.  
[Loop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.Loop.html) | When time reaches the end of the animation clip, time will continue at the beginning.  
[PingPong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.PingPong.html) | When time reaches the end of the animation clip, time will ping pong back between beginning and end.  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.Default.html) | Reads the default repeat mode set higher up.  
[ClampForever](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.ClampForever.html) | Plays back the animation. When it reaches the end, it will keep playing the last frame and never stop playing.  
* * *
