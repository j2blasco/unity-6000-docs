* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DefaultRadiusHandleSizeFunction.html

#  [ArcHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html).DefaultRadiusHandleSizeFunction
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
public static float DefaultRadiusHandleSizeFunction([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The current position of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
### Returns
**float** The size to use for a handle at the specified position. 
### Description
A [SizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SizeFunction.html) that returns a fixed screen-space size.
This method is the default value assigned to [radiusHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-radiusHandleSizeFunction.html) for new [ArcHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html) instances, and is not intended to be called on its own.
* * *
