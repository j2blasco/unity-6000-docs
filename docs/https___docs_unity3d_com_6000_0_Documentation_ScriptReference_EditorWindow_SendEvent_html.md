* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.SendEvent.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).SendEvent
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
public bool SendEvent([Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) e); 
### Description
Sends an Event to a window.
The [SendEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.SendEvent.html) public function passes a selected [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) to a chosen visible window. The [Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) can be found in the [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html) list.  
  
In the following scripts `SendEventExample` looks up the `ReceiveEventExample` window. A `Paste` event is then sent over when the button is pressed. 
```
// Send an event to another editor window. The second
// window needs to be visible to receive the event.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class SendEventExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Send Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html)")]
    static void Init()
    {
        SendEventExample window =
            EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<SendEventExample>(true, "Send Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) Window");
        window.Show();
    }

    void CreateGUI()
    {
        var buttonSendEvent = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonSendEvent.text = "Send Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html)";
        buttonSendEvent.clicked += () =>
        {
            EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) win = GetWindow<ReceiveEventExample>();
            if (win)
                using (var commandEvent = ExecuteCommandEvent.GetPooled(EditorGUIUtility.CommandEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.CommandEvent.html)("Paste")))
                {
                    win.rootVisualElement.SendEvent(commandEvent);
                }
        };
        rootVisualElement.Add(buttonSendEvent);
    }
}

```

```
// An Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window that receives sent events.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class ReceiveEventExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Receive Events[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events.html)")]
    static void Init()
    {
        ReceiveEventExample window =
            EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<ReceiveEventExample>(true, "Receive Events[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events.html) Window");
        window.Show();
    }

    void CreateGUI()
    {
        var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        button.text = "Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)";
        rootVisualElement.Add(button);

        rootVisualElement.RegisterCallback<ExecuteCommandEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ExecuteCommandEvent.html)>(evt =>
        {
            if (evt.commandName == "Paste")
                button.text = "Paste received";
        }, TrickleDown.TrickleDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.TrickleDown.html));
    }
}

```

* * *
