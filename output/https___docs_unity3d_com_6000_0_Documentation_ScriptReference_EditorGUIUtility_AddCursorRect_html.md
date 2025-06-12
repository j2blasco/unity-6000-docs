* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.AddCursorRect.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).AddCursorRect
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
public static void AddCursorRect([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [MouseCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.html) mouse); 
## Declaration
public static void AddCursorRect([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [MouseCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.html) mouse, int controlID); 
### Parameters
Parameter | Description  
---|---  
position | The rectangle the control should be shown within.  
mouse | The mouse cursor to use.  
controlID | ID of a target control.  
### Description
Add a custom mouse pointer to a control.
```
// Create a small window that has a color box in it.
// Hovering over it causes a Zoom mouse cursor to appear.  (The window is not
// zoomed however.)
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AddCursorRectExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/AddCursorRect Example")]
    static void addCursorRectExample()
    {
        AddCursorRectExample window =
            EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)<AddCursorRectExample>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 180, 80));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.DrawRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 160, 60), new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.5f, 0.5f, 0.85f));
        EditorGUI.DrawRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 140, 40), new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.9f));
        EditorGUIUtility.AddCursorRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.AddCursorRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 140, 40), MouseCursor.Zoom[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Zoom.html));
    }
}

```

* * *
