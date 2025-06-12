* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCast.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).CapsuleCast
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
public static bool CapsuleCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point2, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
point1 | The center of the sphere at the `start` of the capsule.  
point2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction into which to sweep the capsule.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True when the capsule sweep intersects any collider, otherwise false. 
### Description
Casts a capsule against all colliders in the Scene and returns detailed information on what was hit.
The capsule is defined by the two spheres with `radius` around `point1` and `point2`, which form the two ends of the capsule. Hits are returned for the first collider which would collide against this capsule if the capsule was moved along `direction`. This is useful when a Raycast does not give enough precision, because you want to find out if an object of a specific size, such as a character, will be able to move somewhere without colliding with anything on the way.  
  
**Notes:** CapsuleCast will not detect colliders for which the capsule overlaps the collider. Passing a zero radius results in undefined output and doesn't always behave the same as [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html).  
  
Additional resources: [Physics.SphereCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SphereCast.html), [Physics.CapsuleCastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCastAll.html), [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Rigidbody.SweepTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SweepTest.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) charContr = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p1 = transform.position + charContr.center + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * -charContr.height * 0.5F;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p2 = p1 + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * charContr.height;
        float distanceToObstacle = 0;  
  
        // Cast character controller shape 10 meters forward to see if it is about to hit anything.
        if (Physics.CapsuleCast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCast.html)(p1, p2, charContr.radius, transform.forward, out hit, 10))
            distanceToObstacle = hit.distance;
    }
}

```

* * *
## Declaration
public static bool CapsuleCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point2, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
point1 | The center of the sphere at the `start` of the capsule.  
point2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction into which to sweep the capsule.  
maxDistance | The max length of the sweep.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Description
* * *
