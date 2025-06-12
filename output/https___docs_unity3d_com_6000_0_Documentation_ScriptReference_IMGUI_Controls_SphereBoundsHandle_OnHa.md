* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SphereBoundsHandle.OnHandleChanged.html

#  [SphereBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SphereBoundsHandle.html).OnHandleChanged
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
protected [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) OnHandleChanged([IMGUI.Controls.PrimitiveBoundsHandle.HandleDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.HandleDirection.html) handle, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) boundsOnClick, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) newBounds); 
### Parameters
Parameter | Description  
---|---  
handle | The handle that was dragged.  
boundsOnClick | The raw [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) for this instance's volume at the time the control handle was clicked.  
newBounds | The raw [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) for this instance's volume based on the updated handle position.  
### Returns
**Bounds** The bounds that should be applied to this instance, with any necessary modifications applied. 
### Description
A callback for when a control handle was dragged in the Scene.
This method ensures that all axes always scale uniformly.
* * *
