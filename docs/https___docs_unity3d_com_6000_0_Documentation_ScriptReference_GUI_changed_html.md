* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).changed
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
changed; 
### Description
Returns true if any controls changed the value of the input data.
```
// Draws a text field and when it gets modified prints a message
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string stringToEdit = "Modify me.";  
  
    void OnGUI()
    {
        // Make a text field that modifies stringToEdit.
        stringToEdit = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 20), stringToEdit, 25);  
  
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Text field has changed.");
        }
    }
}

```

* * *
