* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html

# GizmoType
enumeration
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
Determines how a gizmo is drawn or picked in the Unity editor.
The types can be combined together with an OR operator.  
  
Additional resources: [DrawGizmo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html).
### Properties
Property | Description  
---|---  
[Pickable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Pickable.html) | The gizmo can be picked in the editor.  
[NotInSelectionHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.NotInSelectionHierarchy.html) | Draw the gizmo if it is not selected and also no parent/ancestor is selected.  
[NonSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.NonSelected.html) | Draw the gizmo if it is not selected.  
[Selected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Selected.html) | Draw the gizmo if it is selected.  
[Active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Active.html) | Draw the gizmo if it is active (shown in the inspector).  
[InSelectionHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.InSelectionHierarchy.html) | Draw the gizmo if it is selected or it is a child/descendent of the selected.  
* * *
