* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).Return
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
Return key.
The key used to accept a line of text. osMac calls this `Return`. A PC calls this `Enter`. There is no `KeyCode.Enter`. On a PC use [Return](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html). Some laptops have no name on the `Return` or `Enter` key.
```
// KeyCode.Return[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html) example.
//
// Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
// This script tells when the Return key is pressed down and when it is released.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect when the Return key is pressed down
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Return[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Return key was pressed.");
        }  
  
        //Detect when the Return key has been released
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)(KeyCode.Return[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Return key was released.");
        }
    }
}

```

* * *
