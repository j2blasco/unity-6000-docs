* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-developerConsoleVisible.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).developerConsoleVisible
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
developerConsoleVisible; 
### Description
Controls whether the development console is visible.
The developer console is a window that can appear when a development build of your project is running. It is similar to the Console window in the Editor, but appears at runtime. The development console automatically appears when an error has been logged, and [Debug.developerConsoleEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-developerConsoleEnabled.html) is true. For example:
```
using UnityEngine;  
  
public class LogErrorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("I am an Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html)");
    }
}

```

You can close the development console when opened by using:
```
using UnityEngine;  
  
public class CloseDevConsoleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.developerConsoleVisible[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-developerConsoleVisible.html) = false;
    }
}

```

You can reopen the development console if at least one entry exists in the console by using:
```
using UnityEngine;  
  
public class OpenDevConsoleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.developerConsoleVisible[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-developerConsoleVisible.html) = true;
    }
}

```

* * *
