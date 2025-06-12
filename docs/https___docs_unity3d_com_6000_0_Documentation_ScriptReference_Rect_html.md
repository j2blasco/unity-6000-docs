* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html

# Rect
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
A 2D Rectangle defined by X and Y position, width and height.
Unity uses a number of 2D coordinate spaces, most of which define X as increasing to the right, and Y increasing upwards. The one exception is in the GUI and GUILayout classes, where Y increases downwards.  
  
The following examples are illustrated in GUI space, where (0,0) represents the top-left corner and Y increases downwards.  
  
Rectangles can be specified in two different ways. The first is with an [x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-x.html) and [y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-y.html) position and a [width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-width.html) and [height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-height.html):  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/RectXY.svg)  
  
The other way is with the X and Y coordinates of each of its edges. These are called [xMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-xMin.html), [xMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-xMax.html), [yMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-yMin.html) and [yMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-yMax.html):  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/RectXMinYMin.svg)  
  
Note that although `x` and `y` have the same values as `xMin` and `yMin`, they behave differently when you set them. Setting `x` or `y` changes the position of the rectangle, but preserves its size:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/RectSetX.svg)  
  
Setting any of `xMin`, `xMax`, `yMin` and `yMax` will resize the rectangle, but preserve the position of the opposite edge:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/RectSetXMin.svg)  
  
Additional resources: [GUI Scripting Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Basics.html), [Camera.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-rect.html), [Camera.pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelRect.html).
### Static Properties
Property | Description  
---|---  
[zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-zero.html) | Shorthand for writing new Rect(0,0,0,0).  
### Properties
Property | Description  
---|---  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-center.html) | The position of the center of the rectangle.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-height.html) | The height of the rectangle, measured from the Y position.  
[max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-max.html) | The position of the maximum corner of the rectangle.  
[min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-min.html) | The position of the minimum corner of the rectangle.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-position.html) | The X and Y position of the rectangle.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-size.html) | The width and height of the rectangle.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-width.html) | The width of the rectangle, measured from the X position.  
[x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-x.html) | The X coordinate of the rectangle.  
[xMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-xMax.html) | The maximum X coordinate of the rectangle.  
[xMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-xMin.html) | The minimum X coordinate of the rectangle.  
[y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-y.html) | The Y coordinate of the rectangle.  
[yMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-yMax.html) | The maximum Y coordinate of the rectangle.  
[yMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-yMin.html) | The minimum Y coordinate of the rectangle.  
### Constructors
Constructor | Description  
---|---  
[Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-ctor.html) | Creates a new rectangle.  
### Public Methods
Method | Description  
---|---  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.Contains.html) | Returns true if the x and y components of point is a point inside this rectangle. If allowInverse is present and true, the width and height of the Rect are allowed to take negative values (ie, the min value is greater than the max), and the test will still work.  
[Overlaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.Overlaps.html) | Returns true if the other rectangle overlaps this one. If allowInverse is present and true, the widths and heights of the Rects are allowed to take negative values (ie, the min value is greater than the max), and the test will still work.  
[Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.Set.html) | Set components of an existing Rect.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.ToString.html) | Returns a formatted string for this Rect.  
### Static Methods
Method | Description  
---|---  
[MinMaxRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.MinMaxRect.html) | Creates a rectangle from min/max coordinate values.  
[NormalizedToPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.NormalizedToPoint.html) | Returns a point inside a rectangle, given normalized coordinates.  
[PointToNormalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.PointToNormalized.html) | Returns the normalized coordinates corresponding to the point.  
### Operators
Operator | Description  
---|---  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-operator_eq.html) | Returns true if the rectangles are the same.  
* * *
