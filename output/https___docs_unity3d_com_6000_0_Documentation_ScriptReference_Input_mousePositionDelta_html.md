* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePositionDelta.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).mousePositionDelta
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) mousePositionDelta; 
### Description
The current mouse position delta in pixel coordinates. (Read Only).
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
[Input.mousePositionDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePositionDelta.html) is a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) for compatibility with functions that have [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) arguments. The z component of the [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) is always 0.  
  
Note: You should use [Input.mousePositionDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePositionDelta.html) instead of [[Input.mousePosition] when [Cursor.lockState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html) is set to [CursorLockMode.Locked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.Locked.html), since when cursor is locked, the mouse position remains stationary when moving the mouse, thus only position delta gives you the information about mouse movement.
* * *
