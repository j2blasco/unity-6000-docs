* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.KeyboardEvent.html

#  [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html).KeyboardEvent
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
public static [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) KeyboardEvent(string key); 
### Parameters
Parameter | Description  
---|---  
key | A string representing keyboard keys and modifiers.  
### Returns
**Event** A new Event with [EventType.KeyDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.KeyDown.html) and the requested [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) and optional EventModifier. 
### Description
Create a keyboard event.
This is useful when you need to check if a certain key has been pressed - possibly with modifiers. The syntax for the key string is a key name (same as in the Input Manager), optionally prefixed by any number of modifiers:   
& = Alternate, ^ = Control, % = Command/Windows key, # = Shift   
Examples: &f12 = Alternate + F12, "^[0]" = Control + keypad0 .  
  
  
See the [Input Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html) manual page for more information on key names.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Detects if the Enter key was pressed
    void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Press Enter To Start Game");  
  
        if (Event.current.Equals(Event.KeyboardEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.KeyboardEvent.html)("[enter]")))
        {
            Application.LoadLevel(1);
        }  
  
        if (Event.current.Equals(Event.KeyboardEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.KeyboardEvent.html)("return")))
        {
 		Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("I said enter, not return - try the keypad");
        }
    }
}

```

* * *
