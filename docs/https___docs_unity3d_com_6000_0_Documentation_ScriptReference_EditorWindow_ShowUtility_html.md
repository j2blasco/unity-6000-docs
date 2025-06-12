* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowUtility.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).ShowUtility
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
public void ShowUtility(); 
### Description
Show the EditorWindow as a floating utility window.
When the utility window loses focus it remains on top of the new active window. This means the [EditorWindow.ShowUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowUtility.html) window is never hidden by the Unity editor. It is, however, not dockable to the editor.  
  
Utility windows will always be in front of normal Unity windows. It will be hidden when the user switches from Unity to another application.  
  
**Note:** You do not need to use [EditorWindow.GetWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html) before using this function to show the window. 
```
// Simple script that randomizes the rotation of the selected GameObjects.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

public class RandomizeInSelectionShowUtility : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    System.Random random = new System.Random();
    public float rotationAmount;
    public string selected = "";

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Randomize Objects")]
    static void Init()
    {
        RandomizeInSelectionShowUtility window =
            EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<RandomizeInSelectionShowUtility>(true, "Randomize Objects");
        window.ShowUtility();
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("Selected an object and click Randomize!");
        rootVisualElement.Add(label);

        var buttonRandomize = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonRandomize.text = "Randomize!";
        buttonRandomize.clicked += () => RandomizeSelected();
        rootVisualElement.Add(buttonRandomize);
    }

    void RandomizeSelected()
    {
        foreach (var transform in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
        {
            Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Random.rotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotation.html);
            rotationAmount = (float)random.NextDouble();
            transform.localRotation = Quaternion.Slerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Slerp.html)(transform.localRotation, rotation, rotationAmount);
        }
    }
}

```

* * *
