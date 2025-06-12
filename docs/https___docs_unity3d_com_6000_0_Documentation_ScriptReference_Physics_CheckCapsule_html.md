* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CheckCapsule.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).CheckCapsule
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
public static bool CheckCapsule([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) end, float radius, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
start | The center of the sphere at the `start` of the capsule.  
end | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
layermask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Description
Checks if any colliders overlap a capsule-shaped volume in world space.
The capsule is defined by the two spheres with `radius` around `point1` and `point2`, which form the two ends of the capsule.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Given the start and end waypoints of a corridor, check if there is enough
    // room for an object of a certain width to pass through.
    bool CorridorIsWideEnough(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startPt, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endPt, float width)
    {
        return Physics.CheckCapsule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CheckCapsule.html)(startPt, endPt, width);
    }
}

```

* * *
