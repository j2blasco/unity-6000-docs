* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapCapsule.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).OverlapCapsule
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
public static Collider[] OverlapCapsule([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point0, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point1, float radius, int layerMask = AllLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
point0 | The center of the sphere at the `start` of the capsule.  
point1 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**Collider[]** Colliders touching or inside the capsule. 
### Description
Check the given capsule against the physics world and return all overlapping colliders.
* * *
