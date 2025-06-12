* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.RGBToHSV.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).RGBToHSV
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
public static void RGBToHSV([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) rgbColor, out float H, out float S, out float V); 
### Parameters
Parameter | Description  
---|---  
rgbColor | An input color.  
H | Output variable for hue.  
S | Output variable for saturation.  
V | Output variable for value.  
### Description
Calculates the hue, saturation and value of an RGB input color.
The H, S, and V are output in the range 0.0 to 1.0.
```
using UnityEngine;  
  
// Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) an RGBA as an HSV  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        float H, S, V;  
  
        Color.RGBToHSV[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.RGBToHSV.html)(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.7f, 0.1f, 1.0F), out H, out S, out V);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("H: " + H + " S: " + S + " V: " + V);
    }
}

```

* * *
