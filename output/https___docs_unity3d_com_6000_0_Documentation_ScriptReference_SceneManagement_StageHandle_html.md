* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageHandle.html

# StageHandle
struct in UnityEditor.SceneManagement
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
### Description
Struct that represents a stage handle.
A stage is an editing context which includes a collection of Scenes. The main stage contains all the currently open regular Scenes, while a Prefab stage contains a preview Scene used solely for editing the Prefab in.  
  
The breadcrumbs which are shown in the Scene view when in Prefab Mode each represent a stage.
### Public Methods
Method | Description  
---|---  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageHandle.Contains.html) | Does the stage contain the given GameObject?  
[FindComponentOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageHandle.FindComponentOfType.html) | Returns the first active loaded object of the given type.  
[FindComponentsOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageHandle.FindComponentsOfType.html) | Returns a list of all active loaded objects of the given type.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageHandle.IsValid.html) | Is this stage handle valid?  
* * *
