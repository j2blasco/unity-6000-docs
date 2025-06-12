* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.PasswordField.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).PasswordField
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
public static string PasswordField(string password, char maskChar, params GUILayoutOption[] options); 
## Declaration
public static string PasswordField(string password, char maskChar, int maxLength, params GUILayoutOption[] options); 
## Declaration
public static string PasswordField(string password, char maskChar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static string PasswordField(string password, char maskChar, int maxLength, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
password | Password to edit. The return value of this function should be assigned back to the string as shown in the example.  
maskChar | Character to mask the password with.  
maxLength | The maximum length of the string. If left out, the user can type for ever and ever.  
style | The style to use. If left out, the `textField` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**string** The edited password. 
### Description
Make a text field where the user can enter a password.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutPasswordField.png)   
_Password field in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string passwordToEdit = "My Password";  
  
    void OnGUI()
    {
        // Make a password field that modifies passwordToEdit.
        passwordToEdit = GUILayout.PasswordField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.PasswordField.html)(passwordToEdit, "*"[0], 25);
    }
}

```

* * *
