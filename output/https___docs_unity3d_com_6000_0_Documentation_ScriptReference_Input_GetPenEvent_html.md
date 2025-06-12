* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetPenEvent.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetPenEvent
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
public static [PenData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html) GetPenEvent(int index); 
### Returns
**PenData** Pen event details in the struct. 
### Description
Returns the [PenData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html) for the pen event at the given index in the pen event queue.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
On Windows, the pen event queue holds, in chronological order, any missed pen events as provided by GetPointerPenInfoHistory. The queue is cleared at the end of each frame. On all other platforms the queue will always be empty.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Pen Window")]
    public static void ShowWindow()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) win = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(Example));
        win.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Pen Window");
        win.wantsMouseMove = true;
    }  
  
    void OnGUI()
    {
        var e = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        if ((e.type == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html)
             || e.type == EventType.MouseDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDrag.html)
             || e.type == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html)
             || e.type == EventType.MouseUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html)
             || e.type == EventType.MouseMove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseMove.html))
            && (e.pointerType == PointerType.Pen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PointerType.Pen.html)))
        {
            int count = Input.penEventCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-penEventCount.html);
            for (int i = 0; i < count; i++)
            {
                // Log data from queued pen events
                PenData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html) p = Input.GetPenEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetPenEvent.html)(i);
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Pen position {p.position}, pen pressure {p.pressure}, pen twist {p.twist}, pen tilt {p.tilt}, pen status - barrel {(p.penStatus & PenStatus.Barrel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Barrel.html)) != 0}");
            }
            Input.ResetPenEvents[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.ResetPenEvents.html)();
        }
    }
}

```

* * *
