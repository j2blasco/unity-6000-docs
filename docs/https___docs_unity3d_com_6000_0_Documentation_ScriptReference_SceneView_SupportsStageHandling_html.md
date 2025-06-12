* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.SupportsStageHandling.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).SupportsStageHandling
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
protected bool SupportsStageHandling(); 
### Returns
**bool** True if the Scene view automatically reacts to stage changes. 
### Description
Override this method to control whether the Scene view should change when you switch from one stage to another stage.
By default, the Scene view changes when you switch from one stage to another. For example, the Scene view changes to render the Prefab Stage when you open that stage.
* * *
