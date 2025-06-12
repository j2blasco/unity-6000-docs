* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectStructureEventArgs.html

# ChangeGameObjectStructureEventArgs
struct in UnityEditor
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
A change of this type indicates that the structure of a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has changed. This happens when a component is added to or removed from the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) using [Undo.AddComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.AddComponent.html) or [Undo.DestroyObjectImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.DestroyObjectImmediate.html).
Note that multiple changes to the structure (e.g. multiple components added) may be represented by a single event.
### Properties
Property | Description  
---|---  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectStructureEventArgs-instanceId.html) | The instance ID of the GameObject that has been changed.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectStructureEventArgs-scene.html) | The Scene containing the GameObject that has been changed.  
### Constructors
Constructor | Description  
---|---  
[ChangeGameObjectStructureEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectStructureEventArgs-ctor.html) | Constructs a new instance.  
* * *
