* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.Evaluate.html

#  [ParticleSystem.MinMaxCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html).Evaluate
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
public float Evaluate(float time); 
## Declaration
public float Evaluate(float time, float lerpFactor); 
### Parameters
Parameter | Description  
---|---  
time | Normalized time (in the range 0 - 1, where 1 represents 100%) at which to evaluate the curve. This is valid when [ParticleSystem.MinMaxCurve.mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve-mode.html) is set to [ParticleSystemCurveMode.Curve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCurveMode.Curve.html) or [ParticleSystemCurveMode.TwoCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCurveMode.TwoCurves.html).  
lerpFactor | Blend between the two curves/constants (Valid when [ParticleSystem.MinMaxCurve.mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve-mode.html) is set to [ParticleSystemCurveMode.TwoConstants](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCurveMode.TwoConstants.html) or [ParticleSystemCurveMode.TwoCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCurveMode.TwoCurves.html)).  
### Returns
**float** Calculated curve/constant value. 
### Description
Manually query the curve to calculate values based on what mode it is in.
This automatically clamps the time and lerpFactor properties between 0 and 1.
* * *
