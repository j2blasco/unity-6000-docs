* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnDestroy.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnDestroy()
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
OnDestroy is called to close the EditorWindow window.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorWindowOnDestroy.png)   
_A simple example of OnDestroy()_
```
// Close the window when the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) is pressed. The window
// will receive an OnDestroy() call.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

public class OnDestroyExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/OnDestroy Example")]
    public static void ShowExample()
    {
        OnDestroyExample wnd = GetWindow<OnDestroyExample>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("OnDestroy Example");
    }

    public void CreateGUI()
    {
        Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) closebutton = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        closebutton.text = "Close!";
        closebutton.clicked += () =>
        {
            this.Close();
        };

        rootVisualElement.Add(closebutton);
    }
    void OnDestroy()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Destroyed...");
    }
}

```

* * *
