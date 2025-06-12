* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-windowFocusChanged.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).windowFocusChanged
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
Called whenever the focused editor window is changed.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

public class FocusedWindowTracker : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Focused Window Tracker")]
    private static void ShowTracker() => GetWindow<FocusedWindowTracker>();

    private void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("I'm logging every focused window");
        rootVisualElement.Add(label);
    }

    private void OnEnable()
    {
        EditorWindow.windowFocusChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-windowFocusChanged.html) += TrackFocusedWindow;
    }

    private void OnDisable()
    {
        EditorWindow.windowFocusChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-windowFocusChanged.html) -= TrackFocusedWindow;
    }

    private static void TrackFocusedWindow()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Current focused window is {focusedWindow.titleContent.text}.");
    }
}

```

* * *
