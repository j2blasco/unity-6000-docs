* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).color
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
Applies a global tint to the GUI. The tint affects backgrounds and text colors.
The tint is applied when Unity draws the content. It multiplies this property by the current color, and uses the resulting color to draw the content. **Note:** Because GUI.Color is a multiplier for the current text color, it has no effect on UI labels when you use the light Unity theme. In the light theme, the default color for label text is black, which has an RGB value of 0. Multiplying any GUI.Color value by 0 yields 0, so the label text color does not change. In the dark theme, the default label text color is white, which has an RGB value of 1, so whatever color you specify in GUI.color becomes the new label text color.
```
// Tints all GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) drawn elements with yellow.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 20), "Hello World!");
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 50, 50, 50), "A BOX");
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 110, 70, 30), "A button");
    }
}

```

* * *
