* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-wantsMouseMove.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).wantsMouseMove
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
wantsMouseMove; 
### Description
Checks whether MouseMove events are received in the GUI in this Editor window.
  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/WantsMouseMoveEx.png)   
_Editor Window that detects mouse moves when the toggle button is activated and the mouse is over the window._
```
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that shows the mouse movement events captured.
// "Mouse Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)" shows where the mouse is outside of the window.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;
using UnityEngine.UIElements;

public class PointerMove : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Mouse Move Example")]
    static void InitWindow()
    {
        PointerMove window = (PointerMove)GetWindowWithRect(typeof(PointerMove), new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 300, 100));
        window.Show();
    }

    Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) m_PointerPosition;

    void CreateGUI()
    {
        rootVisualElement.pickingMode = PickingMode.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.Position.html);

        // Create a toggle button that toggles the value of wantsMouseMove
        var toggle = new Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)
        {
            text = "Receive Movement"
        };
        wantsMouseMove = toggle.value;
        rootVisualElement.Add(toggle);

        m_PointerPosition = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)();
        rootVisualElement.Add(m_PointerPosition);
        
        toggle.RegisterValueChangedCallback((evt) =>
        {
            if (evt.newValue)
                rootVisualElement.RegisterCallback<PointerMoveEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html)>(LogPointerMoved);
            else
                rootVisualElement.UnregisterCallback<PointerMoveEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html)>(LogPointerMoved);
        });
    }

    void LogPointerMoved(PointerMoveEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html) evt)
    {
        m_PointerPosition.text = $"Pointer Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html): {evt.position}";
    }
}

```

* * *
