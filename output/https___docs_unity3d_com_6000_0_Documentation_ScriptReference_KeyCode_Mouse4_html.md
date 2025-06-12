* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse4.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).Mouse4
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
Additional (fifth) mouse button.
Use this for detecting mouse button presses. The “4” mouse button is the fifth button on the user’s mouse if this additional button exists, for example, volume buttons on the mouse. Unity defines this as the "4" Mouse button, as the mouse Button numbering begins at 0.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect if the extra mouse button is pressed
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Mouse4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse4.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse 4 ");
        }
    }
}

```

* * *
