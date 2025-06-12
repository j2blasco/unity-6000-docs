* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DrawHandle.html

#  [ArcHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html).DrawHandle
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
public void DrawHandle(); 
### Description
A function to display this instance in the current handle camera using its current configuration.
Always write properties to the handle before calling this function. Place the calls to this function inside [EditorGUI.BeginChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html) and [EditorGUI.EndChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html) to detect user interaction and read the updated properties from the handle.  
  
Additional resources: [Editor.OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html), [Handles.SetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SetCamera.html).
* * *
