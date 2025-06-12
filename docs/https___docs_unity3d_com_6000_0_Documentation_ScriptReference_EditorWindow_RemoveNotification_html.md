* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.RemoveNotification.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).RemoveNotification
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
public void RemoveNotification(); 
### Description
Stop showing notification message.
Notification message fades away automatically after some time. This function will remove it immediately.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ShowRemoveNotification.png)  
_Show a notification in an editor window._
```
// Simple example that shows a notification message
// that the user has typed.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.UIElements;

public class NotificationWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{

    string notification = "This is a notification";

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Notification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Notification.html) Window")]
    public static void ShowExample()
    {
        NotificationWindow wnd = GetWindow<NotificationWindow>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Notification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Notification.html) Window");
    }

    public void CreateGUI()
    {
        // Create button to show notification
        Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) showNotification = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        showNotification.text = "Show!";
        showNotification.clicked += () =>
        {
            this.ShowNotification(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(notification));
        };

        rootVisualElement.Add(showNotification);

        // Create button to remove notification
        Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) removeNotification = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        removeNotification.text = "Remove!";
        removeNotification.clicked += () =>
        {
            this.RemoveNotification();
        };

        rootVisualElement.Add(removeNotification);
    }
}

```

* * *
