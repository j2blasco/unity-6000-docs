* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html

# SphericalHarmonicsL2
struct in UnityEngine.Rendering
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
Spherical harmonics up to the second order (3 bands, 9 coefficients).
Spherical harmonics (SH) represent a function or signal over directions, and are commonly used in computer graphics to efficiently evaluate smooth lighting. Unity uses them for [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html) and environment lighting.  
  
L2 spherical harmonics is composed of 9 coefficients for each color channel.  
  
Additional resources: [RenderSettings.ambientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientMode.html), [RenderSettings.ambientProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientProbe.html), [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).
### Properties
Property | Description  
---|---  
[this[int,int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.Index_operator.html) | Access individual SH coefficients.  
### Public Methods
Method | Description  
---|---  
[AddAmbientLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.AddAmbientLight.html) | Add an ambient light to the spherical harmonics.  
[AddDirectionalLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.AddDirectionalLight.html) | Add a directional light to the spherical harmonics.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.Clear.html) | Clears the spherical harmonics coefficients to zero.  
[Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.Evaluate.html) | Evaluates the spherical harmonics for each given direction. The directions and results arrays must have the same size.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2-operator_ne.html) | Returns true if the spherical harmonics are different.  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2-operator_multiply.html) | Scales SH by a given factor.  
[operator +](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2-operator_add.html) | Adds two spherical harmonics.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2-operator_eq.html) | Returns true if the spherical harmonics are equal.  
* * *
