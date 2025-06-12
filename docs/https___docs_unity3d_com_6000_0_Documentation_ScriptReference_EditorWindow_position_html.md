* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-position.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).position
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
[Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position; 
### Description
The desired position of the window in screen space.
Setting this value will undock the window if it is docked.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorWindowPosition.png)  
_Create an undocked editor window with position._
```
// The position of the window is displayed when it is
// external from Unity.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class PositionExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Vector2Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) p1;
    bool showButton = true;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Window Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)")]
    static void Init()
    {
        GetWindow<PositionExample>("position");
    }

    void CreateGUI()
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r = position;
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html): " + r.x + "x" + r.y);
        rootVisualElement.Add(label);
        
        var field = new Vector2IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector2IntField.html)("Set the position:");
        rootVisualElement.Add(field);
        if (showButton)
        {
            var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)(() => {
                r.x = field.value.x;
                r.y = field.value.y;

                position = r;
            });
            button.text = "Accept new position";
            rootVisualElement.Add(button);
        }
    }
}

```

* * *
