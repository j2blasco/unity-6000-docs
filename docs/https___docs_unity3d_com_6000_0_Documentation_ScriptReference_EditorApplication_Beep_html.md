* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Beep.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).Beep
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
public static void Beep(); 
### Description
Plays system beep sound.
```
// Play beep sound on menu click  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class BeepExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Play beep")]
    static void DoBeep()
    {
        EditorApplication.Beep[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Beep.html)();
    }
}

```

* * *
