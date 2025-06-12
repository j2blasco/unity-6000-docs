* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html

# Plane
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
Representation of a plane in 3D space.
A plane is an infinitely large, flat surface that exists in 3D space and divides the space into two halves known as _half-spaces_. It is easy to determine which of the two half-spaces a particular point is in and also how far the point is from the plane. Walls, floors and other flat surfaces are common in games, so a plane is sometimes useful for mathematical calculations with these objects. Also, there are cases where a real surface does not exist but it is useful to imagine that one is there. For example, in sports, a goal line or out-of-bounds line is often assumed to extend into the air, effectively defining a plane.  
  
When a plane passes through the <0,0,0> point in world space, it is defined simply by a normal vector that determines which way it faces. It is easy to visualise this if you imagine looking at the plane edge-on.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PlaneNormalOrigin.png)  
  
Note that the side from which the normal vector points is important since it is used to identify which half-space a point is in (ie, on the positive or "normal" side of the plane or the other side). When the plane doesn't pass through <0,0,0> it can be defined by the normal vector along with a distance from <0,0,0>  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PlaneNormalOffset.png)  
  
A plane can also be defined by the three corner points of a triangle that lies within the plane. In this case, the normal vector points toward you if the corner points go around clockwise as you look at the triangle face-on.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Plane3Points.png).
### Properties
Property | Description  
---|---  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane-distance.html) | The distance measured from the Plane to the origin, along the Plane's normal.  
[flipped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane-flipped.html) | Returns a copy of the plane that faces in the opposite direction.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane-normal.html) | Normal vector of the plane.  
### Constructors
Constructor | Description  
---|---  
[Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane-ctor.html) | Creates a plane.  
### Public Methods
Method | Description  
---|---  
[ClosestPointOnPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.ClosestPointOnPlane.html) | For a given point returns the closest point on the plane.  
[Flip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Flip.html) | Makes the plane face in the opposite direction.  
[GetDistanceToPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.GetDistanceToPoint.html) | Returns a signed distance from plane to point.  
[GetSide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.GetSide.html) | Is a point on the positive side of the plane?  
[Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Raycast.html) | Intersects a ray with the plane.  
[SameSide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.SameSide.html) | Are two points on the same side of the plane?  
[Set3Points](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Set3Points.html) | Sets a plane using three points that lie within it. The points go around clockwise as you look down on the top surface of the plane.  
[SetNormalAndPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.SetNormalAndPosition.html) | Sets a plane using a point that lies within it along with a normal to orient it.  
[Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Translate.html) | Returns a copy of the given plane that is moved in space by the given translation.  
* * *
