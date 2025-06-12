* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html

# EditorSceneManager
class in UnityEditor.SceneManagement
/
Inherits from:[SceneManagement.SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html)
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
Scene management in the Editor.
### Static Properties
Property | Description  
---|---  
[DefaultSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.DefaultSceneCullingMask.html) | Use SceneCullingMasks.DefaultSceneCullingMask instead.  
[playModeStartScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-playModeStartScene.html) | Loads this SceneAsset when you start Play Mode.  
[preventCrossSceneReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-preventCrossSceneReferences.html) | Controls whether cross-Scene references are allowed in the Editor.  
[previewSceneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-previewSceneCount.html) | The current amount of active preview Scenes.  
### Static Methods
Method | Description  
---|---  
[CalculateAvailableSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.CalculateAvailableSceneCullingMask.html) | Go through all Scenes and find the smallest unused bit in the unition of all Scene culling masks.  
[ClosePreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.ClosePreviewScene.html) | Closes a preview Scene created by NewPreviewScene or OpenPreviewScene.  
[CloseScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.CloseScene.html) | Close the Scene. If removeScene flag is true, the closed Scene will also be removed from EditorSceneManager.  
[DetectCrossSceneReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.DetectCrossSceneReferences.html) | Detects cross-Scene references in a Scene.  
[EnsureUntitledSceneHasBeenSaved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.EnsureUntitledSceneHasBeenSaved.html) | Shows a save dialog if an Untitled Scene exists in the current Scene manager setup.  
[GetSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.GetSceneCullingMask.html) | Return the culling mask set on the given Scene.  
[GetSceneManagerSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.GetSceneManagerSetup.html) | Returns the current setup of the SceneManager.  
[IsPreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.IsPreviewScene.html) | Is the Scene a preview Scene?  
[IsPreviewSceneObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.IsPreviewSceneObject.html) | Is this object part of a preview Scene?  
[LoadSceneAsyncInPlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.LoadSceneAsyncInPlayMode.html) | This method allows you to load a Scene during playmode in the editor, without requiring the Scene to be included in the Build Settings Scene list.  
[LoadSceneInPlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.LoadSceneInPlayMode.html) | This method allows you to load a Scene during playmode in the editor, without requiring the Scene to be included in the Build Settings Scene list.  
[MarkAllScenesDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.MarkAllScenesDirty.html) | Mark all the loaded Scenes as modified.  
[MarkSceneDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.MarkSceneDirty.html) | Mark the specified Scene as modified.  
[MoveSceneAfter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.MoveSceneAfter.html) | Allows you to reorder the Scenes currently open in the Hierarchy window. Moves the source Scene so it comes after the destination Scene.  
[MoveSceneBefore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.MoveSceneBefore.html) | Allows you to reorder the Scenes currently open in the Hierarchy window. Moves the source Scene so it comes before the destination Scene.  
[NewPreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewPreviewScene.html) | Creates a new preview Scene. Any object added to a preview Scene will only be rendered in that Scene.  
[NewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewScene.html) | Create a new Scene.  
[OpenPreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.OpenPreviewScene.html) | Opens a Scene Asset in a preview Scene.  
[OpenScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.OpenScene.html) | Open a Scene in the Editor.  
[RestoreSceneManagerSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.RestoreSceneManagerSetup.html) | Restore the setup of the SceneManager.  
[SaveCurrentModifiedScenesIfUserWantsTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveCurrentModifiedScenesIfUserWantsTo.html) | Asks the user if they want to save the current open modified Scene or Scenes in the Hierarchy.  
[SaveModifiedScenesIfUserWantsTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveModifiedScenesIfUserWantsTo.html) | Asks whether the modfied input Scenes should be saved.  
[SaveOpenScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveOpenScenes.html) | Save all open Scenes.  
[SaveScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveScene.html) | Save a Scene.  
[SaveScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveScenes.html) | Save a list of Scenes.  
[SetSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SetSceneCullingMask.html) | Set the culling mask on this scene to this value. Cameras will only render objects in Scenes that have the same bits set in their culling mask.  
### Events
Event | Description  
---|---  
[activeSceneChangedInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-activeSceneChangedInEditMode.html) | Subscribe to this event to get notified when the active Scene has changed in Edit mode in the Editor.  
[newSceneCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-newSceneCreated.html) | This event is called after a new Scene has been created.  
[sceneClosed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneClosed.html) | This event is called after a Scene has been closed in the editor.  
[sceneClosing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneClosing.html) | This event is called before closing an open Scene after you have requested that the Scene is closed.  
[sceneDirtied](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneDirtied.html) | This event is called after a Scene has been modified in the editor.  
[sceneManagerSetupRestored](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneManagerSetupRestored.html) | This can be useful to get notified when the SceneManager's scenes are replaced with a set of new scenes from calls to RestoreSceneManagerSetup.Use the scenes argument to check what scenes has just been opened.Additional resources: SceneManagerSetupRestoredCallback.  
[sceneOpened](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneOpened.html) | This event is called after a Scene has been opened in the editor.  
[sceneOpening](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneOpening.html) | This event is called before opening an existing Scene.  
[sceneSaved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneSaved.html) | This event is called after a Scene has been saved.  
[sceneSaving](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneSaving.html) | This event is called before a Scene is saved disk after you have requested the Scene to be saved.  
### Delegates
Delegate | Description  
---|---  
[NewSceneCreatedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewSceneCreatedCallback.html) | Callbacks of this type which have been added to the newSceneCreated event are called after a new Scene has been created.  
[SceneClosedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneClosedCallback.html) | Callbacks of this type which have been added to the sceneClosed event are called immediately after the Scene has been closed.  
[SceneClosingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneClosingCallback.html) | Callbacks of this type which have been added to the sceneClosing event are called just before a Scene is closed.  
[SceneDirtiedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneDirtiedCallback.html) | Callbacks of this type which have been added to the sceneDirtied event are called after a Scene changes from being unmodified to being modified.  
[SceneManagerSetupRestoredCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneManagerSetupRestoredCallback.html) | Callbacks of this type which have been added to the sceneManagerSetupRestored event are called after RestoreSceneManagerSetup has been called.  
[SceneOpenedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneOpenedCallback.html) | Callbacks of this type which have been added to the sceneOpened event are called after a Scene has been opened.  
[SceneOpeningCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneOpeningCallback.html) | Callbacks of this type which have been added to the sceneOpening event are called just before opening a Scene.  
[SceneSavedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneSavedCallback.html) | Callbacks of this type which have been added to the sceneSaved event are called after a Scene has been saved.  
[SceneSavingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneSavingCallback.html) | Callbacks of this type which have been added to the sceneSaving event are called just before the Scene is saved.  
### Inherited Members
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
