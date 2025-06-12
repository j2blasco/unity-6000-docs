* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html

# RectInt
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
A 2D Rectangle defined by x, y, width, height with integers.
### Static Properties
Property | Description  
---|---  
[zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-zero.html) | Shorthand for writing new RectInt(0,0,0,0).  
### Properties
Property | Description  
---|---  
[allPositionsWithin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-allPositionsWithin.html) | A RectInt.PositionCollection that contains all positions within the RectInt.  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-center.html) | Center coordinate of the rectangle.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-height.html) | Height of the rectangle.  
[max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-max.html) | The upper right corner of the rectangle; which is the maximal position of the rectangle along the x- and y-axes, when it is aligned to both axes.  
[min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-min.html) | The lower left corner of the rectangle; which is the minimal position of the rectangle along the x- and y-axes, when it is aligned to both axes.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-position.html) | Returns the position (x, y) of the RectInt.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-size.html) | Returns the width and height of the RectInt.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-width.html) | Width of the rectangle.  
[x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-x.html) | Left coordinate of the rectangle.  
[xMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-xMax.html) | Shows the maximum X value of the RectInt.  
[xMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-xMin.html) | Shows the minimum X value of the RectInt.  
[y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-y.html) | Top coordinate of the rectangle.  
[yMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-yMax.html) | Shows the maximum Y value of the RectInt.  
[yMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-yMin.html) | Show the minimum Y value of the RectInt.  
### Constructors
Constructor | Description  
---|---  
[RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-ctor.html) | Creates a new RectInt.  
### Public Methods
Method | Description  
---|---  
[ClampToBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.ClampToBounds.html) | Clamps the position and size of the RectInt to the given bounds.  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.Contains.html) | Returns true if the given position is within the RectInt.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.Equals.html) | Returns true if the given RectInt is equal to this RectInt.  
[Overlaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.Overlaps.html) | RectInts overlap if each RectInt Contains a shared point.  
[SetMinMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.SetMinMax.html) | Sets the bounds to the min and max value of the rect.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.ToString.html) | Returns the x, y, width and height of the RectInt.  
### Operators
Operator | Description  
---|---  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt-operator_eq.html) | Returns true if the rectangles are the same.  
* * *
