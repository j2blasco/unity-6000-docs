* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-keyCode.html

#  [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html).keyCode
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
[KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) keyCode; 
### Description
The raw key code for keyboard events.
Used in [EventType.KeyDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.KeyDown.html) and [EventType.KeyUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.KeyUp.html) events; this returns [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) value that matches the physical keyboard key. Use this for handling cursor keys, function keys etc.  
  
Additional resources: [Event.character](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-character.html).
```
// Detects keys pressed and prints their keycode  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) e = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        if (e.isKey)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Detected key code: " + e.keyCode);
        }
    }
}

```

* * *
