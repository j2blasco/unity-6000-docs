* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.CommandEvent.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).CommandEvent
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
public static [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) CommandEvent(string commandName); 
### Parameters
Parameter | Description  
---|---  
commandName | The command to be sent.  
### Description
Creates an event that can be sent to another window.
```
// Sends a paste event to an EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html), as if Paste
// was selected from the Edit menu.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CommandEventExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/CommandEvent example")]
    static void commandEventExample()
    {
        CommandEventExample window = EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)<CommandEventExample>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 150, 40));
        window.Show();
    }  
  
    void OnGUI()
    {
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Paste"))
        {
            Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) e = EditorGUIUtility.CommandEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.CommandEvent.html)("Paste");
            EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) ew = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<CommandEventTest>(true);
            ew.SendEvent(e);
        }
    }
}

```

The script below receives the Paste message sent from CommandEventExample above.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CommandEventTest : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    private int eventCount = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Example that receives a paste event")]
    static void test()
    {
        CommandEventTest window = EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)<CommandEventTest>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 40));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 90, 30), "Paste: " + eventCount.ToString());  
  
        if (Event.current.type == EventType.ExecuteCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.ExecuteCommand.html))
        {
            Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) e = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
            if (e.commandName == "Paste")
            {
                eventCount = eventCount + 1;
            }
        }
    }
}

```

* * *
