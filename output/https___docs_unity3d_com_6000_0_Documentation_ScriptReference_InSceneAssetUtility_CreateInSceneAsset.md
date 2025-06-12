* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CreateInSceneAssetFromAsset.html

#  [InSceneAssetUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.html).CreateInSceneAssetFromAsset
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
public static Object CreateInSceneAssetFromAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) asset, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObjectReferencingAsset); 
### Parameters
Parameter | Description  
---|---  
asset | The persistent asset to convert to an in-scene asset.  
gameObjectReferencingAsset | The GameObject that is referencing the asset either directly or through its children in its hierarchy.  
### Returns
**Object** An in-scene asset object referenced by `gameObjectReferencingAsset` if successful, otherwise null. 
### Description
Creates an in-scene asset object from the given project asset.
Given a project asset and a GameObject referencing it, the function clones the asset, makes it non-persistent and remaps the GameObject's references to the new in-scene asset object.  
  
Additional resources: [InSceneAssetUtility.CreateAssetFromInSceneAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CreateAssetFromInSceneAsset.html).
* * *
