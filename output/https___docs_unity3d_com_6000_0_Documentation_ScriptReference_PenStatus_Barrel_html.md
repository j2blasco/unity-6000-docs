* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Barrel.html

#  [PenStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.html).Barrel
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
The barrel button on the pen is currently pressed.
On macOS, this flag will always correspond to the lower barrel button.
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
                if (m_Event.penStatus == PenStatus.Barrel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenStatus.Barrel.html))
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Barrel button on pen is down.");
            }
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse Down.");                   //If it's not a pen event, it's a mouse event. 
        }
    }
}

```

* * *
