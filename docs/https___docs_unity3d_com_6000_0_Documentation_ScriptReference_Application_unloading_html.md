* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unloading.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).unloading
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
Unity raises this event when the Player is unloading.
Add an event handler to this event if you want to trigger events to [Application.Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html) calls. The event is raised after a call to [Application.Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html) is made, right before the unloading starts.  
  
**Note:** The `Application.unloading` event is only supported on iOS, Android, and Universal Windows Platform.
```
using UnityEngine;
using System.Collections;  
  
// Unload Unity when the user clicks the button. Exit is not applied to the application.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 75), "Unload"))
            Application.Unload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html)();
    }  
  
    static void OnUnload()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Unloading the Player");
    }  
  
    [RuntimeInitializeOnLoadMethod]
    static void RunOnStart()
    {
        Application.unloading[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unloading.html) += OnUnload;
    }
}

```

Additional resources: [Application.Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html).
* * *
