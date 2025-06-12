* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).SetNextControlName
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
public static void SetNextControlName(string name); 
### Description
Set the name of the next control.
This makes the following control be registered with a given name.  
  
Additional resources: [GetNameOfFocusedControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GetNameOfFocusedControl.html), [FocusControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusControl.html).
```
// Sets the login textfield with "user".  If it is selected and the user
// presses enter, it prints Login  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string login = "username";
    public string login2 = "no action here";  
  
    void OnGUI()
    {
        GUI.SetNextControlName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html)("user");
        login = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 130, 20), login);  
  
        login2 = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 40, 130, 20), login2);
        if (Event.current.Equals(Event.KeyboardEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.KeyboardEvent.html)("return")) && GUI.GetNameOfFocusedControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GetNameOfFocusedControl.html)() == "user")
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Login");  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(150, 10, 50, 20), "Login"))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Login");
    }
}

```

* * *
