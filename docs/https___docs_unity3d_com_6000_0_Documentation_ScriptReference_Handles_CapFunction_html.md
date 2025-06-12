* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).CapFunction
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
public delegate void CapFunction(int controlID, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size, [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html) eventType); 
### Parameters
Parameter | Description  
---|---  
controlID | The control ID for the handle.  
position | The position of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The size of the handle in world-space units.  
eventType | Event type for the handle to act upon. By design it handles [EventType.Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Layout.html) and [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) events.  
### Description
The function to use for drawing the handle e.g. Handles.RectangleCap.
Custom CapFunction has two responsibilities:
  1. For [EventType.Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Layout.html) event, call [HandleUtility.AddControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddControl.html) to inform Unity about the distance of the handle from mouse position.
  2. For [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) event, render the actual handle.


* * *
