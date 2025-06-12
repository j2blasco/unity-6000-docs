* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CollectInSceneAssets.html

#  [InSceneAssetUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.html).CollectInSceneAssets
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
public static InSceneAssetInformation[] CollectInSceneAssets(GameObject[] gameObjects); 
## Declaration
public static InSceneAssetInformation[] CollectInSceneAssets([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
gameObjects | The GameObjects to traverse and collect in-scene asset references for.  
scene | The scene to traverse and collect in-scene asset references for.  
### Returns
**InSceneAssetInformation[]** Information about the in-scene assets referenced by the provided GameObjects or the GameObjects of the provided scene. 
### Description
Gets information about in-scene assets referenced by the given GameObjects or scene.
Checks the entire hierarchy of each provided GameObject or GameObjects of the provided scene, their respective child GameObjects, and components to collect all in-scene assets referenced by them.  
  
Additional resources: [InSceneAssetInformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetInformation.html).
* * *
