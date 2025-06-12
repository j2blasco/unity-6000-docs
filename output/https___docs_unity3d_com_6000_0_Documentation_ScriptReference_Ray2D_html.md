* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D.html

# Ray2D
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
A ray in 2D space.
A _ray_ is a line segment that extends from a point in space in a specified direction. Rays have a number of uses in Unity but the most common is probably _raycasting_. This technique involves tracing along the path of a ray from its origin to determine if it intersects with any objects. This is useful for plotting the paths of projectiles, determining lines of sight and implementing many common game mechanics.  
  
Additional resources: [Physics2D.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Raycast.html), [Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) class, [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) class.
### Properties
Property | Description  
---|---  
[direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D-direction.html) | The direction of the ray in world space.  
[origin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D-origin.html) | The starting point of the ray in world space.  
### Constructors
Constructor | Description  
---|---  
[Ray2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D-ctor.html) | Creates a 2D ray starting at origin along direction.  
### Public Methods
Method | Description  
---|---  
[GetPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D.GetPoint.html) | Get a point that lies a given distance along a ray.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D.ToString.html) | Returns a formatted string for this 2D ray.  
* * *
