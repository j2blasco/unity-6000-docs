* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html

# EventType
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
Types of UnityGUI input and processing events.
Use this to tell which type of event has taken place in the GUI. Types of Events include mouse clicking, mouse dragging, button pressing, the mouse entering or exiting the window, and the scroll wheel as well as others mentioned below.  
  
Events can be used to prevent other GUI elements from responding to that event. Refer to [Event.Use](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.Use.html).  
  
Additional resources: [Event.type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-type.html), [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html), [GUI Scripting Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script is a basic overview of some of the Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) Types available. It outputs messages depending on the current Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) Type.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) m_Event = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);  
  
        if (m_Event.type == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse Down.");
        }  
  
        if (m_Event.type == EventType.MouseDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDrag.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse Dragged.");
        }  
  
        if (m_Event.type == EventType.MouseUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse Up.");
        }
    }
}

```

```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) m_Event = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);  
  
        if (m_Event.type == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html))
        {
            if (m_Event.pointerType == PointerType.Pen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PointerType.Pen.html))     //Check if it's a pen event.
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pen Down.");
            else 
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse Down.");                   //If it's not a pen event, it's a mouse event. 
        }
    }
}

```

### Properties
Property | Description  
---|---  
[MouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html) | Mouse button was pressed.  
[MouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html) | Mouse button was released.  
[MouseMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseMove.html) | Mouse was moved (Editor views only).  
[MouseDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDrag.html) | Mouse was dragged.  
[KeyDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.KeyDown.html) | A keyboard key was pressed.  
[KeyUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.KeyUp.html) | A keyboard key was released.  
[ScrollWheel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ScrollWheel.html) | The scroll wheel was moved.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) | A repaint event. One is sent every frame.  
[Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Layout.html) | A layout event.  
[DragUpdated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragUpdated.html) | Editor only: drag & drop operation updated.  
[DragPerform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragPerform.html) | Editor only: drag & drop operation performed.  
[DragExited](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragExited.html) | Editor only: drag & drop operation exited.  
[Ignore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Ignore.html) |  Event should be ignored.  
[Used](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Used.html) | Already processed event.  
[ValidateCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ValidateCommand.html) | Validates a special command (e.g. copy & paste).  
[ExecuteCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ExecuteCommand.html) | Execute a special command (eg. copy & paste).  
[ContextClick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ContextClick.html) | User has right-clicked (or control-clicked on the mac).  
[MouseEnterWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseEnterWindow.html) | Mouse entered a window (Editor views only).  
[MouseLeaveWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseLeaveWindow.html) | Mouse left a window (Editor views only).  
[TouchDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.TouchDown.html) | Direct manipulation device (finger, pen) touched the screen.  
[TouchUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.TouchUp.html) | Direct manipulation device (finger, pen) left the screen.  
[TouchMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.TouchMove.html) | Direct manipulation device (finger, pen) moved on the screen (drag).  
[TouchEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.TouchEnter.html) | Direct manipulation device (finger, pen) moving into the window (drag).  
[TouchLeave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.TouchLeave.html) | Direct manipulation device (finger, pen) moved out of the window (drag).  
[TouchStationary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.TouchStationary.html) | Direct manipulation device (finger, pen) stationary event (long touch down).  
* * *
