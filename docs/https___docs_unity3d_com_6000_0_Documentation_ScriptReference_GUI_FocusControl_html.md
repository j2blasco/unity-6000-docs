* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusControl.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).FocusControl
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
public static void FocusControl(string name); 
### Parameters
Parameter | Description  
---|---  
name | Name set using [SetNextControlName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html).  
### Description
Move keyboard focus to a named control.
Additional resources: [SetNextControlName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html), [GetNameOfFocusedControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GetNameOfFocusedControl.html).  
  
For focusing text in Editor GUI text fields, see [EditorGUI.FocusTextInControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FocusTextInControl.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // When pressed the button, selects the "username" Textfield.
    public string username = "username";
    public string pwd = "a pwd";  
  
    void OnGUI()
    {
        // Set the internal name of the textfield
        GUI.SetNextControlName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html)("MyTextField");  
  
        // Make the actual text field.
        username = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 20), username);
        pwd = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 40, 100, 20), pwd);  
  
        // If the user presses this button, keyboard focus will move.
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 80, 20), "Move Focus"))
            GUI.FocusControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusControl.html)("MyTextField");
    }
}

```

* * *
