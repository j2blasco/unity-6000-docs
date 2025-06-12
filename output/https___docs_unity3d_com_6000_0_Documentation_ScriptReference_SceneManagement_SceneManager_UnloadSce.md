* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).UnloadSceneAsync
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
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UnloadSceneAsync(int sceneBuildIndex); 
## Declaration
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UnloadSceneAsync(string sceneName); 
## Declaration
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UnloadSceneAsync([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
## Declaration
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UnloadSceneAsync(int sceneBuildIndex, [SceneManagement.UnloadSceneOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.html) options); 
## Declaration
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UnloadSceneAsync(string sceneName, [SceneManagement.UnloadSceneOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.html) options); 
## Declaration
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UnloadSceneAsync([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene, [SceneManagement.UnloadSceneOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
sceneBuildIndex | Index of the Scene in BuildSettings.  
sceneName | Name or path of the Scene to unload.  
scene | Scene to unload.  
options | Scene unloading options.  
### Returns
**AsyncOperation** Use the [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) to determine if the operation has completed. 
### Description
Destroys all GameObjects associated with the given Scene and removes the Scene from the SceneManager.
The given Scene name can either be the full Scene path, the path shown in the Build Settings window or just the Scene name. If only the Scene name is given this will unload the first Scene in the list that matches. If you have multiple Scenes with same name but different paths, you should use the full Scene path. Examples of supported formats:  
`"Scene1"`  
`"Scene2"`  
`"Scenes/Scene3"`  
`"Scenes/Others/Scene3"`  
`"Assets/scenes/others/scene3.unity"`  
  
**Note:** This is case-insensitive and due to it being async there are no guarantees about completion time.   
**Note:** Assets are currently not unloaded. In order to free up asset memory call [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).   
**Note:** It is not possible to [UnloadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html) if there are no scenes to load. For example, a project that has a single scene cannot use this static member.
* * *
