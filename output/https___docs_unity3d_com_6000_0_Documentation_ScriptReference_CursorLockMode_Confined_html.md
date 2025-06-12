* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.Confined.html

#  [CursorLockMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.html).Confined
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
### Description
Confine cursor to the game window.
Note that confined cursor lock mode is only supported on the standalone player platform on Windows and Linux. Confined cursor lock mode is not supported on MacOS or Android.
```
//This script makes Buttons that control the Cursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html)'s lock state. Note that the Confined mode only works on Windows and Linux Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Standalone.html) platform build.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
