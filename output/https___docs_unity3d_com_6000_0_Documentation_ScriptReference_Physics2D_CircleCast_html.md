* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CircleCast.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).CircleCast
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
public static [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) CircleCast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) origin, float radius, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, float distance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, float minDepth = -Mathf.Infinity, float maxDepth = Mathf.Infinity); 
### Parameters
Parameter | Description  
---|---  
origin | The point in 2D space where the circle originates.  
radius | The radius of the circle.  
direction | A vector representing the direction of the circle.  
distance | The maximum distance over which to cast the circle.  
layerMask | Filter to detect Colliders only on certain layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than or equal to this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than or equal to this value.  
### Returns
**RaycastHit2D** The cast results returned. 
### Description
Casts a circle against Colliders in the Scene, returning the first Collider to contact with it.
A _CircleCast_ is conceptually like dragging a circle through the Scene in a particular direction. Any object making contact with the circle can be detected and reported.  
  
This function returns a [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) object with a reference to the Collider that is hit by the box (the Collider property of the result will be NULL if nothing was hit). The _layerMask_ can be used to detect objects selectively only on certain layers (this allows you to apply the detection only to enemy characters, for example).  
  
The returned [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) returns both the point and normal of the contact where the circle would touch the Collider. It also returns the centroid where the circle would be positioned for it to contact at that point.  
  
Additional resources: [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) class, [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) class, :[CircleCastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CircleCastAll.html), [CircleCastNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CircleCastNonAlloc.html), [DefaultRaycastLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.DefaultRaycastLayers.html), [IgnoreRaycastLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.IgnoreRaycastLayer.html), [raycastsHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-raycastsHitTriggers.html).
* * *
## Declaration
public static int CircleCast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) origin, float radius, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, RaycastHit2D[] results, float distance = Mathf.Infinity); 
### Parameters
Parameter | Description  
---|---  
origin | The point in 2D space where the circle originates.  
radius | The radius of the circle.  
direction | A vector representing the direction of the circle.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
distance | The maximum distance over which to cast the circle.  
### Returns
**int** Returns the number of results placed in the `results` array. 
### Description
Casts a circle against Colliders in the Scene, returning all Colliders that contact with it.
This function returns the number of contacts found and places those contacts in the `results` array. The results can also be filtered by the `contactFilter`.  
  
Additional resources: [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) and [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html).
* * *
## Declaration
public static int CircleCast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) origin, float radius, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<RaycastHit2D> results, float distance = Mathf.Infinity); 
### Parameters
Parameter | Description  
---|---  
origin | The point in 2D space where the circle originates.  
radius | The radius of the circle.  
direction | A vector representing the direction of the circle.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The list to receive results.  
distance | The maximum distance over which to cast the circle.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Casts a circle against Colliders in the Scene, returning all Colliders that contact with it.
The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) and [RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html).
* * *
