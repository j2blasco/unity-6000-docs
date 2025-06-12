* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.Evaluate.html

#  [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).Evaluate
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
## Declaration
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Evaluate(float time); 
### Parameters
Parameter | Description  
---|---  
time | Time of the evaluation (0 - 1).  
### Description
Calculate color at a given time.
Gradient color and alpha keys are blended and interpolated depending on the gradient [mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-mode.html).  
  
Unity clamps the colors and alpha if you use a value for `time` that's smaller than `0` or larger than `1`.   
  
Additional resources: [mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-mode.html), [GradientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientMode.html), [SetKeys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.SetKeys.html).
* * *
