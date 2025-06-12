* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.html

# Painter2D
class in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
Object to draw 2D vector graphics. 
The example below demonstrates how to use the Painter2D class to draw content in a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) with the [VisualElement.generateVisualContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-generateVisualContent.html) callback. You can also create a standalone [Painter2D.Painter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-ctor.html) object to draw content offscreen, and use the [Painter2D.SaveToVectorImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.SaveToVectorImage.html) method to save the painter content in a [VectorImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VectorImage.html) asset.   
  

```
 using UnityEngine;
 using UnityEngine.UIElements;  
  
 [RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(UIDocument[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html)))]
 public class Painter2DExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
 {
     public void OnEnable()
     {
         var doc = GetComponent<UIDocument[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html)>();
         doc.rootVisualElement.generateVisualContent += Draw;
     }  
  
     void Draw(MeshGenerationContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html) ctx)
     {
         var painter = ctx.painter2D;
         painter.lineWidth = 10.0f;
         painter.lineCap = LineCap.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LineCap.Round.html);
         painter.strokeGradient = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)() {
             colorKeys = new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] {
                 new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)() { color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), time = 0.0f },
                 new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)() { color = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html), time = 1.0f }
             }
         };
         painter.BeginPath();
         painter.MoveTo(new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(10, 10));
         painter.BezierCurveTo(new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(100, 100), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(200, 0), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(300, 100));
         painter.Stroke();
     }
 }

```

### Properties
Property | Description  
---|---  
[fillColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-fillColor.html) |  The color used for fill paths when using Fill.   
[lineCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-lineCap.html) |  The cap to use when drawing paths using Stroke.   
[lineJoin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-lineJoin.html) |  The join to use when drawing paths using Stroke.   
[lineWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-lineWidth.html) |  The line width of draw paths when using Stroke.   
[miterLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-miterLimit.html) |  When using LineJoin.Miter joins, this defines the limit on the ratio of the miter length to the stroke width before converting the miter to a bevel.   
[strokeColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-strokeColor.html) |  The color of draw paths when using Stroke.   
[strokeGradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-strokeGradient.html) |  The stroke gradient to use when using Stroke.   
### Constructors
Constructor | Description  
---|---  
[Painter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D-ctor.html) |  Initializes an instance of Painter2D.   
### Public Methods
Method | Description  
---|---  
[Arc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.Arc.html) |  Adds an arc to the current sub-path to the provided position, radius and angles.   
[ArcTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.ArcTo.html) |  Adds an arc to the current sub-path to the provided position using a control point.   
[BeginPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.BeginPath.html) |  Begins a new path and empties the list of recorded sub-paths.   
[BezierCurveTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.BezierCurveTo.html) |  Adds a cubic bezier curve to the current sub-path to the provided position using two control points.   
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.Clear.html) |  When created as a detached painter, clears the current content. Does nothing otherwise.   
[ClosePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.ClosePath.html) |  Closes the current sub-path with a straight line. If the sub-path is already closed, this does nothing.   
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.Dispose.html) |  Dispose the Painter2D object and free its internal unmanaged resources.   
[Fill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.Fill.html) |  Fills the currently defined path.   
[LineTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.LineTo.html) |  Adds a straight line to the current sub-path to the provided position.   
[MoveTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.MoveTo.html) |  Begins a new sub-path at the provied coordinate.   
[QuadraticCurveTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.QuadraticCurveTo.html) |  Adds a quadratic bezier curve to the current sub-path to the provided position using a control point.   
[SaveToVectorImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.SaveToVectorImage.html) |  Saves the content of this Painter2D to a VectorImage object.   
[Stroke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.Stroke.html) |  Strokes the currently defined path.   
* * *
