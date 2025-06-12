* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html

# AnimationState
class in UnityEngine
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
The AnimationState gives full control over animation blending.
In most cases the [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) interface is sufficient and easier to use. Use the AnimationState if you need full control over the animation blending any playback process.  
  
The AnimationState interface allows you to modify speed, weight, time and layers while any animation is playing. You can also setup animation mixing and wrapMode.  
  
The Animation.
### Properties
Property | Description  
---|---  
[blendMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-blendMode.html) | Which blend mode should be used?  
[clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-clip.html) | The clip that is being played by this animation state.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-enabled.html) | Enables / disables the animation.  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-length.html) | The length of the animation clip in seconds.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-name.html) | The name of the animation.  
[normalizedSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-normalizedSpeed.html) | The normalized playback speed.  
[normalizedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-normalizedTime.html) | Normalized time of the State.  
[speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-speed.html) | The playback speed of the animation. 1 is normal playback speed.  
[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-time.html) | The current time of the animation.  
[weight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-weight.html) | The weight of animation.  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-wrapMode.html) | Wrapping mode of the animation.  
### Public Methods
Method | Description  
---|---  
[AddMixingTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.AddMixingTransform.html) | Adds a transform which should be animated. This allows you to reduce the number of animations you have to create.  
[RemoveMixingTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.RemoveMixingTransform.html) | Removes a transform which should be animated.  
* * *
