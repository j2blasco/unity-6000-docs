* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html

# Bounds
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
Represents an axis aligned bounding box.
An axis-aligned bounding box, or AABB for short, is a box aligned with coordinate axes and fully enclosing some object. Because the box is never rotated with respect to the axes, it can be defined by just its [center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-center.html) and [extents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-extents.html), or alternatively by [min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-min.html) and [max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-max.html) points.  
  
`Bounds` is used by [Collider.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-bounds.html), [Mesh.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html) and [Renderer.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-bounds.html).
### Properties
Property | Description  
---|---  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-center.html) | The center of the bounding box.  
[extents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-extents.html) | The extents of the Bounding Box. This is always half of the size of the Bounds.  
[max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-max.html) | The maximal point of the box. This is always equal to center+extents.  
[min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-min.html) | The minimal point of the box. This is always equal to center-extents.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-size.html) | The total size of the box. This is always twice as large as the extents.  
### Constructors
Constructor | Description  
---|---  
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-ctor.html) | Creates a new Bounds.  
### Public Methods
Method | Description  
---|---  
[ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.ClosestPoint.html) | The closest point on the bounding box.  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Contains.html) | Is point contained in the bounding box?  
[Encapsulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Encapsulate.html) | Grows the Bounds to include the point.  
[Expand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Expand.html) | Expand the bounds by increasing its size by amount along each side.  
[IntersectRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.IntersectRay.html) | Does ray intersect this bounding box?  
[Intersects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Intersects.html) | Does another bounding box intersect with this bounding box?  
[SetMinMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.SetMinMax.html) | Sets the bounds to the min and max value of the box.  
[SqrDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.SqrDistance.html) | The smallest squared distance between the point and this bounding box.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.ToString.html) | Returns a formatted string for the bounds.  
* * *
