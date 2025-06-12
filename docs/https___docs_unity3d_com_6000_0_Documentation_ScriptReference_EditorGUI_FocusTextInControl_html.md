* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FocusTextInControl.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).FocusTextInControl
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
public static void FocusTextInControl(string name); 
### Parameters
Parameter | Description  
---|---  
name | Name set using [GUI.SetNextControlName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html).  
### Description
Move keyboard focus to a named text field and begin editing of the content.
In Editor GUI, text fields can have keyboard focus without the text being edited. For example you may switch focus between text fields or other controls by using the up and down arrow keys. Once you click inside the text field, editing of the text itself begins and the arrow keys are then used to navigate the text content. [EditorGUI.FocusTextInControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FocusTextInControl.html) is like [GUI.FocusControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusControl.html) in that it gives keyboard focus to a control, but it also begins editing of the text itself.  
  
Additional resources: [GUI.SetNextControlName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html), [GUI.GetNameOfFocusedControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GetNameOfFocusedControl.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // When pressed the button, selects the "username" Textfield.
    string username = "username";
    string pwd = "a pwd";
    void OnInspectorGUI()
    {
        // Set the internal name of the textfield
        GUI.SetNextControlName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html)("MyTextField");  
  
        // Make the actual text field.
        username = EditorGUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 20), username);
        pwd = EditorGUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 40, 100, 20), pwd);  
  
        // If the user presses this button, keyboard focus will move.
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 80, 20), "Move Focus"))
        {
            EditorGUI.FocusTextInControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FocusTextInControl.html)("MyTextField");
        }
    }
}

```

* * *
