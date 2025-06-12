* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.html

# UnloadSceneOptions
enumeration
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
Scene unloading options passed to SceneManager.UnloadScene.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.None.html) | Unload the scene without any special options.  
[UnloadAllEmbeddedSceneObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.UnloadAllEmbeddedSceneObjects.html) | Unloads all objects that are loaded from the scene's serialized file. Without this flag, only GameObject and Components within the scene's hierarchy are unloaded.Note: Objects that are dynamically created during the build process can be embedded in the scene's serialized file. This can occur when asset types are created and referenced inside the scene's post-processor callback. Some examples of these types are textures, meshes, and scriptable objects. Assets from your assets folder are not embedded in the scene's serialized file. Note: This flag does not unload assets which can be referenced by other scenes.  
* * *
