* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SphereCastNonAlloc.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).SphereCastNonAlloc
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
public static int SphereCastNonAlloc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
origin | The center of the sphere at the start of the sweep.  
radius | The radius of the sphere.  
direction | The direction in which to sweep the sphere.  
results | The buffer to save the hits into.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a sphere.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** The amount of hits stored into the `results` buffer. 
### Description
Cast sphere along the direction and store the results into buffer.
This is variant of [Physics.SphereCastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SphereCastAll.html), but instead of allocating the array with the results of the query, it stores the results into the user-provided array. It will only compute as many hits as fit into the buffer, and store them in no particular order. It's not guaranteed that it will store only the closest hits. Generates no garbage.
* * *
## Declaration
public static int SphereCastNonAlloc([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray, float radius, RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
ray | The starting point and direction of the ray into which the sphere sweep is cast.  
radius | The radius of the sphere.  
results | The buffer to save the results to.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a sphere.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** The amount of hits stored into the `results` buffer. 
### Description
Cast sphere along the direction and store the results into buffer.
* * *
