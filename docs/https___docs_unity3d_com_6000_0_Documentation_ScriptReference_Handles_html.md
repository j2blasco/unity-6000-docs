* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html

# Handles
class in UnityEditor
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
Custom 3D GUI controls and drawing in the Scene view.
Handles are the 3D controls that Unity uses to manipulate items in the Scene view. There are a number of built-in Handle GUIs, such as the familiar tools to position, scale and rotate an object via the Transform component. However, it is also possible to define your own Handle GUIs to use with custom component editors. Such GUIs can be a very useful way to edit procedurally-generated Scene content, "invisible" items and groups of related objects, such as waypoints and location markers.  
  
You can also supplement the 3D Handle GUI in the Scene with 2D buttons and other controls overlaid on the Scene view. This is done by enclosing standard Unity GUI calls in a [Handles.BeginGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html) and [Handles.EndGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html) pair within the [Editor.OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) function. You can use [HandleUtility.GUIPointToWorldRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToWorldRay.html) and [HandleUtility.WorldToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldToGUIPoint.html) to convert coordinates between 2D GUI and 3D world coordinates.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float value = 7.0f;
}  
  
// A tiny custom editor for ExampleScript component
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ExampleScript))]
public class ExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    // Custom in-scene UI for when ExampleScript
    // component is selected.
    public void OnSceneGUI()
    {
        var t = target as ExampleScript;
        var tr = t.transform;
        var pos = tr.position;
        // display an orange disc where the object is
        var color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 0.8f, 0.4f, 1);
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = color;
        Handles.DrawWireDisc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireDisc.html)(pos, tr.up, 1.0f);
        // display object "value" in scene
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = color;
        Handles.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html)(pos, t.value.ToString("F1"));
    }
}

