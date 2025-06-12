* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.HSVToRGB.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).HSVToRGB
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
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) HSVToRGB(float H, float S, float V); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) HSVToRGB(float H, float S, float V, bool hdr); 
### Parameters
Parameter | Description  
---|---  
H | Hue [0..1].  
S | Saturation [0..1].  
V | Brightness value [0..1].  
hdr | Output HDR colours. If true, the returned colour will not be clamped to [0..1].  
### Returns
**Color** An opaque colour with HSV matching the input. 
### Description
Creates an RGB colour from HSV input.
Creates an RGB color from the hue, saturation and value of the input.
```
//Create three Sliders ( **Create**>**UI**>**Slider**)
//These are for manipulating the hue, saturation and value levels of the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).  
  
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Make sure it has a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component.
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach each of the Sliders and Texts to the fields in the Inspector.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class ColorHSVtoRGBExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float m_Hue;
    float m_Saturation;
    float m_Value;
    //These are the Sliders that control the values. Remember to attach them in the Inspector window.
    public Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) m_SliderHue, m_SliderSaturation, m_SliderValue;  
  
    //Make sure your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component in the Inspector window
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) m_Renderer;  
  
    void Start()
    {
        //Fetch the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached
        m_Renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
        //Set the maximum and minimum values for the Sliders
        m_SliderHue.maxValue = 1;
        m_SliderSaturation.maxValue = 1;
        m_SliderValue.maxValue = 1;  
  
        m_SliderHue.minValue = 0;
        m_SliderSaturation.minValue = 0;
        m_SliderValue.minValue = 0;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //These are the Sliders that determine the amount of the hue, saturation and value in the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
        m_Hue = m_SliderHue.value;
        m_Saturation = m_SliderSaturation.value;
        m_Value = m_SliderValue.value;  
  
        //Create an RGB color from the HSV values from the Sliders
        //Change the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
        m_Renderer.material.color = Color.HSVToRGB[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.HSVToRGB.html)(m_Hue, m_Saturation, m_Value);
    }
}

```

* * *
