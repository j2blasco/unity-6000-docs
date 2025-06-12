* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.html

# BaseAnimValue<T0>
class in UnityEditor.AnimatedValues
Leave feedback
  

Implements interfaces:[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)
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
Abstract base class for Animated Values.
Animated Values are an editor only concept for values that have a current value and a target. The value will tween towards the target at a given speed.
### Properties
Property | Description  
---|---  
[isAnimating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1-isAnimating.html) | Is the value currently animating.  
[speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1-speed.html) | Speed of the tween.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1-target.html) | Target to tween towards.  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1-value.html) | Current value of the animation.  
[valueChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1-valueChanged.html) | Callback while the value is changing.  
### Protected Methods
Method | Description  
---|---  
[BeginAnimating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.BeginAnimating.html) | Begin an animation moving from the start value to the target value.  
[GetValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.GetValue.html) | Abstract function to be overridden in derived types. Should return the current value of the animated value.  
[StopAnim](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.StopAnim.html) | Stop the animation and assign the given value.  
* * *
