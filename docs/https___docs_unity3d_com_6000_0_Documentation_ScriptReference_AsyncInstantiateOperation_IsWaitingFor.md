* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.IsWaitingForSceneActivation.html

#  [AsyncInstantiateOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.html).IsWaitingForSceneActivation
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
public bool IsWaitingForSceneActivation(); 
### Returns
**bool** True if the operation is waits for user to allow the scene activation. 
### Description
This property can be true only if allowSceneActivation is set to false, and if the operation has already completed everything needed for object instantiation except for the main thread integrating the objects and calling their Awake methods. Users can set allowSceneActivation to true to trigger the activation or call the Cancel method to cancel instantiation.
* * *
