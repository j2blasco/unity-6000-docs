* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-maximized.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).maximized
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
maximized; 
### Description
Whether or not this window is maximized?
To maximize the custome Editor window to the size of the Unity screen, set `maximized`. It works only when the custom Editor window is docked within Unity. 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

public class MaximizedExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Maximized Window Example")]
    public static void ShowExample()
    {
        MaximizedExample wnd = GetWindow<MaximizedExample>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("MaximizedExample");
    }

    public void CreateGUI()
    {
        var toggle = new Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)("Maximize window");
        toggle.value = this.maximized;
        rootVisualElement.Add(toggle);
    }
}

```

* * *
