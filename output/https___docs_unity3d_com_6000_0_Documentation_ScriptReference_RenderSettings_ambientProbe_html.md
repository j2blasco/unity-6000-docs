* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientProbe.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).ambientProbe
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
[Rendering.SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) ambientProbe; 
### Description
An ambient probe that captures environment lighting.
Unity generates the ambient probe when you generate lighting for a scene. If you haven't yet generated lighting in a scene, Unity uses a default ambient probe that matches the default skybox instead. Unity uses the ambient probe to make sure environment lighting affects your scene and the GameObjects in it by default.  
  
Unity does not use this probe to affect GameObjects that you manually associate with Light Probes and light maps in the Global Illumination system. This is because manually generated Light Probes and light maps include an environment contribution by default.  
  
As a result, adjusting this automatically generated ambient probe does not affect Enlighten Realtime Global Illumination and Baked Global Illumination lighting results. If you want to affect Global Illumination values with this ambient probe, select an [AmbientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AmbientMode.html) and make any manual adjustments needed to use that mode.  
  
Additional resources: [ambientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientMode.html), [SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html), [The Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html).
* * *
