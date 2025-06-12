* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.ApplyGizmoInfo.html

#  [GizmoUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.html).ApplyGizmoInfo
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
public static void ApplyGizmoInfo([GizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo.html) info, bool addToRecentlyChanged); 
### Parameters
Parameter | Description  
---|---  
info | The GizmoInfo to apply.  
addToRecentlyChanged | Set true to append this component to the "Recently Changed" list in the Annotation Window.  
### Description
Apply [gizmoEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo-gizmoEnabled.html) and [iconEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo-iconEnabled.html) for a [GizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo.html) object.
This is equivalent to calling [SetGizmoEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.SetGizmoEnabled.html) and [SetIconEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.SetIconEnabled.html).
* * *
