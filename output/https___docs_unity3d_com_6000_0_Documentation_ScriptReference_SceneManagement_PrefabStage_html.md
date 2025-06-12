* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.html

# PrefabStage
class in UnityEditor.SceneManagement
/
Inherits from:[SceneManagement.PreviewSceneStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PreviewSceneStage.html)
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
The PrefabStage class represents an editing context for Prefab Assets.
A stage is an editing context which includes a collection of Scenes. The main stage contains all the currently open regular Scenes, while a Prefab stage contains a preview Scene used solely for editing the Prefab in.  
  
The breadcrumbs which are shown in the Scene view when in Prefab Mode each represent a stage. Those with a Prefab icon represent Prefab stages.
### Properties
Property | Description  
---|---  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-assetPath.html) | The asset path where the Prefab Asset file is stored, relative to the project root.  
[mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-mode.html) | The Prefab Stage can be opened either in isolation or in context.  
[openedFromInstanceObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-openedFromInstanceObject.html) | A GameObject inside the Prefab instance that you opened Prefab Mode through.  
[openedFromInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-openedFromInstanceRoot.html) | The root of the Prefab instance that you opened Prefab Mode through.  
[prefabContentsRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-prefabContentsRoot.html) | The root GameObject of the loaded Prefab Asset contents.  
### Public Methods
Method | Description  
---|---  
[ClearDirtiness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.ClearDirtiness.html) | Clear the dirtyness flag for the Prefab stage.  
[IsPartOfPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.IsPartOfPrefabContents.html) | Returns true if the given GameObject is part of the loaded Prefab Asset contents in the Prefab stage.  
### Events
Event | Description  
---|---  
[prefabSaved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-prefabSaved.html) | Callback that is invoked whenever the contents of a Prefab stage has been saved.  
[prefabSaving](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-prefabSaving.html) | Callback that's invoked whenever the contents of a Prefab stage is about to be saved.  
[prefabStageClosing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-prefabStageClosing.html) | Callback that's invoked whenever a Prefab stage is about to be opened.  
[prefabStageDirtied](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-prefabStageDirtied.html) | Callback that's invoked whenever a Prefab stage changes from unmodified to modified.  
[prefabStageOpened](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage-prefabStageOpened.html) | Callback that's invoked whenever a Prefab stage has been opened.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PreviewSceneStage-scene.html) | The preview Scene this stage controls. Stage content should be moved into this Scene.  
[stageHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PreviewSceneStage-stageHandle.html) | See Stage.stageHandle.  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage-assetPath.html) | The path of the Asset file associated with the stage, relative to the project root folder.  
[stageHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage-stageHandle.html) | The StageHandle struct for this stage.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
[FindComponentOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.FindComponentOfType.html) | Returns the first active loaded object of the given type.  
[FindComponentsOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.FindComponentsOfType.html) | Returns a list of all active loaded objects of the given type.  
[GetCombinedSceneCullingMaskForCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.GetCombinedSceneCullingMaskForCamera.html) | Gets the Scene culling mask from this Stage.  
### Protected Methods
Method | Description  
---|---  
[OnCloseStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PreviewSceneStage.OnCloseStage.html) | Unity calls this method when the Stage is closed. Classes that inherit from PreviewSceneStage should implement cleanup logic in this method.  
[OnOpenStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PreviewSceneStage.OnOpenStage.html) | Unity calls this method when the Stage is opened. Classes that inherit from PreviewSceneStage should implement initialization logic in this method.  
[CreateHeaderContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.CreateHeaderContent.html) | Creates the header content for this Stage. Both the Hierarchy window header and Scene view breadcrumb bar use this content.  
[GetHashForStateStorage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.GetHashForStateStorage.html) | Unity calls this method to get a hash code that is used to save the state of the Stage to disk.  
[OnCloseStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnCloseStage.html) | Unity calls this method when the Stage is closed. Classes that inherit from Stage should implement cleanup logic in this method.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnDisable.html) | See ScriptableObject.OnDisable.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnEnable.html) | See ScriptableObject.OnEnable.  
[OnFirstTimeOpenStageInSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnFirstTimeOpenStageInSceneView.html) | Unity calls this method the first time a Stage is opened for a specific Asset, for a specific Scene view.  
[OnOpenStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnOpenStage.html) | Unity calls this method when the Stage is opened. Classes that inherit from Stage should implement initialization logic in this method.  
[OnReturnToStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnReturnToStage.html) | Unity calls this method when you return to a Stage that is already open.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
