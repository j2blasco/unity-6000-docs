* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.html

# MouseCursor
enumeration
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
Custom mouse cursor shapes used with EditorGUIUtility.AddCursorRect.
```
//Create a folder and name it “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” if this doesn’t already exist
//Put this script in the folder  
  
//This script creates a new menu (“Examples”) and a menu item (“Mouse Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)”). Click on this option. This displays a small window that has a color box in it.
//Hover over the colored box to cause an Orbit mouse cursor to appear.  
  

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
        EditorGUIUtility.AddCursorRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.AddCursorRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 140, 40), MouseCursor.Orbit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Orbit.html));
    }
}

```

### Properties
Property | Description  
---|---  
[Arrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Arrow.html) | Normal pointer arrow.  
[Text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Text.html) | Text cursor.  
[ResizeVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ResizeVertical.html) | Vertical resize arrows.  
[ResizeHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ResizeHorizontal.html) | Horizontal resize arrows.  
[Link](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Link.html) | Arrow with a Link badge (for assigning pointers).  
[SlideArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.SlideArrow.html) | Arrow with small arrows for indicating sliding at number fields.  
[ResizeUpRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ResizeUpRight.html) | Resize up-right for window edges.  
[ResizeUpLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ResizeUpLeft.html) | Resize up-Left for window edges.  
[MoveArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.MoveArrow.html) | Arrow with the move symbol next to it for the sceneview.  
[RotateArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.RotateArrow.html) | Arrow with the rotate symbol next to it for the sceneview.  
[ScaleArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ScaleArrow.html) | Arrow with the scale symbol next to it for the sceneview.  
[ArrowPlus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ArrowPlus.html) | Arrow with the plus symbol next to it.  
[ArrowMinus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.ArrowMinus.html) | Arrow with the minus symbol next to it.  
[Pan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Pan.html) | Cursor with a dragging hand for pan.  
[Orbit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Orbit.html) | Cursor with an eye for orbit.  
[Zoom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.Zoom.html) | Cursor with a magnifying glass for zoom.  
[FPS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.FPS.html) | Cursor with an eye and stylized arrow keys for FPS navigation.  
[CustomCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.CustomCursor.html) | The current user defined cursor.  
[SplitResizeUpDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.SplitResizeUpDown.html) | Up-Down resize arrows for window splitters.  
[SplitResizeLeftRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.SplitResizeLeftRight.html) | Left-Right resize arrows for window splitters.  
* * *
