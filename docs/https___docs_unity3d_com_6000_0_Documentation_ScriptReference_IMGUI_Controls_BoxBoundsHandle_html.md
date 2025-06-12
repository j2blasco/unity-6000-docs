* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.html

# BoxBoundsHandle
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
A compound handle to edit a box-shaped bounding volume in the Scene view.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BoxBoundsHandle.png) _2D and 3D BoxBoundsHandle in the Scene View._  
  
Additional resources: [PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html).
### Properties
Property | Description  
---|---  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle-size.html) | Returns or specifies the size of the bounding box.  
### Constructors
Constructor | Description  
---|---  
[BoxBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle-ctor.html) | Create a new instance of the BoxBoundsHandle class.  
### Protected Methods
Method | Description  
---|---  
[DrawWireframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.DrawWireframe.html) | Draw a wireframe box for this instance.  
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
[OnHandleChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.OnHandleChanged.html) | A callback for when a control handle was dragged in the Scene.  
[SetSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.SetSize.html) | Sets the current size of the bounding volume for this instance.  
### Static Methods
Method | Description  
---|---  
[DefaultMidpointHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.DefaultMidpointHandleSizeFunction.html) | A SizeFunction that returns a fixed screen-space size.  
* * *
