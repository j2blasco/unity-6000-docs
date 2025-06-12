* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html

# BoundsInt
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
Represents an axis aligned bounding box with all values as integers.
An axis-aligned bounding box, or AABB for short, is a box aligned with coordinate axes and fully enclosing some object. As the box is never rotated with respect to the axes, it can be defined by [min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-min.html) and [max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-max.html) points.
### Properties
Property | Description  
---|---  
[allPositionsWithin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-allPositionsWithin.html) | A BoundsInt.PositionCollection that contains all positions within the BoundsInt.  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-center.html) | The center of the bounding box.  
[max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-max.html) | The maximal point of the box.  
[min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-min.html) | The minimal point of the box.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-position.html) | The position of the bounding box.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-size.html) | The total size of the box.  
[x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-x.html) | X value of the minimal point of the box.  
[xMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-xMax.html) | The maximal x point of the box.  
[xMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-xMin.html) | The minimal x point of the box.  
[y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-y.html) | Y value of the minimal point of the box.  
[yMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-yMax.html) | The maximal y point of the box.  
[yMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-yMin.html) | The minimal y point of the box.  
[z](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-z.html) | Z value of the minimal point of the box.  
[zMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-zMax.html) | The maximal z point of the box.  
[zMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-zMin.html) | The minimal z point of the box.  
### Public Methods
Method | Description  
---|---  
[ClampToBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.ClampToBounds.html) | Clamps the position and size of this bounding box to the given bounds.  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.Contains.html) | Is point contained in the bounding box?  
[SetMinMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.SetMinMax.html) | Sets the bounds to the min and max value of the box.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.ToString.html) | Returns a formatted string for the bounds.  
* * *
