* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Linecast.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).Linecast
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
## Declaration
public static [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) Linecast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) start, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) end, int layerMask = DefaultRaycastLayers, float minDepth = -Mathf.Infinity, float maxDepth = Mathf.Infinity); 
### Parameters
Parameter | Description  
---|---  
start | The start point of the line in world space.  
end | The end point of the line in world space.  
layerMask | Filter to detect Colliders only on certain layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than or equal to this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than or equal to this value.  
### Returns
**RaycastHit2D** The cast results returned. 
### Description
Casts a line segment against Colliders in the Scene.
A _linecast_ is an imaginary line between two points in world space. Any object making contact with this line can be detected and reported. This differs from the similar _raycast_ in that raycasting specifies the line using an origin and direction.  
  
This function returns a RaycastHit2D object when the line contacts a Collider in the Scene. The _layerMask_ can be used to detect objects selectively only on certain layers (this allows you to apply the detection only to enemy characters, for example). The direction of the line is assumed to extend from the start point to the end point. Only the first Collider encountered in that direction will be reported. Although the Z axis is not relevant for rendering or collisions in 2D, you can use the _minDepth_ and _maxDepth_ parameters to filter objects based on their Z coordinate.  
  
Linecasts are useful for determining lines of sight, targets hit by gunfire and for many other purposes in gameplay.  
  
Note that this function will allocate memory for the returned RaycastHit2D object. You can use [LinecastNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.LinecastNonAlloc.html) to avoid this overhead if you need to make linecasts frequently.  
  
Additionally, this will also detect Collider(s) at the start of the line. In this case the line is starting inside the Collider and doesn't intersect the Collider surface. This means that the collision normal cannot be calculated in which case the collision normal returned is set to the inverse of the line vector being tested. This can easily be detected because such results are always at a RaycastHit2D fraction of zero.  
  
Additional resources: [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) class, [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) class, [LinecastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.LinecastAll.html), [LinecastNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.LinecastNonAlloc.html), [DefaultRaycastLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.DefaultRaycastLayers.html), [IgnoreRaycastLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.IgnoreRaycastLayer.html), [raycastsHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-raycastsHitTriggers.html).
* * *
## Declaration
public static int Linecast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) start, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) end, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, RaycastHit2D[] results); 
### Parameters
Parameter | Description  
---|---  
start | The start point of the line in world space.  
end | The end point of the line in world space.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
### Returns
**int** Returns the number of results placed in the `results` array. 
### Description
Casts a line segment against Colliders in the Scene with results filtered by [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html).
The overloads of this function with the `contactFilter` parameter can filter the returned results by the options in [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html).  
  
Additional resources: [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) and [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html).
* * *
## Declaration
public static int Linecast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) start, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) end, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<RaycastHit2D> results); 
### Parameters
Parameter | Description  
---|---  
start | The start point of the line in world space.  
end | The end point of the line in world space.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The list to receive results.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Casts a line segment against Colliders in the Scene with results filtered by [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html).
The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) and [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html).
* * *
