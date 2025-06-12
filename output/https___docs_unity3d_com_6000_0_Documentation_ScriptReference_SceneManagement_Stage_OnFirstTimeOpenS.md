* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnFirstTimeOpenStageInSceneView.html

#  [Stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html).OnFirstTimeOpenStageInSceneView
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
protected void OnFirstTimeOpenStageInSceneView([SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sceneView); 
### Parameters
Parameter | Description  
---|---  
sceneView | The Scene view the Stage is opened in.  
### Description
Unity calls this method the first time a Stage is opened for a specific Asset, for a specific Scene view.
Classes that inherit from Stage can implement this method to configure the Scene view in a suitable way for this Stage.
* * *
