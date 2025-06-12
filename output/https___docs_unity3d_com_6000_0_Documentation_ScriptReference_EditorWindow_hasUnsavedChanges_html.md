* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-hasUnsavedChanges.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).hasUnsavedChanges
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
hasUnsavedChanges; 
### Description
This property specifies whether the Editor prompts the user to save or discard unsaved changes before the window closes.
Set hasUnsavedChanges to true to prompt the user to save or discard unsaved changes. This helps prevent them from accidentally losing unsaved work. When you use hasUnsavedChanges, you must also use [EditorWindow.saveChangesMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-saveChangesMessage.html), and override the [EditorWindow.SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.SaveChanges.html) and/or [EditorWindow.DiscardChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.DiscardChanges.html) methods. When hasUnsavedChanges is enabled, the title bar and docked tabs update to indicate that the user needs to save their work. If the user closes the window without saving, a message box appears, and prompts them to either save, discard their changes, or cancel. 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class UnsavedChangesExampleWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window With Unsaved Changes")]
    static void Init()
    {
        UnsavedChangesExampleWindow window = (UnsavedChangesExampleWindow)EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)(typeof(UnsavedChangesExampleWindow), new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 400, 400));

        window.saveChangesMessage = "This window has unsaved changes. Would you like to save?";
        window.Show();
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)();
        label.text = hasUnsavedChanges ? "I have changes!" : "No changes.";
        rootVisualElement.Add(label);

        var buttonCreate = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonCreate.text = "Create unsaved changes";
        buttonCreate.clicked += () => {
            hasUnsavedChanges = true;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{this} has unsaved changes!!!");
        };
        rootVisualElement.Add(buttonCreate);

        var buttonSave = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonSave.text = "Save";
        buttonSave.clicked += () => SaveChanges();
        rootVisualElement.Add(buttonSave);

        var buttonDiscard = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonDiscard.text = "Discard";
        buttonDiscard.clicked += () => DiscardChanges();
        rootVisualElement.Add(buttonDiscard);
    }

    public override void SaveChanges()
    {
        // Your custom save procedures here

        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{this} saved successfully!!!");
        base.SaveChanges();
    }

    public override void DiscardChanges()
    {
        // Your custom procedures to discard changes

        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{this} discarded changes!!!");
        base.DiscardChanges();
    }
}

```

* * *
