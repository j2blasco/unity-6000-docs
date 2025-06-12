* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-r.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).r
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
r; 
### Description
Red component of the color.
The value ranges from 0 to 1.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) attached to it
//Use the sliders in Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html) to change the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) m_Renderer;
    //Set the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) to white to start off
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
    void Start()
    {
        //Fetch the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
    }  
  
    private void OnGUI()
    {
        //Sliders for the red, green and blue components of the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
        color.r = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 00, 100, 30), color.r, 0, 1);
        color.g = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 40, 100, 30), color.g, 0, 1);
        color.b = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 80, 100, 30), color.b, 0, 1);  
  
        //Set the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to the new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)
        m_Renderer.material.color = color;
    }
}

```

* * *
