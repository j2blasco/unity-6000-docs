* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVersion.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).graphicsDeviceVersion
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
graphicsDeviceVersion; 
### Description
The graphics API type and driver version used by the graphics device (Read Only).
Returns a string identifying low-level graphics API kind and driver version. In most cases when you need to detect which graphics API is being used it is much easier to use [SystemInfo.graphicsDeviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceType.html).  
  
In case of OpenGL API, the returned string will contain "`OpenGL`" followed by version in "`major.minor`" format, followed by full version string in square brackets.  
  
In case of Direct3D9 API, the returned string will contain "`Direct3D 9.0c`" followed by driver name and version in square brackets.  
  
In case of Direct3D11 API, the returned string will contain "`Direct3D 11.0`" followed by feature level in square brackets.  
  
Additional resources: [SystemInfo.graphicsDeviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceType.html), [SystemInfo.graphicsDeviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceName.html), [SystemInfo.graphicsDeviceVendor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendor.html).
```
using UnityEngine;
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints "OpenGL 2.0 [2.0 ATI-1.4.40]" on MacBook Pro running Mac OS X 10.4.8
        // Prints "Direct3D 9.0c [atiumdag.dll 7.14.10.471]" on MacBook Pro running Windows Vista
        print(SystemInfo.graphicsDeviceVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVersion.html));
    }
}

```

* * *
