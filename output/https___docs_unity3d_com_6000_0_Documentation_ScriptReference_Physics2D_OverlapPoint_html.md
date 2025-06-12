* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapPoint.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).OverlapPoint
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
public static [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) OverlapPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point, int layerMask = DefaultRaycastLayers, float minDepth = -Mathf.Infinity, float maxDepth = Mathf.Infinity); 
### Parameters
Parameter | Description  
---|---  
point | A point in world space.  
layerMask | Filter to check objects only on specific layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than or equal to this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than or equal to this value.  
### Returns
**Collider2D** The Collider overlapping the point. 
### Description
Checks if a Collider overlaps a point in space.
The optional _layerMask_ allows the test to check only for objects on specific layers.  
  
Although the Z axis is not relevant for rendering or collisions in 2D, you can use the _minDepth_ and _maxDepth_ parameters to filter objects based on their Z coordinate. If more than one Collider overlaps the point then the one returned will be the one with the lowest Z coordinate value. Null is returned if there are no Colliders over the point.  
  
Additional resources: [OverlapPointAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapPointAll.html), [OverlapPointNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapPointNonAlloc.html).
* * *
## Declaration
public static int OverlapPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, Collider2D[] results); 
### Parameters
Parameter | Description  
---|---  
point | A point in world space.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth. Note that normal angle is not used for overlap testing.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
### Returns
**int** Returns the number of results placed in the `results` array. 
### Description
Checks if a Collider overlaps a point in world space.
This function returns the number of Colliders found and places those Colliders in the `results` array.
* * *
## Declaration
public static int OverlapPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<Collider2D> results); 
### Parameters
Parameter | Description  
---|---  
point | A point in world space.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth. Note that normal angle is not used for overlap testing.  
results | The list to receive results.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Checks if a Collider overlaps a point in world space.
The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.
* * *
