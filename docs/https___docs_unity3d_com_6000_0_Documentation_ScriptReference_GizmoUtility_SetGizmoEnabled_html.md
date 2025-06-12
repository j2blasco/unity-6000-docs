* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.SetGizmoEnabled.html

#  [GizmoUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.html).SetGizmoEnabled
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
public static void SetGizmoEnabled(Type type, bool enabled, bool addToRecentlyChanged); 
### Parameters
Parameter | Description  
---|---  
type | The component type to render or hide gizmos.  
enabled | Set true to render gizmos in the Scene View, false to hide.  
addToRecentlyChanged | Set true to append this component to the "Recently Changed" list in the Annotation Window.  
### Description
Enable or disable gizmo rendering in the Scene View for a component type. Gizmos are the simple lines and guides drawn by component editors. For example, the Camera frustum guidelines are gizmos.
Type must be assignable to UnityEngine.Component.
* * *
