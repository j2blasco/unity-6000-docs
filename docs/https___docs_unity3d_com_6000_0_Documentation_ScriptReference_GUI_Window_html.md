* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).Window
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
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, string text); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) title, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
Style | An optional style to use for the window. If left out, the `window` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
id | ID number for the window (can be any value as long as it is unique).  
clientRect | Onscreen rectangle denoting the window's position and size.  
func | Script function to display the window's contents.  
text | Text to render inside the window.  
image | Image to render inside the window.  
content | GUIContent to render inside the window.  
style | Style information for the window.  
title | Text displayed in the window's title bar.  
### Returns
**Rect** Onscreen rectangle denoting the window's position and size. 
### Description
Make a popup window.
Windows float above normal GUI controls, feature click-to-focus and can optionally be dragged around by the end user. Unlike other controls, you need to pass them a separate function that renders the GUI controls inside the window.  
  
**Note:** If you are using [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) to place your components inside the window, you should use [GUILayout.Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html). Also, if [MonoBehaviour.useGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour-useGUILayout.html) is set to false then a call to GUI.Window will not have any effect, even though it is not a GUILayout function.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);  
  
    void OnGUI()
    {
        // Register the window. Notice the 3rd parameter
        windowRect = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, windowRect, DoMyWindow, "My Window");
    }  
  
    // Make the contents of the window
    void DoMyWindow(int windowID)
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 20, 100, 20), "Hello World"))
        {
            print("Got a click");
        }
    }
}

```

You can use the same function to create multiple windows. Just make sure that _each window has its own ID_. Example:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect0 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect1 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 100, 120, 50);  
  
    void OnGUI()
    {
        // Register the window. We create two windows that use the same function
        // Notice that their IDs differ
        windowRect0 = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, windowRect0, DoMyWindow, "My Window");
        windowRect1 = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(1, windowRect1, DoMyWindow, "My Window");
    }  
  
    // Make the contents of the window
    void DoMyWindow(int windowID)
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 20, 100, 20), "Hello World"))
        {
            print("Got a click in window " + windowID);
        }  
  
        // Make the windows be draggable.
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 10000, 10000));
    }
}

```

To stop showing a window, simply stop calling GUI.Window from inside your main OnGUI function:
```
// boolean variable to decide whether to show the window or not.
// Change this from the in-game GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html), scripting, the inspector or anywhere else to
// decide whether the window is visible  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public bool doWindow0 = true;  
  
    // Make the contents of the window.
    void DoWindow0(int windowID)
    {
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 80, 20), "Click Me!");
    }  
  
    void OnGUI()
    {
        // Make a toggle button for hiding and showing the window
        doWindow0 = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 20), doWindow0, "Window 0");  
  
        // Make sure we only call GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) if doWindow0 is true.
        if (doWindow0)
        {
            GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(110, 10, 200, 60), DoWindow0, "Basic Window");
        }
    }
}

```

To make a window that gets its size from automatic GUI layouting, use [GUILayout.Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html). **Call Ordering** Windows need to be drawn back-to-front; windows on top of other windows need to be drawn later than the ones below them. This means that you can not count on your DoWindow functions to be called in any particular order. In order for this to work seamlessly, the following values are stored when you create your window (using the **Window** function), and retrieved when your DoWindow gets called: [GUI.skin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-skin.html), [GUI.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html), [GUI.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html), [GUI.backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-backgroundColor.html), [GUI.contentColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-contentColor.html), [GUI.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect0 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect1 = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 100, 120, 50);  
  
    void OnGUI()
    {
        // Here we make 2 windows. We set the GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) value to something before each.
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        windowRect0 = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(0, windowRect0, DoMyWindow, "Red Window");  
  
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
        windowRect1 = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)(1, windowRect1, DoMyWindow, "Green Window");
    }  
  
    // Make the contents of the window.
    // The value of GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) is set to what it was when the window
    // was created in the code above.
    void DoMyWindow(int windowID)
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 20, 100, 20), "Hello World"))
        {
            print("Got a click in window with color " + GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html));
        }  
  
        // Make the windows be draggable.
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 10000, 10000));
    }
}

```

Note that you can use the alpha component of [GUI.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) to fade windows in and out.  
  
Additional resources: [DragWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html), [BringWindowToFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToFront.html), [BringWindowToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html).
* * *
