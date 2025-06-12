* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.html

# ResourcesAPI
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
Derive from this base class to provide alternative implementations to the C# behavior of specific [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) methods.
The example provided logs the time taken to handle slower Resources APIs to the player or editor log.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Diagnostics;
using UnityEngine;
using Object = UnityEngine.Object;
using Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) = UnityEngine.Debug;  
  
public class ResourcesPerformanceLogger : ResourcesAPI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.html)
{
    [RuntimeInitializeOnLoadMethod]
    static void OnRuntimeMethodLoad()
    {
        ResourcesAPI.overrideAPI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI-overrideAPI.html) = new ResourcesPerformanceLogger();
    }  
  
    protected override Object[] FindObjectsOfTypeAll(Type systemTypeInstance)
    {
        Stopwatch timer = new Stopwatch();
        timer.Start();
        Object[] results = base.FindObjectsOfTypeAll(systemTypeInstance);
        timer.Stop();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"FindObjectsOfTypeAll({systemTypeInstance}) Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html): {timer.Elapsed}");
        return results;
    }  
  
    protected override Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) FindShaderByName(string name)
    {
        Stopwatch timer = new Stopwatch();
        timer.Start();
        Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) result = base.FindShaderByName(name);
        timer.Stop();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"FindShaderByName({name}) Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html): {timer.Elapsed}");
        return result;
    }  
  
    protected override Object[] LoadAll(string path, Type systemTypeInstance)
    {
        Stopwatch timer = new Stopwatch();
        timer.Start();
        Object[] results = base.LoadAll(path, systemTypeInstance);
        timer.Stop();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"LoadAll({path}, {systemTypeInstance}) Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html): {timer.Elapsed}");
        return results;
    }
}

```

### Static Properties
Property | Description  
---|---  
[overrideAPI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI-overrideAPI.html) | The specific ResourcesAPI instance to use to handle overridden Resources methods.  
### Protected Methods
Method | Description  
---|---  
[FindObjectsOfTypeAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.FindObjectsOfTypeAll.html) | Override for customizing the behavior of the Resources.FindObjectsOfTypeAll function.  
[FindShaderByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.FindShaderByName.html) | Override for customizing the behavior of the Shader.Find function.  
[Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.Load.html) | Override for customizing the behavior of the Resources.Load function.  
[LoadAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.LoadAll.html) | Override for customizing the behavior of the Resources.LoadAll function.  
[LoadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.LoadAsync.html) | Override for customizing the behavior of the Resources.LoadAsync function.  
[UnloadAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.UnloadAsset.html) | Override for customizing the behavior of the Resources.Unload function.  
* * *
