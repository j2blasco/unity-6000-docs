* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.InverseSquaredNoRangeAttenuation.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [FalloffType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html).InverseSquaredNoRangeAttenuation
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
Inverse squared distance falloff model (without smooth range attenuation).
This is a physically based falloff model for point and spot lights. The falloff model falls off with the inverse squared distance between the light and the point being shaded. This means that observed light is very bright when the surface is close to the light and falls off rapidly as the distance increases.  
  
This is fundamentally different from non physically based falloff models. When switching to this falloff model the intensity takes on a physical unit and a much higher value is typically needed in order to see the effect of the light. A light with 1 lumens is **very** dim.  
  
The distance is in Unity units (metric: 1 = 1m). The falloff is only defined within the range of the light and **sharply** falls off to zero at the light range. Please use [FalloffType.InverseSquared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.InverseSquared.html) if you observe artifacts due to the sharp cutoff at the light range. The minimum distance used for the calculation is 1cm in order to avoid numerical issues.
* * *
