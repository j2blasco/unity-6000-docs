* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html

#  [Cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html).lockState
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
[CursorLockMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.html) lockState; 
### Description
Determines whether the hardware pointer is locked to the center of the view, constrained to the window, or not constrained at all.
A locked cursor is positioned in the center of the view and cannot be moved. The cursor is invisible in this state, regardless of the value of [Cursor.visible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-visible.html). **Note** : Locking the cursor prevents the user from interacting with UI elements.  
  
A confined cursor behaves normally, but it is confined to the view. For example, if the application is running in a window, the a confined cursor cannot leave that window. The confined cursor mode is only supported on Windows and Linux standalone builds.  
  
The recommended best practice for a positive user experiences is to only to lock or confine the cursor because of a user's action, such as pressing a button.  
  
The cursor state can be changed by the operating system or the Editor. For example, check the state of the cursor when the application regains focus or the state of a game changes to reveal a UI.  
  
In the Editor, the cursor loses focus in Game mode when you press Escape or when you switch an application. In the Standalone Player, you have full control over the mouse cursor, but if you switch applications, the cursor goes out of focus.
```
using UnityEngine;  
  
public class CursorLockExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space bar to apply no locking to the Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
            Cursor.lockState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html) = CursorLockMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.None.html);
    }  
  
    void OnGUI()
    {
        //Press this button to lock the Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 50), "Lock Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)"))
        {
            Cursor.lockState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html) = CursorLockMode.Locked[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.Locked.html);
        }  
  
        //Press this button to confine the Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html) within the screen
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(125, 0, 100, 50), "Confine Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)"))
        {
            Cursor.lockState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html) = CursorLockMode.Confined[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.Confined.html);
        }
    }
}

```

* * *
