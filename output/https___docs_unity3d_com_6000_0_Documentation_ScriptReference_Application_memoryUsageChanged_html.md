* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-memoryUsageChanged.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).memoryUsageChanged
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
Informs about significant changes in the application's memory usage.
This event occurs when there are significant changes in the application's memory usage, such as an increase to a dangerous level or a drop to a much safer level.  
  
You can use this event to balance your application's memory usage for device capability. For example, you can lower the resource intensity of your application when memory usage becomes critical.  
  
iOS, Android, and Universal Windows Platform (UWP) support this event, but not every platform supports all possible [ApplicationMemoryUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.html) values. 
  * Android supports [Medium](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Medium.html), [High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.High.html), and [Critical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Critical.html).   
**Note:** When targeting [GameActivity](https://developer.android.com/games/agdk/game-activity), only [Critical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Critical.html) is supported.
  * iOS supports [Critical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Critical.html).
  * UWP supports [Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Low.html), [Medium](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Medium.html), [High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.High.html), and [Critical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Critical.html).


```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;  
  
public class Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Application.memoryUsageChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-memoryUsageChanged.html) += OnMemoryUsageChanged;
    }  
  
    void OnMemoryUsageChanged(in ApplicationMemoryUsageChange[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsageChange.html) newUsage)
    {
        if (newUsage.memoryUsage == ApplicationMemoryUsage.Critical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Critical.html))
        {
            // release resources here
            Resources.UnloadUnusedAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html)();
            GC.Collect();
        }
    }
}

```

This code sample shows how to perform garbage collection if the application is critically low on memory.
* * *
