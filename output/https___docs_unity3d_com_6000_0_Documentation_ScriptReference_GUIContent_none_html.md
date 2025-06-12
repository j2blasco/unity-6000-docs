* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html

#  [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html).none
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
[GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) none; 
### Description
Shorthand for empty content.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20), GUIContent.none[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html));
    }
}

```

* * *
