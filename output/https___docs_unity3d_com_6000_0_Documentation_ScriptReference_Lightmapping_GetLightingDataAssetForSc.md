* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetLightingDataAssetForScene.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).GetLightingDataAssetForScene
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
public static [LightingDataAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingDataAsset.html) GetLightingDataAssetForScene([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | The scene to get the LightingDataAsset for.  
### Returns
**LightingDataAsset** The LightingDataAsset associated with the scene. 
### Description
Gets the LightingDataAsset associated with a specific scene. This method will return null if the scene has no LightingDataAsset, or the scene is invalid.
Additional resources: [Lightmapping.SetLightingDataAssetForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingDataAssetForScene.html).
* * *
