* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.TryGetGizmoInfo.html

#  [GizmoUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.html).TryGetGizmoInfo
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
public static bool TryGetGizmoInfo(Type type, out [GizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo.html) info); 
### Parameters
Parameter | Description  
---|---  
type | The type to get GizmoInfo for.  
info | The output argument will contain a valid GizmoInfo when this function returns true.  
### Returns
**bool** Returns true if Unity has a gizmo or icon registered for the requested type. 
### Description
Get a GizmoInfo for a type if it exists.
Type must be assignable to [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).
* * *
