* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeChildrenOrderEventArgs.html

# ChangeChildrenOrderEventArgs
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
A change of this type indicates that a GameObject's children have been reordered. This happens when [Undo.RegisterChildrenOrderUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterChildrenOrderUndo.html) is called or when reordering a child in the hierarchy under the same parent.
### Properties
Property | Description  
---|---  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeChildrenOrderEventArgs-instanceId.html) | The instance ID of the parent GameObject whose children have been reordered. Note that this is not the instance ID of the Transform component.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeChildrenOrderEventArgs-scene.html) | The Scene containing the GameObject whose children were reordered.  
### Constructors
Constructor | Description  
---|---  
[ChangeChildrenOrderEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeChildrenOrderEventArgs-ctor.html) | Constructs a new instance.  
* * *
