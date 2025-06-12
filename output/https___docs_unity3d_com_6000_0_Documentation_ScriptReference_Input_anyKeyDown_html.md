* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-anyKeyDown.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).anyKeyDown
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
anyKeyDown; 
### Description
Returns true the first frame the user hits any key or mouse button. (Read Only)
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
You should be polling this variable from the [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) function, since the state gets reset each frame. It will not return true until the user has released all keys / buttons and pressed any key / buttons again. This does not detect touches. For touches, use [Input.touchCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Detects if any key has been pressed down.  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.anyKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-anyKeyDown.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("A key or mouse click has been detected");
        }
    }
}

```

* * *
