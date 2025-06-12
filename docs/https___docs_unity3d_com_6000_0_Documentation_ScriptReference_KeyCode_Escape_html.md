* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Escape.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).Escape
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
Escape key.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Escape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Escape.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Escape key was pressed");
        }  
  
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)(KeyCode.Escape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Escape.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Escape key was released");
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Escape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Escape.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Escape key is being pressed");
        }
    }
}

```

* * *
