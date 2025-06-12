* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalSlider.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).VerticalSlider
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
public static float VerticalSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float topValue, float bottomValue); 
## Declaration
public static float VerticalSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float topValue, float bottomValue, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) slider, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) thumb); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the slider.  
value | The value the slider shows. This determines the position of the draggable thumb.  
topValue | The value at the top end of the slider.  
bottomValue | The value at the bottom end of the slider.  
slider | The [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for displaying the dragging area. If left out, the `horizontalSlider` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
thumb | The [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for displaying draggable thumb. If left out, the `horizontalSliderThumb` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**float** The value that has been set by the user. 
### Description
A vertical slider the user can drag to change a value between a min and a max.
```
// Draws a vertical slider control that goes from  10 (top) to 0 (bottom)  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float vSliderValue = 0.0f;  
  
    void OnGUI()
    {
        vSliderValue = GUI.VerticalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 100, 30), vSliderValue, 10.0f, 0.0f);
    }
}

```

* * *
