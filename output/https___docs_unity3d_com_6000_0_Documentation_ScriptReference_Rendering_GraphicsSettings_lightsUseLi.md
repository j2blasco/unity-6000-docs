* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).lightsUseLinearIntensity
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
lightsUseLinearIntensity; 
### Description
If this is true, Light intensity is multiplied against linear color values. If it is false, gamma color values are used.
Light intensity is multiplied by the linear color value when lightsUseLinearIntensity is enabled. This is physically correct but not the default for 3D projects created with Unity 5.6 and newer. By default [lightsUseLinearIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html) is set to false.  
  
2D projects will have [lightsUseLinearIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html) set to disabled by default. When disabled, the gamma color value is multiplied with the intensity. If you want to use [lightsUseColorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseColorTemperature.html), [lightsUseLinearIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html) has to be enabled.  
  
If you enable [lightsUseLinearIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html) on an existing project, all your Lights will need to be tweaked to regain their original look.  
  
Additional resources: [GraphicsSettings.lightsUseColorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseColorTemperature.html), [Light.colorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-colorTemperature.html). 
* * *
