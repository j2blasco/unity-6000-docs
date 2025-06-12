* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).mousePosition
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) mousePosition; 
### Description
The current mouse position in pixel coordinates. (Read Only).
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
[Input.mousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html) is a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) for compatibility with functions that have [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) arguments. The z component of the [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) is always 0.  
  
The bottom-left of the screen or window is at (0, 0). The top-right of the screen or window is at ([Screen.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), [Screen.height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)).  
  
Note: [Input.mousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html) reports the position of the mouse even when it is not inside the Game View, such as when [Cursor.lockState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html) is set to [CursorLockMode.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.None.html). When running in windowed mode with an unconfined cursor, position values smaller than 0 or greater than the screen dimensions ([Screen.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html),[Screen.height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)) indicate that the mouse cursor is outside of the game window.  
  
In the following example, the x and y coordinates of the mouse position are printed when the “Fire1” button is clicked.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("Fire1"))
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) mousePos = Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html);
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(mousePos.x);
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(mousePos.y);
            }
        }
    }
}

```

* * *
