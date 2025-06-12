* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).hotControl
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
hotControl; 
### Description
The controlID of the current hot control.
The hot control is one that is temporarily active. When the user mousedown's on a button, it becomes hot.   
No other controls are allowed to respond to mouse events while some other control is hot.  
once the user mouseup's, the control sets `hotControl` to 0 in order to indicate that other controls can now respond to user input.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Click on the button to see the id  
  
    void OnGUI()
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Press Me!");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("id: " + GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html));
    }
}

```

* * *
