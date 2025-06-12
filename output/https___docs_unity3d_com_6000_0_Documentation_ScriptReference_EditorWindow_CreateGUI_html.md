* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).CreateGUI()
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
`CreateGUI` is called when the EditorWindow's rootVisualElement is ready to be populated.
Use `CreateGUI` to add UI Toolkit UI elements to your window.   
  
When creating a custom Editor window, follow these guidelines: 
  * Put code dependent on UXML/USS loading in the [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) method to ensure that all necessary assets are available.
  * Keep the event registration code inside [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) or after [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) is called.


It's important to note that `CreateGUI` might not be called before the first call to [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Update.html). For more information, refer to [the order of execution of the Editor window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).  
  
For an example on how to create an Editor window to react to user input, refer to [Create a custom Editor window with C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateEditorWindow.html). 
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
