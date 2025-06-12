* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSelectionFrame.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawSelectionFrame
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
public static void DrawSelectionFrame(int controlID, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size, [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html) eventType); 
### Parameters
Parameter | Description  
---|---  
position | The position of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html). Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen space size.  
controlID | The control ID for the handle.  
eventType | The type of event for the handle to act on. You can only use this function with [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html).  
### Description
Creates a square at a position and rotation with a specified size.
* * *
