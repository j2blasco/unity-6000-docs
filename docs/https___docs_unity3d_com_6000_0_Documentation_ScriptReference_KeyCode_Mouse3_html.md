* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse3.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).Mouse3
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
Additional (fourth) mouse button.
Use this for detecting mouse button presses. The “3” mouse button is the fourth button on the user’s mouse if any additional buttons exist, for example, extra volume buttons. Unity defines this as the "3" mouse button, as the mouse button numbering begins at 0 for the main mouse button.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect if the extra mouse button is pressed
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Mouse3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse3.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse 3 ");
        }
    }
}

```

* * *
