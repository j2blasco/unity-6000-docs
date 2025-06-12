* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseColorTemperature.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).lightsUseColorTemperature
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
lightsUseColorTemperature; 
### Description
Whether to use a Light's color temperature when calculating the final color of that Light."
Enable to use the correlated color temperature (abbreviated as CCT) for adjusting light color. CCT is a natural way to set light color based on the physical properties of the light source. The CCT is multiplied with the color filter when calculating the final color of a light source. The color temperature of the electromagnetic radiation emitted from an ideal black body is defined as its surface temperature in degrees Kelvin. White is 6500K according to the D65 standard. A candle light is 1800K and a soft warm light bulb is 2700K. If you want to use lightsUseColorTemperature, lightsUseLinearIntensity has to be enabled to ensure physically correct output.  
  
Additional resources: [GraphicsSettings.lightsUseLinearIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html), [[Light.useColorTemperature], [Light.colorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-colorTemperature.html). 
* * *
