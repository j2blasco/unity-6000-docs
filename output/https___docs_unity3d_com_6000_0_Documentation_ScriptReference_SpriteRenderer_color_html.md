* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-color.html

#  [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html).color
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color; 
### Description
Rendering color for the Sprite graphic.
The selected vertex color becomes the rendering color, and is accessible in a pixel shader. The default color is white when no color is selected.
```
//This example outputs Sliders that control the red green and blue elements of a sprite's color
//Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach a SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) component  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) m_SpriteRenderer;
    //The Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) to be assigned to the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)’s Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_NewColor;  
  
    //These are the values that the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Sliders return
    float m_Red, m_Blue, m_Green;  
  
    void Start()
    {
        //Fetch the SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_SpriteRenderer = GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        //Set the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) quickly to a set Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) (blue)
        m_SpriteRenderer.color = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
    }  
  
    void OnGUI()
    {
        //Use the Sliders to manipulate the RGB component of Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
        //Use the Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) to identify the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 30, 50, 30), "Red: ");
        //Use the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) to change amount of red in the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
        m_Red = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(35, 25, 200, 30), m_Red, 0, 1);  
  
        //The Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) manipulates the amount of green in the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 70, 50, 30), "Green: ");
        m_Green = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(35, 60, 200, 30), m_Green, 0, 1);  
  
        //This Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) decides the amount of blue in the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 105, 50, 30), "Blue: ");
        m_Blue = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(35, 95, 200, 30), m_Blue, 0, 1);  
  
        //Set the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) to the values gained from the Sliders
        m_NewColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(m_Red, m_Green, m_Blue);  
  
        //Set the SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) to the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) defined by the Sliders
        m_SpriteRenderer.color = m_NewColor;
    }
}

```

* * *
