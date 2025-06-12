* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse5.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).Mouse5
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
Additional (or sixth) mouse button.
Use this for detecting mouse button presses. The “5” mouse button is the sixth button on the user’s mouse if this additional button exists. Unity defines this as the "5" Mouse button, as the mouse Button numbering begins at 0.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect if the extra mouse button is pressed
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Mouse5[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse5.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse 5 ");
        }
    }
}

```

* * *
