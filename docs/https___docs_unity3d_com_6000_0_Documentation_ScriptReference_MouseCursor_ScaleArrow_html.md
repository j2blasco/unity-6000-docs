* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ScaleArrow.html

#  [MouseCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.html).ScaleArrow
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
### Description
Arrow with the scale symbol next to it for the sceneview.
```
//Create a folder and name it “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” if this doesn’t already exist
//Put this script in the folder  
  
//This script creates a new menu (“Examples”) and a menu item (“Mouse Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)”). Click on this option. This displays a small window that has a color box in it.
//Hover over the colored box to cause a ScaleArrow mouse cursor to appear.  
  

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MouseCursorExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/MouseCursorRect Example")]
    static void AddCursorRectExample()
    {
        MouseCursorExample window =
            EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)<MouseCursorExample>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 180, 80));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.DrawRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 160, 60), new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.5f, 0.5f, 0.85f));
        EditorGUI.DrawRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 140, 40), new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.9f, 0.9f, 0.9f));
        EditorGUIUtility.AddCursorRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.AddCursorRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 140, 40), MouseCursor.ScaleArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ScaleArrow.html));
    }
}

```

* * *
