* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BoxCastAll.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).BoxCastAll
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
public static RaycastHit[] BoxCastAll([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layermask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**RaycastHit[]** All colliders that were hit. 
### Description
Like [Physics.BoxCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BoxCast.html), but returns all hits.
**Notes:** For colliders that overlap the box at the start of the sweep, [RaycastHit.normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-normal.html) is set opposite to the direction of the sweep, [RaycastHit.distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-distance.html) is set to zero, and the zero vector gets returned in [RaycastHit.point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-point.html). You might want to check whether this is the case in your particular query and perform additional queries to refine the result.
* * *
