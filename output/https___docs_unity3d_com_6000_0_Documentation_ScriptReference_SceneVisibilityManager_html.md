* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html

# SceneVisibilityManager
class in UnityEditor
/
Inherits from:[ScriptableSingleton_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1.html)
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
Manages Scene Visibility in the editor.
### Public Methods
Method | Description  
---|---  
[AreAllDescendantsHidden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.AreAllDescendantsHidden.html) | Checks whether all the descendants of a GameObject are hidden.  
[AreAllDescendantsVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.AreAllDescendantsVisible.html) | Checks whether all the descendants are visible.  
[AreAnyDescendantsHidden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.AreAnyDescendantsHidden.html) | Checks whether any descendants are hidden.  
[DisableAllPicking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.DisableAllPicking.html) | Disables picking on all GameObjects.  
[DisablePicking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.DisablePicking.html) | Disables picking on a GameObject, or an Array of GameObjects, and their descendants.  
[EnableAllPicking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.EnableAllPicking.html) | Enables picking on all GameObjects.  
[EnablePicking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.EnablePicking.html) | Enables picking on a GameObject, or an array of GameObjects, and its descendants.  
[ExitIsolation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.ExitIsolation.html) | Exits Isolation Mode.  
[Hide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.Hide.html) | Hides a GameObject, or an Array of GameObjects, and their descendants.  
[HideAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.HideAll.html) | Hides all GameObjects.  
[IsCurrentStageIsolated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsCurrentStageIsolated.html) | Checks whether the current stage is in Isolation mode.  
[IsHidden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsHidden.html) | Checks the hidden state of a GameObject and, optionally, its descendants.  
[Isolate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.Isolate.html) | Isolates a GameObject and its descendants.  
[IsPickingDisabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsPickingDisabled.html) | Checks the picking state of a GameObject and, optionally, its descendants.  
[IsPickingDisabledOnAllDescendants](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsPickingDisabledOnAllDescendants.html) | Checks whether all the descendants of a GameObject have picking disabled.  
[IsPickingDisabledOnAnyDescendant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsPickingDisabledOnAnyDescendant.html) | Checks whether any descendants have picking disabled.  
[IsPickingEnabledOnAllDescendants](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsPickingEnabledOnAllDescendants.html) | Checks whether all the descendants are pickable.  
[Show](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.Show.html) | Shows a GameObject, or an array of GameObjects, and its descendants.  
[ShowAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.ShowAll.html) | Shows all GameObjects.  
[TogglePicking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.TogglePicking.html) | Toggles the picking ability of a GameObject.  
[ToggleVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.ToggleVisibility.html) | Toggles the visible state of a GameObject.  
### Events
Event | Description  
---|---  
[pickingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager-pickingChanged.html) | The event raised whenever the picking state of a GameObject changes.  
[visibilityChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager-visibilityChanged.html) | The event raised whenever the visibility of a GameObject changes.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[instance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1-instance.html) | Gets the instance of the Singleton. Unity creates the Singleton instance when this property is accessed for the first time. If you use the FilePathAttribute, then Unity loads the data on the first access as well.  
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Protected Methods
Method | Description  
---|---  
[Save](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1.Save.html) | Saves the current state of the ScriptableSingleton.  
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
[GetFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1.GetFilePath.html) | Get the file path where this ScriptableSingleton is saved to.  
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
