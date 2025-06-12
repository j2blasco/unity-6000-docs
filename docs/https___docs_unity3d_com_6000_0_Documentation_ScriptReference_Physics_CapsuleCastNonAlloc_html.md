* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCastNonAlloc.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).CapsuleCastNonAlloc
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
public static int CapsuleCastNonAlloc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point2, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
point1 | The center of the sphere at the `start` of the capsule.  
point2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction into which to sweep the capsule.  
results | The buffer to store the hits into.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** The amount of hits stored into the buffer. 
### Description
Casts a capsule against all colliders in the Scene and returns detailed information on what was hit into the buffer.
Like [Physics.CapsuleCastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCastAll.html), but generates no garbage.
* * *
