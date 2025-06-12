* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html

# SceneManager
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
Scene management at run-time.
### Static Properties
Property | Description  
---|---  
[loadedSceneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-loadedSceneCount.html) | The number of loaded Scenes.  
[sceneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneCount.html) | The current number of Scenes.  
[sceneCountInBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneCountInBuildSettings.html) | Number of Scenes in Build Settings.  
### Static Methods
Method | Description  
---|---  
[CreateScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.CreateScene.html) | Create an empty new Scene at runtime with the given name.  
[GetActiveScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html) | Gets the currently active Scene.  
[GetSceneAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneAt.html) | Get the Scene at index in the SceneManager's list of loaded Scenes.  
[GetSceneByBuildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByBuildIndex.html) | Get a Scene struct from a build index.  
[GetSceneByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByName.html) | Searches through the Scenes loaded for a Scene with the given name.  
[GetSceneByPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByPath.html) | Searches all Scenes loaded for a Scene that has the given asset path.  
[LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html) | Loads the Scene by its name or index in Build Settings.  
[LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html) | Loads the Scene asynchronously in the background.  
[MergeScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.MergeScenes.html) | This will merge the source Scene into the destinationScene.  
[MoveGameObjectsToScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.MoveGameObjectsToScene.html) | Move multiple GameObjects, represented by a NativeArray of instance IDs, from their current Scene to a new Scene.  
[MoveGameObjectToScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.MoveGameObjectToScene.html) | Move a GameObject from its current Scene to a new Scene.  
[SetActiveScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.SetActiveScene.html) | Set the Scene to be active.  
[UnloadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html) | Destroys all GameObjects associated with the given Scene and removes the Scene from the SceneManager.  
### Events
Event | Description  
---|---  
[activeSceneChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-activeSceneChanged.html) | Subscribe to this event to get notified when the active Scene has changed.  
[sceneLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html) | Assign a custom callback to this event to get notifications when a Scene has loaded.  
[sceneUnloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html) | Add a delegate to this to get notifications when a Scene has unloaded.  
* * *
