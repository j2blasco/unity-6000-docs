* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-enableSpotReflector.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).enableSpotReflector
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
enableSpotReflector; 
### Description
Wether a Spot Light should simulate having a reflector.
When enabled, indicates that the Spot Light intensity should be simulated using a reflector. This means the narrower the Outer Angle, the more intense the Spot Light. When disabled, the intensity of the Light should match that of a Point Light and thus remains constant regardless of the Outer Angle. Only relevant for Spot Lights measued in [LightUnit.Lumen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightUnit.Lumen.html). Only Scriptable Render Pipelines use this property; the built-in renderer does not support it.  
  
Additional resources: [LightUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightUnit.html), [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html).
* * *
