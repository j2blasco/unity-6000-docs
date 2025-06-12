* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-colorSpace.html

#  [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).colorSpace
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
[ColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.html) colorSpace; 
### Description
Indicates the color space that the gradient color keys are using.
Color space setting is automatically set up by the gradient editor, based on [GradientUsageAttribute.colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-colorSpace.html) value.  
  
If you are creating gradients from C# code, this value needs to be set manually. Default value assumes that [colorKeys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-colorKeys.html) are expressed in [Gamma](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.Gamma.html) sRGB. Set this to [Linear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.Linear.html) if color keys are expressed as linear values.  
  
Currently only the [GradientMode.PerceptualBlend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientMode.PerceptualBlend.html) mode needs to know the color space; the value is ignored for other modes.
* * *
