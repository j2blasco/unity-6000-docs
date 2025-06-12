* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.CorrelatedColorTemperatureToRGB.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).CorrelatedColorTemperatureToRGB
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) CorrelatedColorTemperatureToRGB(float kelvin); 
### Parameters
Parameter | Description  
---|---  
kelvin | Temperature in Kelvin. Range 1000 to 40000 Kelvin.  
### Returns
**Color** Correlated Color Temperature as floating point RGB color. 
### Description
Convert a color temperature in Kelvin to RGB color.
Given a correlated color temperature (in Kelvin), estimate the RGB equivalent. Curve fit error is max 0.008.  
  
Correlated color temperature is defined as the color temperature of the electromagnetic radiation emitted from an ideal black body with its surface temperature given in degrees Kelvin.  
  
Temperature must fall between 1000 and 40000 degrees.
* * *
