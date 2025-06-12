* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.IsAxisEnabled.html

#  [PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html).IsAxisEnabled
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
protected bool IsAxisEnabled([IMGUI.Controls.PrimitiveBoundsHandle.Axes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.Axes.html) axis); 
## Declaration
protected bool IsAxisEnabled(int vector3Axis); 
### Parameters
Parameter | Description  
---|---  
axis | An [Axes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.Axes.html).  
vector3Axis | An integer corresponding to an axis on a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html). For example, `0` is x, `1` is y, and `2` is z.  
### Returns
**bool** `true` if the specified axis is enabled; otherwise, `false`. 
### Description
Gets a value indicating whether the specified axis is enabled for the current instance.
Additional resources: [axes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-axes.html).
* * *
