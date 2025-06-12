* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.html

# InSceneAssetUtility
class in UnityEditor
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
Provides methods related to in-scene assets.
In-scene assets are scene objects that are referenced by one or more objects in a scene and are of an asset type. Examples of asset types include, but are not limited to, [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), and [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html). If in-scene assets are not converted to project assets (with [AssetDatabase.CreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html), for example), they are serialized inside scene files. This can cause unwanted increases in the scene file size. `InSceneAssetUtility` provides methods to identify and manage such objects.
### Static Methods
Method | Description  
---|---  
[CollectInSceneAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CollectInSceneAssets.html) | Gets information about in-scene assets referenced by the given GameObjects or scene.  
[CreateAssetFromInSceneAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CreateAssetFromInSceneAsset.html) | Creates a project asset from the given in-scene asset and saves it at the provided file path.  
[CreateInSceneAssetFromAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CreateInSceneAssetFromAsset.html) | Creates an in-scene asset object from the given project asset.  
[IsInSceneAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.IsInSceneAsset.html) | Checks if the given object is an in-scene asset.  
* * *
