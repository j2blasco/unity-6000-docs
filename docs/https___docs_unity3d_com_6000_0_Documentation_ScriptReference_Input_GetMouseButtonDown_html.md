* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetMouseButtonDown
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
public static bool GetMouseButtonDown(int button); 
### Description
Returns true during the frame the user pressed the given mouse button.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Call this function from the [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) function, since the state gets reset each frame. It will not return true until the user has released the mouse button and pressed it again. _button_ values are 0 for left button, 1 for right button, 2 for the middle button.
```
using UnityEngine;
using System.Collections;  
  
// Detects clicks from the mouse and prints a message
// depending on the click detected.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(0))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pressed left-click.");  
  
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(1))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pressed right-click.");  
  
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(2))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pressed middle-click.");
    }
}

```

* * *
