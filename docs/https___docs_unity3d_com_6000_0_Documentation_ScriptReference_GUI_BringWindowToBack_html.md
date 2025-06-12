* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).BringWindowToBack
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
public static void BringWindowToBack(int windowID); 
### Parameters
Parameter | Description  
---|---  
windowID | The identifier used when you created the window in the [Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) call.  
### Description
Bring a specific window to back of the floating windows.
```
// Draws 2 overlapped windows and when clicked on 1 window's button
// Brings the window to the back.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect2 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(80, 20, 120, 50);
    void OnGUI()
    {
        windowRect = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, windowRect, DoMyFirstWindow, "First");
        windowRect2 = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(1, windowRect2, DoMySecondWindow, "Second");
    }  
  
    void DoMyFirstWindow(int windowID)
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 20, 100, 20), "Put Back"))
            GUI.BringWindowToBack[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html)(0);  
  
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 10000, 20));
    }  
  
    void DoMySecondWindow(int windowID)
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 20, 100, 20), "Put Back"))
            GUI.BringWindowToBack[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html)(1);  
  
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 10000, 20));
    }
}

```

* * *
