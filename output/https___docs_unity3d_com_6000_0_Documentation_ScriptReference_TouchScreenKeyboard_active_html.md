* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-active.html

#  [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html).active
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
active; 
### Description
Is the keyboard visible or sliding into the position on the screen?
Use this property to bring previously hidden keyboard back on the screen.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Hides the keyboard if the device is facing down
    // and resumes input if the device is facing up.  
  
    TouchScreenKeyboard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) keyboard;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (keyboard != null)
        {
            if (Input.deviceOrientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-deviceOrientation.html) == DeviceOrientation.FaceDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceOrientation.FaceDown.html))
                keyboard.active = false;
            if (Input.deviceOrientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-deviceOrientation.html) == DeviceOrientation.FaceUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceOrientation.FaceUp.html))
                keyboard.active = true;
        }
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 10, 200, 32), "Open keyboard"))
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("text");
    }
}

```

* * *
