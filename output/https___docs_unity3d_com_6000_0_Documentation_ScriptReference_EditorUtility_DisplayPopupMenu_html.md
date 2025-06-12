* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayPopupMenu.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).DisplayPopupMenu
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
public static void DisplayPopupMenu([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string menuItemPath, [MenuCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) command); 
### Description
Displays a popup menu.
Menu is shown at position `pos`, generated from a submenu specified by `menuItemPath` using a [MenuCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) as menu context.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Shows the Assets menu when you right click on the contextRect Rectangle.
public class EditorUtilityDisplayPopupMenu : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) evt = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) contextRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100);
        if (evt.type == EventType.ContextClick[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ContextClick.html))
        {
            Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePos = evt.mousePosition;
            if (contextRect.Contains(mousePos))
            {
                EditorUtility.DisplayPopupMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayPopupMenu.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(mousePos.x, mousePos.y, 0, 0), "Assets/", null);
                evt.Use();
            }
        }
    }
}

```

* * *
