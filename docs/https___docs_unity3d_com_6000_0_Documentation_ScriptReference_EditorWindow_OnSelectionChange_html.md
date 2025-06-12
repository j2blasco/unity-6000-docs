* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnSelectionChange.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnSelectionChange()
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
Called whenever the selection has changed.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SelectionChange.png)   
_Saves the current selection and load it later with a simple click._
```
// Simple example that lets you save the current selection and load it.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class OnSelectionChangeExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    private int[] selectionIDs;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) Saver")]
    private static void Init()
    {
        OnSelectionChangeExample window = (OnSelectionChangeExample)GetWindow(typeof(OnSelectionChangeExample));
        window.Show();
    }

    void CreateGUI()
    {
        var buttonSave = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonSave.text = "Save";
        buttonSave.clicked += () => SaveSelection();
        rootVisualElement.Add(buttonSave);
        
        var buttonLoad = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonLoad.text = "Load";
        buttonLoad.clicked += () => LoadLastSavedSelection();
        rootVisualElement.Add(buttonLoad);

        // Initialize selectionIDs at least once
        OnSelectionChange();
    }

    void OnSelectionChange()
    {
        selectionIDs = Selection.instanceIDs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-instanceIDs.html);
    }

    private void SaveSelection()
    {
        var saveStr = "";

        foreach (int i in selectionIDs)
        {
            saveStr += i + ";";
        }

        saveStr = saveStr.TrimEnd(char.Parse(";"));
        EditorPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html)("SelectedIDs", saveStr);
    }

    private void LoadLastSavedSelection()
    {
        string[] strIDs = EditorPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetString.html)("SelectedIDs").Split(char.Parse(";"));

        int[] ids = new int[strIDs.Length];
        for (var i = 0; i < strIDs.Length; i++)
        {
            if (!string.IsNullOrEmpty(strIDs[i]))
                ids[i] = int.Parse(strIDs[i]);
        }

        Selection.instanceIDs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-instanceIDs.html) = ids;
    }
}

```

* * *
