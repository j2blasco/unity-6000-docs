* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.EndWindows.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).EndWindows
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
public void EndWindows(); 
### Description
Close a window group started with [EditorWindow.BeginWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.BeginWindows.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUIWindowDemo.png)   
_Simple editor Window with a window and a button inside._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;

public class IMGUIWindowDemo : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // The position of the window
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 200, 200);
    void OnGUI()
    {
        BeginWindows();

        // All GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) or GUILayout.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html) must come inside here
        windowRect = GUILayout.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html)(1, windowRect, DoWindow, "Hi There");

        EndWindows();
    }

    // The window function. This works just like ingame GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)
    void DoWindow(int unusedWindowID)
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Hi");
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)();
    }

    // Add menu item to show this demo.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/GUIWindow Demo")]
    static void Init()
    {
        EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(IMGUIWindowDemo));
    }
}

```

The placement of the [BeginWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.BeginWindows.html) / [EndWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.EndWindows.html) pair determines where popup windows will appear; all windows are clipped to the clipping area defined by [GUI.BeginGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html) or [GUI.BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html). A small example of that:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUIWindowDemo2.png)  
_Simple editor window with a window and a button inside using scroll bars._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;

public class IMGUIWindowDemo2 : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // The position of the window
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 200, 200);

    // Scroll position
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPos = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);

    void OnGUI()
    {
        // Set up a scroll view
        scrollPos = GUI.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, position.width, position.height), scrollPos, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 1000, 1000));

        // Same code as before - make a window. Only now, it's INSIDE the scrollview
        BeginWindows();
        windowRect = GUILayout.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html)(1, windowRect, DoWindow, "Hi There");
        EndWindows();
        // Close the scroll view
        GUI.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndScrollView.html)();
    }

    void DoWindow(int unusedWindowID)
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Hi");
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)();
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/GUIWindow Demo 2")]
    static void Init()
    {
        EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(IMGUIWindowDemo2));
    }
}

```

* * *
