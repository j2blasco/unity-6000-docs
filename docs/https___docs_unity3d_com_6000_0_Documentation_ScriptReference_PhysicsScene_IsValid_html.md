* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.IsValid.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).IsValid
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
public bool IsValid(); 
### Returns
**bool** Is the physics scene valid? 
### Description
Gets whether the physics Scene is valid or not.
If the physics Scene is associated with a specific [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) which has been destroyed then the physics Scene is no longer valid. Note that the [Physics.defaultPhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultPhysicsScene.html) is always valid.
* * *
