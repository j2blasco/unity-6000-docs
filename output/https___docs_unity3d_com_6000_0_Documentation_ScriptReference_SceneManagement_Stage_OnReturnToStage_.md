* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.OnReturnToStage.html

#  [Stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html).OnReturnToStage
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
protected void OnReturnToStage(); 
### Description
Unity calls this method when you return to a Stage that is already open.
A Stage can remain open even after another Stage becomes the active Stage. Unity only closes a Stage once it's no longer visible in the Scene view breadcrumb bar. OnReturnToStage is called when clicking the breadcrumb of a stage that is not the current one.
* * *
