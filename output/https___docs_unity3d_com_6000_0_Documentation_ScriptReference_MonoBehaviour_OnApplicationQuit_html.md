* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationQuit.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnApplicationQuit()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Sent to all GameObjects before the application quits.
In the Editor, Unity calls this message when playmode is stopped.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnApplicationQuit()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Application[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) ending after " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + " seconds");
    }
}

```

**Note:** iOS applications are usually suspended and do not quit. For iOS builds, enable the "`Exit on Suspend`" property in Player Settings to make the application quit and not suspend, otherwise you might not see this call. If you do not enable the "`Exit on Suspend`" property then you will see calls to [OnApplicationPause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationPause.html) instead.  
  
On Windows Store Apps and Windows Phone 8.1 there is no application quit event. Use the [OnApplicationFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html) event when focusStatus equals `false`.  
On WebGL it is not possible to implement [OnApplicationQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationQuit.html) because of the way browser tabs close. For a workaround, see the Unity User Manual documentation on [Interacting with browser scripting in WebGL](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html).  
  
**Warning** : If the user suspends your application on a mobile platform, the operating system can quit the application to free up resources. In this case, depending on the operating system, Unity might be unable to call this method. On mobile platforms, it is best practice to not rely on this method to save the state of your application. Instead, consider every loss of application focus as the exit of the application and use [MonoBehaviour.OnApplicationFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html) to save any data. 
* * *
