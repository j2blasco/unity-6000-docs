* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-wantsMouseEnterLeaveWindow.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).wantsMouseEnterLeaveWindow
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
wantsMouseEnterLeaveWindow; 
### Description
Checks whether MouseEnterWindow and MouseLeaveWindow events are received in the GUI in this Editor window.
If set to true, the window recieves an OnGUI call whenever the mouse enters or leaves a window.  
  
**Note:** This function does not trigger Repaint() Automatically. Also, entering or leaving a window while a mouse button is pressed does not trigger either event, as pressing the mouse button activates drag mode (see [EventType.MouseDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDrag.html) and other drag-related events for more information).
```
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that shows how mouse enter and leave window events
// get caught in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

public class WantsMouseEnterLeaveWindowEx : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/wantsMouseEnterLeaveWindow example")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) editorWindow = GetWindow(typeof(WantsMouseEnterLeaveWindowEx));
        editorWindow.Show();
    }

    public void OnGUI()
    {
        wantsMouseEnterLeaveWindow = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Receive Enter/Leave: ", wantsMouseEnterLeaveWindow);
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Check Console for MouseEnter/LeaveWindow messages");

        // Repaint the window as wantsMouseEnterLeaveWindow doesn't trigger a repaint automatically
        if (Event.current.type == EventType.MouseEnterWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseEnterWindow.html) ||
            Event.current.type == EventType.MouseLeaveWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseLeaveWindow.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Received event " +
                ((Event.current.type == EventType.MouseEnterWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseEnterWindow.html)) ? "MouseEnterWindow" : "MouseLeaveWindow"));
            Repaint();
        }
    }   
}

```

* * *
