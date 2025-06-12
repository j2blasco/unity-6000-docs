* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.OverlapSphere.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).OverlapSphere
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
public int OverlapSphere([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius, Collider[] results, int layerMask = AllLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
position | Center of the sphere.  
radius | Radius of the sphere.  
results | The buffer to store the results into.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** The amount of colliders stored into the `results` buffer. 
### Description
Computes and stores colliders touching or inside the sphere into the provided buffer.
Additional resources: [Physics.OverlapSphereNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphereNonAlloc.html).
* * *
