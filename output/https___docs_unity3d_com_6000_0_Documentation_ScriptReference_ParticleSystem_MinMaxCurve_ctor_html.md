* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve-ctor.html

# ParticleSystem.MinMaxCurve Constructor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
## Declaration
public ParticleSystem.MinMaxCurve(float constant); 
### Parameters
Parameter | Description  
---|---  
constant | Constant value.  
### Description
A single constant value for the entire curve.
* * *
## Declaration
public ParticleSystem.MinMaxCurve(float multiplier, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve); 
### Parameters
Parameter | Description  
---|---  
scalar | A multiplier to apply to the curve.  
curve | A single curve to evaluate against.  
### Description
Use one curve when evaluating numbers along this Min-Max curve.
* * *
## Declaration
public ParticleSystem.MinMaxCurve(float multiplier, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) min, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) max); 
### Parameters
Parameter | Description  
---|---  
scalar | A multiplier to apply to the curves.  
min | The curve describing the minimum values to be evaluated.  
max | The curve describing the maximum values to be evaluated.  
### Description
Randomly select values based on the interval between the minimum and maximum curves.
* * *
## Declaration
public ParticleSystem.MinMaxCurve(float min, float max); 
### Parameters
Parameter | Description  
---|---  
min | The constant describing the minimum values to be evaluated.  
max | The constant describing the maximum values to be evaluated.  
### Description
Randomly select values based on the interval between the minimum and maximum constants.
* * *
