* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.SphereCast.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).SphereCast
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
public bool SphereCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
origin | The center of the sphere at the start of the sweep.  
radius | The radius of the sphere.  
direction | The direction into which to sweep the sphere.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True when the sphere sweep intersects any collider, otherwise false. 
### Description
Casts a sphere along a ray and returns detailed information on what was hit.
Additional resources: [Physics.SphereCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SphereCast.html).
* * *
## Declaration
public int SphereCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
origin | The center of the sphere at the start of the sweep.  
radius | The radius of the sphere.  
direction | The direction into which to sweep the sphere.  
results | The buffer to save the results to.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
### Returns
**int** The amount of hits stored into the `results` buffer. 
### Description
Cast sphere along the direction and store the results into buffer.
Additional resources: Physics.SphereCastNonAllloc.
* * *
