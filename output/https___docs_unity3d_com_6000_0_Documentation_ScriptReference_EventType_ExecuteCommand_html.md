* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ExecuteCommand.html

#  [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html).ExecuteCommand
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
Execute a special command (eg. copy & paste).
"Copy", "Cut", "Paste", "Delete", "FrameSelected", "Duplicate", "SelectAll" and so on. Sent only in the editor. Example. Checking that that a frame has the focus:
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        //implement frame selection
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) e = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        if (e.type == EventType.ExecuteCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ExecuteCommand.html) ||
            e.type == EventType.ValidateCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ValidateCommand.html))
        {
            if (Event.current.commandName == "FrameSelected")
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("frame selected");
        }
    }
}

```

Additional resources: [Event.commandName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-commandName.html), [EventType.ValidateCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ValidateCommand.html).
* * *
