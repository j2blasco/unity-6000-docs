* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html

# EditorBuildSettings
class in UnityEditor
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
This class allows you to modify the Editor [Build Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html) via script.
See [EditorBuildSettings.scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-scenes.html) for an example of how to use this class. Additional resources: [EditorBuildSettingsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html), [EditorUserBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html), [BuildPlayerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html).
### Static Properties
Property | Description  
---|---  
[globalScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-globalScenes.html) | The list of scenes used by all platform profiles and build profiles that do not override global scenes.  
[scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-scenes.html) | The list of scenes used in the active platform profile or build profile that should be inculded in the build.  
[UseParallelAssetBundleBuilding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.UseParallelAssetBundleBuilding.html) | Enables multi-process AssetBundle building. Additional resources: BuildPipeline.BuildAssetBundles   
### Static Methods
Method | Description  
---|---  
[AddConfigObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.AddConfigObject.html) | Store a reference to a config object by name. The object must be an asset in the project, otherwise it will not be saved when the editor is restarted or scripts are reloaded. To avoid name conflicts with other packages, it is recommended that names are qualified by a namespace, i.e. "company.package.name".  
[GetConfigObjectNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.GetConfigObjectNames.html) | Return a string array containing the names of all stored config object references.  
[RemoveConfigObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.RemoveConfigObject.html) | Remove a config object reference by name.  
[TryGetConfigObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.TryGetConfigObject.html) | Retrieve a config object reference by name.  
### Events
Event | Description  
---|---  
[sceneListChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-sceneListChanged.html) | A delegate called whenever EditorBuildSettings.scenes is set.  
### Inherited Members
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
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
