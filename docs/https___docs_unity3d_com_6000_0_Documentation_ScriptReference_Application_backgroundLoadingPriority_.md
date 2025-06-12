* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-backgroundLoadingPriority.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).backgroundLoadingPriority
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
[ThreadPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.html) backgroundLoadingPriority; 
### Description
Priority of background loading thread.
Lets you control how long it takes to load data asynchronously vs performance impact on the game while loading in the background.  
  
Asynchronous load functions that load objects ([Resources.LoadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAsync.html), [AssetBundle.LoadAssetAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAssetAsync.html), AssetBundle.LoadAllAssetAsync), scenes ([SceneManager.LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html)) do data read and deserialization on a separate background loading thread and object integration on a main thread. _Integration_ depends on an object type and for textures, meshes means uploading data to the GPU, audio clips prepare data for playing.  
  
To avoid hiccups we limit _integration_ time on a main thread depending on [backgroundLoadingPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-backgroundLoadingPriority.html) value:  
- [ThreadPriority.Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.Low.html) - 2ms  
- [ThreadPriority.BelowNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.BelowNormal.html) - 4ms  
- [ThreadPriority.Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.Normal.html) - 10ms  
- [ThreadPriority.High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.High.html) - 50ms  
This value defines the maximum time all asynchronous operations can spend within a single frame on a main thread.  
  
The default value is [ThreadPriority.BelowNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.BelowNormal.html), however some platforms override it:
  * Universal Windows Platform - [ThreadPriority.High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.High.html)
  * Consoles - [ThreadPriority.Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.Normal.html)


Background loading thread uses [backgroundLoadingPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-backgroundLoadingPriority.html) directly.  
  
The Profiler marker **Application.Integrate Assets in Background** lets you optimize background loading. 
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example1()
    {
        // Load as much data as possible, as a result frame rate will drop.
        // Good for fast loading when showing progress bars.  
  
        Application.backgroundLoadingPriority[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-backgroundLoadingPriority.html) = ThreadPriority.High[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.High.html);
    }  
  
    void Example2()
    {
        // Load data very slowly and try not to affect performance of the game.
        // Good for loading in the background while the game is playing.  
  
        Application.backgroundLoadingPriority[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-backgroundLoadingPriority.html) = ThreadPriority.Low[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.Low.html);
    }
}

```

Additional resources: [ThreadPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.html) enum, [AsyncOperation.priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-priority.html).
* * *
