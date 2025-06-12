* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-keyboardControl.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).keyboardControl
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
keyboardControl; 
### Description
The controlID of the control that has keyboard focus.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Click on the text field to see the id of the control.  
  
    string str = "A String!";
    void OnGUI()
    {
        str = GUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.TextField.html)(str, 10);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("id: " + GUIUtility.keyboardControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-keyboardControl.html));
    }
}

```

* * *
