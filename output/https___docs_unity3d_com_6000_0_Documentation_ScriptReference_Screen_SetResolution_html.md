* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetResolution.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).SetResolution
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
public static void SetResolution(int width, int height, bool fullscreen); 
## Declaration
public static void SetResolution(int width, int height, [FullScreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.html) fullscreenMode); 
## Declaration
public static void SetResolution(int width, int height, [FullScreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.html) fullscreenMode, [RefreshRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RefreshRate.html) preferredRefreshRate); 
### Description
Switches the screen resolution.
A `width` by `height` resolution is used. If no matching resolution is supported, the closest one is used.  
  
If `preferredRefreshRate` is 0 (default) Unity switches to the highest refresh rate that the monitor supports.  
If `preferredRefreshRate` is not 0 Unity uses it if the monitor supports it, otherwise it chooses the highest supported one. Changing refresh rate is only supported when using exclusive full-screen mode.  
  
On Android `fullscreen` controls the `SYSTEM_UI_FLAG_LOW_PROFILE` flag to `View.setSystemUiVisibility`.  
  
To set a specific full-screen mode on a desktop platform, use the method overload that accepts the FullScreenMode parameter. Exclusive full-screen mode is only supported on Windows standalone player.  
  
If you use [multi-display](https://docs.unity3d.com/6000.0/Documentation/Manual/MultiDisplay.html), you can only use `Screen.SetResolution` to set the resolution of the primary screen.   
  
A resolution switch does not happen immediately; it happens when the current frame is finished.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to 640 x 480 full-screen
        Screen.SetResolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetResolution.html)(640, 480, true);
    }
}

```

Another example:
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to 640 x 480 full-screen at 60 hz
        Screen.SetResolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetResolution.html)(640, 480, FullScreenMode.ExclusiveFullScreen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.ExclusiveFullScreen.html), new RefreshRate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RefreshRate.html)() { numerator = 60, denominator = 1 });
    }
}

```

Another example:
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to 800 x 600 windowed
        Screen.SetResolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetResolution.html)(800, 600, false);
    }
}

```

Additional resources: [resolutions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-resolutions.html) property.
* * *
