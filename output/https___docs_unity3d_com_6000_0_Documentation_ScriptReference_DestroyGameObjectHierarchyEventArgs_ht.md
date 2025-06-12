* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs.html

# DestroyGameObjectHierarchyEventArgs
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
A change of this type indicates that a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and the entire hierarchy below it has been destroyed. This happens for example when [Undo.DestroyObjectImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.DestroyObjectImmediate.html) is used with an [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
### Properties
Property | Description  
---|---  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs-instanceId.html) | The instance ID of the GameObject that has been destroyed.  
[parentInstanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs-parentInstanceId.html) | The instance ID for the parent GameObject of the GameObject that has been destroyed.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs-scene.html) | The scene containing the GameObject that has been destroyed.  
### Constructors
Constructor | Description  
---|---  
[DestroyGameObjectHierarchyEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs-ctor.html) | Constructs a new instance.  
* * *
