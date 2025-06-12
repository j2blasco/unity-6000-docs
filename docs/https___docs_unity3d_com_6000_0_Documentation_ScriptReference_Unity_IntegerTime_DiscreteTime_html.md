* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.html

# DiscreteTime
struct in Unity.IntegerTime
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Data-type representing a discrete time value.
### Static Properties
Property | Description  
---|---  
[MaxValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.MaxValue.html) | The maximum representable time.  
[MaxValueSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.MaxValueSeconds.html) | The maximum representable time in seconds.  
[MinValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.MinValue.html) | The minimum representable time.  
[MinValueSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.MinValueSeconds.html) | The minimum representable time in seconds.  
[Tick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.Tick.html) | The duration in seconds of a tick (the smallest representable unit of time).  
[Zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.Zero.html) | The zero value.  
### Properties
Property | Description  
---|---  
[Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.Value.html) | The underlying discrete time value, which represents the number of discrete ticks.  
### Constructors
Constructor | Description  
---|---  
[DiscreteTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-ctor.html) | Constructs a discrete time from either seconds (float/double) or ticks (int/long).  
### Public Methods
Method | Description  
---|---  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.ToString.html) | Returns a string representation of the time.  
### Static Methods
Method | Description  
---|---  
[FromTicks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.FromTicks.html) | Explicitly converts a tick value to a DiscreteTime value.  
### Operators
Operator | Description  
---|---  
[operator -](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_subtract.html) | Returns the substraction of two time values.  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_ne.html) | Returns whether two time values are different.  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_multiply.html) | Returns the multiplication of two time values.  
[operator /](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_divide.html) | A time value divided by a floating point amount.  
[operator +](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_add.html) | Returns the addition of two time values.  
[operator <](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_lt.html) | Returns whether the left-hand time value is less than the right-hand one.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_eq.html) | Returns true if the time is equal to a given time, false otherwise.  
[operator >](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_gt.html) | Returns whether left-hand time value is greater than the right-hand one.  
[RationalTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_DiscreteTime.html) | Converts a DiscreteTime to a RationalTime representation. This conversion is always lossless.  
[Unknown operator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_.html) | Returns whether the left-hand time value is less than or equal to the right-hand one.  
[Unknown operator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_.html) | Returns whether the left-hand time value is greater than or equal to the right-hand one.  
[Unknown operator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime-operator_.html) | Returns the modulus of two time values.  
* * *
