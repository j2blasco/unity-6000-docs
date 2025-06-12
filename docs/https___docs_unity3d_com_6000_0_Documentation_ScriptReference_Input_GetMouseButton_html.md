* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetMouseButton
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
public static bool GetMouseButton(int button); 
### Description
Returns whether the given mouse button is held down.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
The _button_ values are: 0 for the left button, 1 for the right button, 2 for the middle button. The return is `true` when the mouse button is pressed down, and `false` when released.
```
using UnityEngine;
using System.Collections;  
  
// Detects clicks from the mouse and prints a message
// depending on the click detected.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(0))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The left mouse button is being held down.");
        }  
  
        if (Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(1))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The right mouse button is being held down.");
        }  
  
        if (Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(2))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The middle mouse button is being held down.");
        }
    }
}

```

* * *
