* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-ctor.html

# ParticleSystem.MinMaxGradient Constructor
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
public ParticleSystem.MinMaxGradient([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color); 
### Parameters
Parameter | Description  
---|---  
color | Constant color.  
### Description
A single constant color for the entire gradient.
* * *
## Declaration
public ParticleSystem.MinMaxGradient([Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient); 
### Parameters
Parameter | Description  
---|---  
gradient | A single gradient for evaluating against.  
### Description
Use one gradient when evaluating numbers along this Min-Max Gradient.
* * *
## Declaration
public ParticleSystem.MinMaxGradient([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) min, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) max); 
### Parameters
Parameter | Description  
---|---  
min | The constant color describing the minimum colors to be evaluated.  
max | The constant color describing the maximum colors to be evaluated.  
### Description
Randomly select colors based on the interval between the minimum and maximum constants.
* * *
## Declaration
public ParticleSystem.MinMaxGradient([Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) min, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) max); 
### Parameters
Parameter | Description  
---|---  
min | The gradient describing the minimum colors to be evaluated.  
max | The gradient describing the maximum colors to be evaluated.  
### Description
Randomly select colors based on the interval between the minimum and maximum gradients.
* * *
