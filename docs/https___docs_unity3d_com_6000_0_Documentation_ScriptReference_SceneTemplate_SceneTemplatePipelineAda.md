* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplatePipelineAdapter.AfterTemplateInstantiation.html

#  [SceneTemplatePipelineAdapter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplatePipelineAdapter.html).AfterTemplateInstantiation
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
public void AfterTemplateInstantiation([SceneTemplate.SceneTemplateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateAsset.html) sceneTemplateAsset, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene, bool isAdditive, string sceneName); 
### Parameters
Parameter | Description  
---|---  
sceneTemplateAsset | The Scene template Asset to instantiate.  
scene | The newly created Scene.  
isAdditive | When set to true, the new Scene is created in additive mode.  
sceneName | The path to the newly created Scene. If the template you instantiated does not have any cloneable dependencies, this can be empty.  
### Description
An event called after the Scene template is instantiated, and while the new Scene is still loaded.
* * *
