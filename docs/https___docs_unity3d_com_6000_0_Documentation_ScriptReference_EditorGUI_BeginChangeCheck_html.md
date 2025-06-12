* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).BeginChangeCheck
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
public static void BeginChangeCheck(); 
### Description
Starts a new code block to check for GUI changes.
Use this in combination with [EditorGUI.EndChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html) to create a code block that checks if the GUI state changed for just the controls contained in that block.  
This method is different from [GUI.changed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html), which returns true for _any_ changes to the GUI state. BeginChangeCheck() limits the check to a specific set of controls. 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float sliderValue = 0;
    string labelText = "-";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Example Window")]
    static void Init()
    {
        var example = (ExampleWindow)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(ExampleWindow));
        example.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("New value", labelText);  
  
        // Start a code block to check for GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) changes
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();  
  
        sliderValue = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)(sliderValue, 0, 1);  
  
        // End the code block and update the label if a change occurs.
        // Note: This indicates user interaction with the slider but does not guarantee that a SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) has changed.
        // To have the updated value, call serializedObject.ApplyModifiedProperties().
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            labelText = sliderValue.ToString();
        }
    }
}

```

* * *
