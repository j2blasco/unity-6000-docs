* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.Vibrate.html

#  [Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html).Vibrate
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
public static void Vibrate(); 
### Description
Triggers device vibration.
**Note:** Duration of vibration is determined by the operating system of the target platform. To configure advanced vibration settings, use platform specific libraries.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 10, 100, 32), "Vibrate!"))
            Handheld.Vibrate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.Vibrate.html)();
    }
}

```

* * *
