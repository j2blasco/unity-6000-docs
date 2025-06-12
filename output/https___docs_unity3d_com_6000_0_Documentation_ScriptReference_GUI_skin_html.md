* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-skin.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).skin
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
[GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) skin; 
### Description
The global skin to use.
You can set this at any point to change the look of your GUI. If you set it to null, the skin will revert to the default Unity skin.
```
// Press space to change between added GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) skins.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GUISkin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html)[] s1;  
  
    private float hSliderValue = 0.0F;
    private float vSliderValue = 0.0F;
    private float hSValue = 0.0F;
    private float vSValue = 0.0F;
    private int cont = 0;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            cont++;
        }
    }  
  
    void OnGUI()
    {
        GUI.skin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-skin.html) = s1[cont % s1.Length];  
  
        if (s1.Length == 0)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Assign at least 1 skin on the array");
            return;
        }  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 20), "Hello World!");
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 50, 50, 50), "A BOX");  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 110, 70, 30), "A button"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) has been pressed");
        }  
  
        hSliderValue = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 150, 100, 30), hSliderValue, 0.0F, 10.0F);
        vSliderValue = GUI.VerticalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 170, 100, 30), vSliderValue, 10.0F, 0.0F);
        hSValue = GUI.HorizontalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalScrollbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 210, 100, 30), hSValue, 1.0F, 0.0F, 10.0F);
        vSValue = GUI.VerticalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalScrollbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 230, 100, 30), vSValue, 1.0F, 10.0F, 0.0F);
    }
}

```

* * *
