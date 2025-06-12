* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CheckBox.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).CheckBox
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
public static bool CheckBox([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, int layermask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half the size of the box in each dimension.  
orientation | Rotation of the box.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True, if the box overlaps with any colliders. 
### Description
Check whether the given box overlaps with other colliders or not.
* * *
