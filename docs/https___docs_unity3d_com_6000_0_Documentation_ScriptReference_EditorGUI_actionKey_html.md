* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-actionKey.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).actionKey
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
actionKey; 
### Description
Is the platform-dependent "action" modifier key held down? (Read Only)
The key is Command on macOS, Control on Windows.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIActionKey.png)  
_Action Key usage, key not pressed/key pressed._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Shows a password field with some "hidden" text.
// When the user presses the action key the password field becomes a text field.  
  
class EditorGUIActionKey : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string text = "This is some text";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Show Hide password")]
    static void Init()
    {
        var window = GetWindow<EditorGUIActionKey>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 250, 60);
        window.Show();
    }  
  
    void OnGUI()
    {
        // Show the contents
        if (EditorGUI.actionKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-actionKey.html))
        {
            text = EditorGUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 5, 245, 20), "Shown  Text:", text);
        }
        else
        {
            // show the pasword field
            text = EditorGUI.PasswordField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PasswordField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 5, 245, 20), "Hidden Text:", text);
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 30, 250, 20), "Close"))
            this.Close();
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
