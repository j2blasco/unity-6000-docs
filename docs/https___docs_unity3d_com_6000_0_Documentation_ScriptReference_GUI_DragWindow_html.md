* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).DragWindow
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
public static void DragWindow([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The part of the window that can be dragged. This is clipped to the actual window.  
### Description
Make a window draggable.
Insert a call to this function inside your window code to make a window draggable.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);  
  
    void OnGUI()
    {
        // Register the window.
        windowRect = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, windowRect, DoMyWindow, "My Window");
    }  
  
    // Make the contents of the window
    void DoMyWindow(int windowID)
    {
        // Make a very long rect that is 20 pixels tall.
        // This will make the window be resizable by the top
        // title bar - no matter how wide it gets.
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 10000, 20));
    }
}

```

* * *
## Declaration
public static void DragWindow(); 
### Description
If you want to have the entire window background to act as a drag area, use the version of DragWindow that takes no parameters and put it at the end of the window function.
This will mean that any other controls will get precedence and the dragging will only be activated if nothing else has mouse focus. Additional resources: [DragWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html), [BringWindowToFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToFront.html), [BringWindowToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);  
  
    void OnGUI()
    {
        windowRect = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, windowRect, DoMyWindow, "My Window");
    }  
  
    // Make the contents of the window
    void DoMyWindow(int windowID)
    {
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 20, 100, 20), "Can't drag me");
        // Insert a huge dragging area at the end.
        // This gets clipped to the window (like all other controls) so you can never
        //  drag the window from outside it.
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 10000, 20));
    }
}

```

* * *
