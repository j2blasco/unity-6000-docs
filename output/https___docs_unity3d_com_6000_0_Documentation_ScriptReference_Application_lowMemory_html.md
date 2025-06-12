* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-lowMemory.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).lowMemory
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
The `Application._lowMemory` event occurs when your application receives a low-memory notification from the device it is running on. 
This only occurs when your application is running in the foreground. You can release non-critical assets from memory (such as, textures and audio clips) to avoid the application from being terminated. You can also load smaller versions of such assets. In addtion, you should serialize any transient data to permanent storage to avoid data loss if the app is terminated.  
  
The `Application._lowMemory` event is supported on iOS, Android, and Universal Windows Platform (UWP) and it corresponds to the following callbacks on different platforms:
  * **iOS** : `UIApplicationDelegate applicationDidReceiveMemoryWarning`
  * **Android** : `onLowMemory(`) and `onTrimMemory(level == TRIM_MEMORY_RUNNING_CRITICAL)`
  * **UWP** : `MemoryManager.AppMemoryUsageIncreased (AppMemoryUsageLevel == OverLimit)`


**Note:** For UWP, this event does not occur on desktop and only works on memory constrained devices, such as HoloLens. The `OverLimit` threshold specified by the OS in this case is so high that it's not reasonably possible to reach it and trigger the event.  
  
Following example shows an example of handling the callback:
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;  
  
class LowMemoryTrigger : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    List<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)> _textures;  
  
    private void Start()
    {
        _textures = new List<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>();
        Application.lowMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-lowMemory.html) += OnLowMemory;
    }  
  
    private void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // allocate textures until we run out of memory
        _textures.Add(new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(256, 256));
    }  
  
    private void OnLowMemory()
    {
        // release all cached textures
        _textures = new List<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>();
        Resources.UnloadUnusedAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html)();
    }
}

```

* * *
