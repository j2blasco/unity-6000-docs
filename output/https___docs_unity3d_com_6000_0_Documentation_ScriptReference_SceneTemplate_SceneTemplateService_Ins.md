* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.Instantiate.html

#  [SceneTemplateService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.html).Instantiate
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
public static [SceneTemplate.InstantiationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.InstantiationResult.html) Instantiate([SceneTemplate.SceneTemplateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateAsset.html) sceneTemplate, bool loadAdditively, string newSceneOutputPath); 
### Parameters
Parameter | Description  
---|---  
sceneTemplate | A Scene template Asset that contains the information required to instantiate the Scene.  
loadAdditively | Specifies whether the new Scene is created additively in the currently loaded Scene.  
newSceneOutputPath | The path to the new Scene created from the template. This is set only when the [SceneTemplateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateAsset.html) has cloneable dependencies, because in that case, the new Scene must be be saved on disk.  
### Returns
**InstantiationResult** The new [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and its [SceneTemplateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateAsset.html) counterpart. 
### Description
Instantiates a new Scene from a template.
* * *
