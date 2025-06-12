* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValueNonAlloc_1.html

# BaseAnimValueNonAlloc<T0>
class in UnityEditor.AnimatedValues
/
Inherits from:[AnimatedValues.BaseAnimValue_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.html)
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
Abstract base class that provides an allocation free version of BaseAnimValue.
Abstract base class that provides an allocation free version of BaseAnimValue. See BaseAnimValue.
### Inherited Members
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
