* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-resolutions.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).resolutions
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
resolutions; 
### Description
Returns all full-screen resolutions that the monitor supports (Read Only).
Unity returns the resolutions the monitor supports and sorts them by width and then by ascending resolution. **Important:** When you use [FullScreenMode.ExclusiveFullScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.ExclusiveFullScreen.html) you should use `Screen.resolutions` to determine which resolution to pass to [Screen.SetResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetResolution.html) because `FullScreenMode.ExclusiveFullScreen` only works with supported resolutions. If you pass a non-supported resolution, it has a severe impact on performance. All other fullscreen modes support arbitrary resolutions without performance penalties. 
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Resolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html)[] resolutions = Screen.resolutions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-resolutions.html);  
  
        // Print the resolutions
        foreach (var res in resolutions)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(res.width + "x" + res.height + " : " + res.refreshRateRatio);
        }
    }
}

```

**Note:** On MacOS devices that have a notch area, the resolution array contains resolutions that don't fit under the notch area and will be resized when applied.   
  
Additional resources: [Resolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html) structure, [SetResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetResolution.html).
* * *
