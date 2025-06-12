* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.html

# PenStatus
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
Options for specifying the state of the pen. For example, whether the pen is in contact with the screen or tablet, whether the pen is inverted, and whether buttons are pressed. You can combine states using bitwise OR operators.
Before you process an event as a pen event, you should check the [PointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PointerType.html) of a mouse event (e.g. [EventType.MouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html)).   
  
When a user uses a pen, some mouse events are often mixed with pen events in the event stream, and you can't distinguish them by type because mouse and pen events share the same [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html). Instead, use [PointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PointerType.html) to distinguish them. Otherwise, Unity processes all incoming mouse events as pen events, which can lead to unexpected behavior because the mouse events (pointerType = Mouse) do not have pen event fields, like [PenStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.html), set.
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
            {
                if (m_Event.penStatus == PenStatus.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.None.html))
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pen is in a neutral state.");
                else if (m_Event.penStatus == PenStatus.Inverted[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Inverted.html))
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The pen is inverted.");
                else if (m_Event.penStatus == PenStatus.Barrel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Barrel.html))
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Barrel button on pen is down.");
                else if (m_Event.penStatus == PenStatus.Contact[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Contact.html))
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pen is in contact with screen or tablet.");
                else if (m_Event.penStatus == PenStatus.Eraser[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Eraser.html))
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pen is in erase mode.");
            }
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
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.None.html) | The pen is in a neutral state.  
[Contact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Contact.html) | The pen is in contact with the screen or tablet.  
[Barrel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Barrel.html) | The barrel button on the pen is currently pressed.  
[Inverted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Inverted.html) | The pen is inverted.  
[Eraser](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Eraser.html) | The pen is in erase mode.  
* * *
