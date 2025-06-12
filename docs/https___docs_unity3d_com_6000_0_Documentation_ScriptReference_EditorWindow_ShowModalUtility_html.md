* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowModalUtility.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).ShowModalUtility
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
public void ShowModalUtility(); 
### Description
Shows the EditorWindow as a floating modal window.
You cannot interact with the utility window while the Editor is runs. The [EditorWindow.ShowModalUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowModalUtility.html) window is never hidden by the Editor. You cannot dock the utility window to the Editor.  
  
Utility windows are always in front of normal Unity windows. The utility window is hidden when the user switches from Unity to another application.  
  
**Note:** You do not need to use [EditorWindow.GetWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html) before you use this function to show the window. 
```
// Simple script that randomizes the rotation of the selected GameObjects.

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

public class RandomizeInSelection : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    System.Random random = new System.Random();
    public float rotationAmount;
    public string selected = "";

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Randomize Objects")]
    static void Init()
    {
        RandomizeInSelection window =
            EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<RandomizeInSelection>(true, "Randomize Objects");
        window.ShowModalUtility();
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("Select an object and click the Randomize! button");
        rootVisualElement.Add(label);

        var randomizeButton = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        randomizeButton.text = "Randomize!";
        randomizeButton.clicked += () => RandomizeSelected();
        rootVisualElement.Add(randomizeButton);
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
