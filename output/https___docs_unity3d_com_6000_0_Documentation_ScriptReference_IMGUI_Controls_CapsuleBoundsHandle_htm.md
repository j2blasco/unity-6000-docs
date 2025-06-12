* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle.html

# CapsuleBoundsHandle
class in UnityEditor.IMGUI.Controls
/
Inherits from:[IMGUI.Controls.PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html)
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
### Description
A compound handle to edit a capsule-shaped bounding volume in the Scene view.
A capsule volume is defined by two parameters. The [height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-height.html) specifies the upper and lower bounds along the [heightAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-heightAxis.html), while the [radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-radius.html) specifies the radius of the capsule's cross section between the upper and lower points on its height axis.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/CapsuleBoundsHandle.png) _2D and 3D CapsuleBoundsHandle in the Scene View._  
  
Additional resources: [PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html).
### Properties
Property | Description  
---|---  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-height.html) | Returns or specifies the height of the capsule bounding volume.  
[heightAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-heightAxis.html) | Returns or specifies the axis in the handle's space to which height maps. The radius maps to the remaining axes.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-radius.html) | Returns or specifies the radius of the capsule bounding volume.  
### Constructors
Constructor | Description  
---|---  
[CapsuleBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle-ctor.html) | Create a new instance of the CapsuleBoundsHandle class.  
### Protected Methods
Method | Description  
---|---  
[DrawWireframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle.DrawWireframe.html) | Draw a wireframe capsule for this instance.  
[OnHandleChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle.OnHandleChanged.html) | A callback for when a control handle was dragged in the Scene.  
### Inherited Members
### Properties
Property | Description  
---|---  
[axes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-axes.html) | Flags specifying which axes should display control handles.  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-center.html) | Returns or specifies the center of the bounding volume for the handle.  
[handleColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-handleColor.html) | Returns or specifies the color of the control handles.  
[midpointHandleDrawFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-midpointHandleDrawFunction.html) | An optional CapFunction to use when displaying the control handles. Defaults to Handles.DotHandleCap if no value is specified.  
[midpointHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-midpointHandleSizeFunction.html) | The SizeFunction to specify how large the midpoint control handles should be.  
[wireframeColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle-wireframeColor.html) | Returns or specifies the color of the wireframe shape.  
### Public Methods
Method | Description  
---|---  
[DrawHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.DrawHandle.html) | A function to display this instance in the current handle camera using its current configuration.  
[SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.SetColor.html) | Sets handleColor and wireframeColor to the same value.  
### Protected Methods
Method | Description  
---|---  
[GetSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.GetSize.html) | Gets the current size of the bounding volume for this instance.  
[IsAxisEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.IsAxisEnabled.html) | Gets a value indicating whether the specified axis is enabled for the current instance.  
[SetSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.SetSize.html) | Sets the current size of the bounding volume for this instance.  
### Static Methods
Method | Description  
---|---  
[DefaultMidpointHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.DefaultMidpointHandleSizeFunction.html) | A SizeFunction that returns a fixed screen-space size.  
* * *
