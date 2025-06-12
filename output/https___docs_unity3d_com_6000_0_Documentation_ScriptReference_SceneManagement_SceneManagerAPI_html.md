* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.html

# SceneManagerAPI
class in UnityEngine.SceneManagement
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
Derive from this base class to provide alternative implementations to the C# behavior of specific [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html) methods.
The example provided logs if scene loading is done by index and logs a warning to switch to loading by scene path.
```
using UnityEngine;
using Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) = UnityEngine.Debug;
using UnityEngine.SceneManagement;  
  
public class SceneIndexLogger : SceneManagerAPI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.html)
{
    [RuntimeInitializeOnLoadMethod]
    static void OnRuntimeMethodLoad()
    {
        SceneManagerAPI.overrideAPI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI-overrideAPI.html) = new SceneIndexLogger();
    }  
  
    protected override int GetNumScenesInBuildSettings()
    {
        Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("SceneManager.GetNumScenesInBuildSettings() called, please load scenes by path to avoid issues when scenes are reordered.");
        return base.GetNumScenesInBuildSettings();
    }  
  
    protected override Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) GetSceneByBuildIndex(int buildIndex)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"SceneManager.GetSceneByBuildIndex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByBuildIndex.html)(buildIndex = {buildIndex}) called, please load scenes by path to avoid issues when scenes are reordered.");
        return base.GetSceneByBuildIndex(buildIndex);
    }
}

```

### Static Properties
Property | Description  
---|---  
[overrideAPI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI-overrideAPI.html) | The specific SceneManagerAPI instance to use to handle overridden SceneManager methods.  
### Protected Methods
Method | Description  
---|---  
[GetNumScenesInBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.GetNumScenesInBuildSettings.html) | Override for customizing the behavior of the SceneManager.sceneCountInBuildSettings function.  
[GetSceneByBuildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.GetSceneByBuildIndex.html) | Override for customizing the behavior of the SceneManager.GetSceneByBuildIndex function.  
[LoadFirstScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.LoadFirstScene.html) | Override for customizing the behavior of loading the first Scene in a stub player build.  
[LoadSceneAsyncByNameOrIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.LoadSceneAsyncByNameOrIndex.html) | Override for customizing the behavior of the SceneManager.LoadScene and SceneManager.LoadSceneAsync functions.  
[UnloadSceneAsyncByNameOrIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.UnloadSceneAsyncByNameOrIndex.html) | Override for customizing the behavior of the SceneManager.UnloadSceneAsync function.  
* * *