```

![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HandlesExample.png).
### Static Properties
Property | Description  
---|---  
[centerColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-centerColor.html) | Color to use for handles that represent the center of something.  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) | Sets the color of handles. Color is a persistent state and affects any handles drawn after it is set. Use DrawingScope to set the color for a block of handles without affecting the color of other handles.  
[elementColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-elementColor.html) | The default color of objects in an Edit Mode.  
[elementPreselectionColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-elementPreselectionColor.html) | Color to use to highlight an unselected object currently under the mouse pointer in a custom Edit Mode.  
[elementSelectionColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-elementSelectionColor.html) | The color of selected objects in a Edit Mode.  
[inverseMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-inverseMatrix.html) | The inverse of the matrix for all handle operations.  
[lighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-lighting.html) | Are handles lit?  
[lineThickness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-lineThickness.html) | Retrieves the user preference setting that controls the thickness of tool handle lines. (Read Only)  
[matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html) | Matrix for all handle operations. This is used by functions in HandleUtility and Handles to transform controls.  
[preselectionColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-preselectionColor.html) | Color to use to highlight an unselected handle currently under the mouse pointer.  
[secondaryColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-secondaryColor.html) | Soft color to use for for general things.  
[selectedColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-selectedColor.html) | Color to use for the currently active handle.  
[UIColliderHandleColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.UIColliderHandleColor.html) | Color to use for the Unity UI's padding visualization.  
[xAxisColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-xAxisColor.html) | Color to use for handles that manipulates the X coordinate of something.  
[yAxisColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-yAxisColor.html) | Color to use for handles that manipulates the Y coordinate of something.  
[zAxisColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-zAxisColor.html) | Color to use for handles that manipulates the Z coordinate of something.  
[zTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-zTest.html) | zTest of the handles.  
### Properties
Property | Description  
---|---  
[currentCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-currentCamera.html) | Gets or sets the camera that is currently rendering.  
### Static Methods
Method | Description  
---|---  
[ArrowHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ArrowHandleCap.html) | Draw an arrow like those used by the move tool.  
[BeginGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html) | Begin a 2D GUI block inside the 3D handle GUI.  
[Button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Button.html) | Make a 3D Button.  
[CircleHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CircleHandleCap.html) | Draw a circle handle. Pass this into handle functions.  
[ClearCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ClearCamera.html) | Clears the camera.  
[ConeHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html) | Draw a cone handle. Pass this into handle functions.  
[CubeHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CubeHandleCap.html) | Draw a cube handle. Pass this into handle functions.  
[CylinderHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CylinderHandleCap.html) | Draw a cylinder handle. Pass this into handle functions.  
[Disc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Disc.html) | Make a 3D disc that can be dragged with the mouse.  
[DotHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DotHandleCap.html) | Draw a dot handle. Pass this into handle functions.  
[DrawAAConvexPolygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawAAConvexPolygon.html) | Draw anti-aliased convex polygon specified with point array.  
[DrawAAPolyLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawAAPolyLine.html) | Draw anti-aliased line specified with point array and width.  
[DrawBezier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawBezier.html) | Draw textured bezier line through start and end points with the given tangents.  
[DrawCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawCamera.html) | Draws a camera inside a rectangle.  
[DrawDottedLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLine.html) | Draw a dotted line from p1 to p2.  
[DrawDottedLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLines.html) | Draw a list of dotted line segments.  
[DrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawGizmos.html) | Draw the Gizmos for the specified camera.  
[DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html) | Draws a line from p1 to p2.  
[DrawLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLines.html) | Draw a list of line segments.  
[DrawOutline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawOutline.html) | Draws an outline around the specified GameObjects in the Scene View.  
[DrawPolyLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawPolyLine.html) | Draw a line going through the list of points.  
[DrawSelectionFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSelectionFrame.html) | Creates a square at a position and rotation with a specified size.  
[DrawSolidArc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidArc.html) | Draw a circular sector (pie piece) in 3D space.  
[DrawSolidDisc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidDisc.html) | Draw a solid flat disc in 3D space.  
[DrawSolidRectangleWithOutline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidRectangleWithOutline.html) | Draw a solid outlined rectangle in 3D space.  
[DrawTexture3DSDF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSDF.html) | Draws a 3D texture using Signed Distance Field rendering mode in 3D space.  
[DrawTexture3DSlice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSlice.html) | Draws a 3D texture using Slice rendering mode in 3D space.  
[DrawTexture3DVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DVolume.html) | Draws a 3D texture using Volume rendering mode in 3D space.  
[DrawWireArc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html) | Draws a circular arc in 3D space.  
[DrawWireCube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireCube.html) | Draw a wireframe box with center and size.  
[DrawWireDisc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireDisc.html) | Draws the outline of a flat disc in 3D space.  
[EndGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html) | End a 2D GUI block and get back to the 3D handle GUI.  
[FreeMoveHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.FreeMoveHandle.html) | Make an unconstrained movement handle.  
[FreeRotateHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.FreeRotateHandle.html) | Make an unconstrained rotation handle.  
[GetMainGameViewSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.GetMainGameViewSize.html) | Get the width and height of the main game view.  
[Label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html) | Creates a text label for a handle that is positioned in 3D space.  
[MakeBezierPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.MakeBezierPoints.html) | Retuns an array of points to representing the bezier curve.  
[PositionHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html) | Make a position handle.  
[RadiusHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RadiusHandle.html) | Make a Scene view radius handle.  
[RectangleHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RectangleHandleCap.html) | Draw a rectangle handle. Pass this into handle functions.  
[RotationHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RotationHandle.html) | Make a Scene view rotation handle.  
[ScaleHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleHandle.html) | Make a Scene view scale handle.  
[ScaleSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleSlider.html) | Make a directional scale slider.  
[ScaleValueHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html) | Make a 3D handle that scales a single float.  
[SetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SetCamera.html) | Set the current camera so all Handles and Gizmos are draw with its settings.  
[ShouldRenderGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ShouldRenderGizmos.html) | Determines whether or not to draw Gizmos.  
[Slider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider.html) | Make a 3D slider that moves along one axis.  
[Slider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider2D.html) | Make a 3D slider that moves along a plane defined by two axes.  
[SnapToGrid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapToGrid.html) | Rounds each Transform.position or Vector3 to the closest multiple of EditorSnapSettings.gridSize.  
[SnapValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapValue.html) | Rounds value to the closest multiple of snap if snapping is active. Note that snap can only be positive.  
[SphereHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SphereHandleCap.html) | Draw a sphere handle. Pass this into handle functions.  
[TransformHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.TransformHandle.html) | Creates a transform handle.  
### Delegates
Delegate | Description  
---|---  
[CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) | The function to use for drawing the handle e.g. Handles.RectangleCap.  
[SizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SizeFunction.html) | A delegate type for getting a handle's size based on its current position.  
* * *
