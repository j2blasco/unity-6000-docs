* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInCallstackAttribute.html

# HideInCallstackAttribute
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Marks the methods you want to hide from the Console window callstack. When you hide these methods they are removed from the detail area of the selected message in the Console window.
To hide the marked methods, click the Console menu button then select **Strip logging callstack** from the menu.
```
using UnityEngine;  
  
public class HideInCallstackExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HiddenDebug("[HideInCallstack] Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) message here.");
        VisibleDebug("Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) message here.");
    }  
  
    // Hidden in the detail area of the message in the console window.
    [HideInCallstack]
    public static void HiddenDebug(object logMsg)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(logMsg);
    }  
  
    // Visible in the detail area of the message in the console window.
    public static void VisibleDebug(string logMsg)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(logMsg);
    }
}

```

* * *
