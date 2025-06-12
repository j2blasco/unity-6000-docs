* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateGameObjectHierarchyEventArgs.html

# CreateGameObjectHierarchyEventArgs
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
A change of this type indicates that a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has been created, possibly with additional objects below it in the hierarchy. This happens for example when [Undo.RegisterCreatedObjectUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html) is used with a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
### Properties
Property | Description  
---|---  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateGameObjectHierarchyEventArgs-instanceId.html) | The instance ID of the GameObject that has been created.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateGameObjectHierarchyEventArgs-scene.html) | The scene containing the GameObject that has been created.  
### Constructors
Constructor | Description  
---|---  
[CreateGameObjectHierarchyEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateGameObjectHierarchyEventArgs-ctor.html) | Constructs a new instance.  
* * *
