* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SyncTransforms.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).SyncTransforms
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
public static void SyncTransforms(); 
### Description
Apply Transform changes to the physics engine.
When a [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component changes, any [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) or [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) on that [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) or its children may need to be repositioned, rotated or scaled depending on the change to the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html). Use this function to flush those changes to the physics engine manually.
* * *
