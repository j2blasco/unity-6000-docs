* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html

#  [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html).UpArrow
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
Up arrow key.
Use this as a parameter to a function like [Input.GetKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html) to detect when the user presses the up arrow key. Additional resources: [Input.GetKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html), [Input.GetKeyDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html), [Input.GetKeyUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html).
```
//Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script tells when the up arrow key is pressed down and when it is released
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect when the up arrow key is pressed down
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.UpArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html)))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Up Arrow key was pressed.");  
  
        //Detect when the up arrow key has been released
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)(KeyCode.UpArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html)))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Up Arrow key was released.");
    }
}

```

* * *
