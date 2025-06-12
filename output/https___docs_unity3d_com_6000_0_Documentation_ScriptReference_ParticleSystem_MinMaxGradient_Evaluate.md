* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.Evaluate.html

#  [ParticleSystem.MinMaxGradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html).Evaluate
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
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Evaluate(float time); 
## Declaration
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Evaluate(float time, float lerpFactor); 
### Parameters
Parameter | Description  
---|---  
time | Normalized time (in the range 0 - 1, where 1 represents 100%) at which to evaluate the gradient. This is valid when [ParticleSystem.MinMaxGradient.mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-mode.html) is set to [ParticleSystemGradientMode.Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGradientMode.Gradient.html) or [ParticleSystemGradientMode.TwoGradients](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGradientMode.TwoGradients.html).  
lerpFactor | Blend between the two gradients/colors (Valid when [ParticleSystem.MinMaxGradient.mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-mode.html) is set to [ParticleSystemGradientMode.TwoColors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGradientMode.TwoColors.html) or [ParticleSystemGradientMode.TwoGradients](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGradientMode.TwoGradients.html)).  
### Returns
**Color** Calculated gradient/color value. 
### Description
Manually query the gradient to calculate colors based on what mode it is in.
This automatically clamps the time and lerpFactor properties between 0 and 1.
* * *
