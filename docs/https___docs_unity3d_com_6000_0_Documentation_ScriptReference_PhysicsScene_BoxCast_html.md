* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.BoxCast.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).BoxCast
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
public bool BoxCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True, if any intersections were found. 
### Description
Casts the box along a ray and returns detailed information on what was hit.
Additional resources: [Physics.BoxCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BoxCast.html).
* * *
## Declaration
public int BoxCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, RaycastHit[] results, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
results | The buffer to store the results in.  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** The amount of hits stored to the `results` buffer. 
### Description
Casts the box along a ray and returns detailed information on what was hit.
Additional resources: [Physics.BoxCastNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BoxCastNonAlloc.html).
* * *
