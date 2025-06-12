* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.IsInSceneAsset.html

#  [InSceneAssetUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.html).IsInSceneAsset
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
public static bool IsInSceneAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) sourceObject); 
### Parameters
Parameter | Description  
---|---  
sourceObject | The object to check.  
### Returns
**bool** True if `sourceObject` is a an in-scene asset. 
### Description
Checks if the given object is an in-scene asset.
In-scene assets are scene objects that are referenced by one or more objects in a scene and are of an asset type. Examples of asset types include, but are not limited to, [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), and [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html).   
  
Additional resources: [InSceneAssetUtility.CollectInSceneAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CollectInSceneAssets.html).
* * *
