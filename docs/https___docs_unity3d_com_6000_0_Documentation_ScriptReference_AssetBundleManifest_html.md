* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html

# AssetBundleManifest
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.AssetBundleModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AssetBundleModule.html)
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
Manifest for all the AssetBundles in the build.
Additional resources: [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html), [AssetBundle.GetAllAssetNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.GetAllAssetNames.html)
### Public Methods
Method | Description  
---|---  
[GetAllAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.GetAllAssetBundles.html) | Get all the AssetBundles in the manifest.  
[GetAllAssetBundlesWithVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.GetAllAssetBundlesWithVariant.html) | Get all the AssetBundles with variant in the manifest.  
[GetAllDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.GetAllDependencies.html) | Get all the dependent AssetBundles for the given AssetBundle.  
[GetAssetBundleHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.GetAssetBundleHash.html) | Get the hash for the given AssetBundle.  
[GetDirectDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.GetDirectDependencies.html) | Get the direct dependent AssetBundles for the given AssetBundle.  
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
