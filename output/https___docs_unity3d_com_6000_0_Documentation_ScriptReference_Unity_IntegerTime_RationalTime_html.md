* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTime.html

# RationalTime
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
Data type that represents time as an integer count of a rational number.
### Properties
Property | Description  
---|---  
[Count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTime.Count.html) | Returns the number of ticks.  
[Ticks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTime.Ticks.html) | Returns the number of ticks per second.  
### Static Methods
Method | Description  
---|---  
[FromDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTime.FromDouble.html) | Converts a floating point number into a RationalTime with an explicit rate.  
### Operators
Operator | Description  
---|---  
[DiscreteTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTime-operator_DiscreteTime.html) | Converts a RationalTime to DiscreteTime representation. If the rate denominator is 1 and the DiscreteTime.TicksPerSecond is a multiple of the numerator, this conversion is lossless.  
* * *
