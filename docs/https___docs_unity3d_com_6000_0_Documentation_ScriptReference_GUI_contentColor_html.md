* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-contentColor.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).contentColor
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) contentColor; 
### Description
Tinting color for all text rendered by the GUI.
This gets multiplied by [color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html).  
  
Additional resources: [backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-backgroundColor.html), [color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUIContentColor.png)  
_Yellow content color (font) in a button._
```
// Tints with yellow the letters of the button.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUI.contentColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-contentColor.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 70, 30), "A button");
    }
}

```

* * *
