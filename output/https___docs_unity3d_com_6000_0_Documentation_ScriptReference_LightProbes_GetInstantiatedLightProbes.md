* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInstantiatedLightProbesForScene.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).GetInstantiatedLightProbesForScene
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
public static [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html) GetInstantiatedLightProbesForScene([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | The scene to get the shared light probe data for.  
### Returns
**LightProbes** The cloned light probe data for the scene. 
### Description
Gets an instantiated clone of the `LightProbes` object for a specific scene.
If you modify the `LightProbes` object returned by this method, you will only affect the lighting of `scene`. Modifications will not affect assets.  
  
**Note** : This function automatically instantiates the `LightProbes` object and makes it unique to the passed scene. You need to destroy the `LightProbes` object when it's no longer needed. You can also use [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) to destroy a `LightProbes` object, which will be called automatically when you switch to a new scene.  
  
Additional resources: [LightProbes.GetSharedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetSharedLightProbesForScene.html).
* * *
