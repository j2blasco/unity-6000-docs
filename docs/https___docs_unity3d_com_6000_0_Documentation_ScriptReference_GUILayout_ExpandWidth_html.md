* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).ExpandWidth
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
## Declaration
public static [GUILayoutOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutOption.html) ExpandWidth(bool expand); 
### Description
Option passed to a control to allow or disallow horizontal expansion.
If this is true, the enclosed UI elements can expand to fill the available horizontal width.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ExpandWidth.png).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html)();
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Short Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)", GUILayout.ExpandWidth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html)(false));
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Very very long Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)");
        GUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html)();
    }
}

```

* * *
