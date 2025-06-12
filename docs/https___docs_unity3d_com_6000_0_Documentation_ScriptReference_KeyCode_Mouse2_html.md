* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse2.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).Mouse2
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
Middle mouse button (or third button).
Use this to detect middle mouse button presses. The “2” mouse button is the third button on the user’s mouse, which is usually the middle mouse button (often a clickable scroll wheel). Unity defines this as the "2" mouse button, as the mouse button numbering begins at 0.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect if the middle mouse button is pressed
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Mouse2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse2.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse 2 ");
        }
    }
}

```

* * *
