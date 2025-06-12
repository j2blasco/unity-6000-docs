* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnInspectorUpdate.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnInspectorUpdate()
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
OnInspectorUpdate is called at 10 frames per second to give the inspector a chance to update.
```
// Simple script that aligns the position of several selected GameObjects
// with the first selected one.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;
using UnityEngine.UIElements;

public class OnInspectorUpdateExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool alignToX = true;
    bool alignToY = true;
    bool alignToZ = true;
    string selected = "";
    string alignTo = "";

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/OnInspectorUpdate example")]
    static void Init()
    {
        OnInspectorUpdateExample window = (OnInspectorUpdateExample)GetWindow(typeof(OnInspectorUpdateExample));
        window.Show();
    }

    void  OnInspectorUpdate()
    {        
        selected = Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html) ? Selection.activeTransform.name : "";
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("Select various Objects in the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html) view to align them with the first selected one.");
        rootVisualElement.Add(label);

        selected = Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html) ? Selection.activeTransform.name : "";

        var labelSelected = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)();
        rootVisualElement.Add(labelSelected);

        labelSelected.schedule.Execute(() =>
        {
            labelSelected.text = $"Selected object: {selected}";
        }).Every(10);

        var toggleX = new Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)();
        toggleX.text = "X";
        toggleX.value = alignToX;
        toggleX.RegisterValueChangedCallback(evt => alignToX = evt.newValue);
        rootVisualElement.Add(toggleX);

        var toggleY = new Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)();
        toggleY.text = "Y";
        toggleY.value = alignToY;
        toggleY.RegisterValueChangedCallback(evt => alignToY = evt.newValue);
        rootVisualElement.Add(toggleY);

        var toggleZ = new Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)();
        toggleZ.text = "Z";
        toggleZ.value = alignToZ;
        toggleZ.RegisterValueChangedCallback(evt => alignToZ = evt.newValue);
        rootVisualElement.Add(toggleZ);

        var buttonAlign = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonAlign.text = "Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html)";
        buttonAlign.clicked += () => Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html)();
        rootVisualElement.Add(buttonAlign);
    }

    void Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html)()
    {
        if (selected == "")
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No objects selected to align");
        }

        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) alignementPosition = Selection.activeTransform.position;
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newPosition;

            newPosition.x = alignToX ? alignementPosition.x : t.position.x;
            newPosition.y = alignToY ? alignementPosition.y : t.position.y;
            newPosition.z = alignToZ ? alignementPosition.z : t.position.z;

            t.position = newPosition;
        }
    }
}

```

* * *
