* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool.html

# AnimBool
class in UnityEditor.AnimatedValues
/
Inherits from:[AnimatedValues.BaseAnimValueNonAlloc_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValueNonAlloc_1.html)
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
Lerp from 0 - 1.
When value is 0 returns false, when value > 0.5 returns true. Animated using [Mathf.Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html).
### Properties
Property | Description  
---|---  
[faded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool-faded.html) | Retuns the float value of the tween.  
### Constructors
Constructor | Description  
---|---  
[AnimBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[Fade](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool.Fade.html) | Returns a value between from and to depending on the current value of the bools animation.  
### Protected Methods
Method | Description  
---|---  
[GetValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool.GetValue.html) | Type specific implementation of BaseAnimValue_1.GetValue.  
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
[StopAnim](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.StopAnim.html) | Stop the animation and assign the given value.  
* * *
