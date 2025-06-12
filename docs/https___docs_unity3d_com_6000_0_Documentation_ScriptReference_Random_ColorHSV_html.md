* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.ColorHSV.html

#  [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html).ColorHSV
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html "Go to Random Component in the Manual")
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorHSV(); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorHSV(float hueMin, float hueMax); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorHSV(float hueMin, float hueMax, float saturationMin, float saturationMax); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorHSV(float hueMin, float hueMax, float saturationMin, float saturationMax, float valueMin, float valueMax); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorHSV(float hueMin, float hueMax, float saturationMin, float saturationMax, float valueMin, float valueMax, float alphaMin, float alphaMax); 
### Parameters
Parameter | Description  
---|---  
hueMin | Minimum hue [0..1].  
hueMax | Maximum hue [0..1].  
saturationMin | Minimum saturation [0..1].  
saturationMax | Maximum saturation [0..1].  
valueMin | Minimum value [0..1].  
valueMax | Maximum value [0..1].  
alphaMin | Minimum alpha [0..1].  
alphaMax | Maximum alpha [0..1].  
### Returns
**Color** A random color with HSV and alpha values in the (inclusive) input ranges. Values for each component are derived via linear interpolation of [value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html). 
### Description
Generates a random color from HSV and alpha ranges.
```
using UnityEngine;  
  
public class ColorOnClick : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnMouseDown()
    {
        // Pick a random, saturated and not-too-dark color
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.color = Random.ColorHSV[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.ColorHSV.html)(0f, 1f, 1f, 1f, 0.5f, 1f);
    }
}

```

* * *
