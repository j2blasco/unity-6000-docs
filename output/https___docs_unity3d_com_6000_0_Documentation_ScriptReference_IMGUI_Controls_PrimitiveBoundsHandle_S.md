* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.SetSize.html

#  [PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html).SetSize
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
protected void SetSize([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size); 
### Parameters
Parameter | Description  
---|---  
size | A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) specifying how large the bounding volume is along all of its axes.  
### Description
Sets the current size of the bounding volume for this instance.
A negative value along any axis of the specified [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) will automatically be converted into a positive value. Disabled axes will automatically be converted to `0`.  
  
Additional resources: [axes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-axes.html).
* * *
