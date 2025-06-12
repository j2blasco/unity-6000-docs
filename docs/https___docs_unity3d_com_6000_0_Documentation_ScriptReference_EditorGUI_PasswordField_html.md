* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PasswordField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).PasswordField
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
public static string PasswordField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string password, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
## Declaration
public static string PasswordField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, string password, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
## Declaration
public static string PasswordField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, string password, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the password field.  
label | Optional label to display in front of the password field.  
password | The password to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**string** The password entered by the user. 
### Description
Makes a text field where the user can enter a password.
This works just like [GUI.PasswordField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.PasswordField.html), but correctly responds to select all, etc. in the editor, and it can have an optional label in front.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIPasswordField.png)  
_Password Field in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that creates a password field and lets you visualize what have you
// typed in a label.  
  
class EditorGUIPasswordField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string text = "Some text here";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Password field usage")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow<EditorGUIPasswordField>();
        window.Show();
    }  
  
    void OnGUI()
    {
        text = EditorGUI.PasswordField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PasswordField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 20),
            "Type Something:",
            text);  
  
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 5, 20),
            "Written Text:",
            text);
    }
}

```

* * *
