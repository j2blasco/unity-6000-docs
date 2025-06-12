* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Update.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).Update()
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
Called multiple times per second on all visible windows.
Save frames from the Game View when on play mode.
```
// The window appears in front of the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).
// The window shows the type of a Unity object the cursor is over.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class MouseOverWindowExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string mouseOver = "Nothing...";
    Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) label;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Mouse Over Example")]
    static void Init()
    {
        GetWindow<MouseOverWindowExample>("mouseOver");
    }

    void CreateGUI()
    {
        label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)($"Mouse over: {mouseOver}");
        rootVisualElement.Add(label);
    }

    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        label.schedule.Execute(() =>
        {
            mouseOver = EditorWindow.mouseOverWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-mouseOverWindow.html) ?
                        EditorWindow.mouseOverWindow.ToString() : "Nothing...";
            label.text = $"Mouse over: {mouseOver}";
        }).Every(10);
    }
}

```

* * *
