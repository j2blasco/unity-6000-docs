* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).MinHeight
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
public static [GUILayoutOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutOption.html) MinHeight(float minHeight); 
### Description
Option passed to a control to specify a minimum height.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutMinHeight.png)   
_Minimum height for a window._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a window you can resize between 80px and 200px height
    // Just click the box inside the window and move your mouse
    Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100);
    bool scaling = false;  
  
    void OnGUI()
    {
        windowRect = GUILayout.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html)(0, windowRect, ScalingWindow, "resizeable",
            GUILayout.MinHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html)(80), GUILayout.MaxHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html)(200));
    }  
  
    void ScalingWindow(int windowID)
    {
        GUILayout.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Box.html)("", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(20), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(20));
        if (Event.current.type == EventType.MouseUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html))
        {
            scaling = false;
        }
        else if (Event.current.type == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html) &&
                 GUILayoutUtility.GetLastRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetLastRect.html)().Contains(Event.current.mousePosition))
        {
            scaling = true;
        }  
  
        if (scaling)
        {
            windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(windowRect.x, windowRect.y,
                windowRect.width + Event.current.delta.x, windowRect.height + Event.current.delta.y);
        }
    }
}

```

* * *
