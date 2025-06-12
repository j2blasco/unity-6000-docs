* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCastAll.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).CapsuleCastAll
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
public static RaycastHit[] CapsuleCastAll([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point2, float radius, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
point1 | The center of the sphere at the `start` of the capsule.  
point2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction into which to sweep the capsule.  
maxDistance | The max length of the sweep.  
layermask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**RaycastHit[]** An array of all colliders hit in the sweep. 
### Description
Like [Physics.CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCast.html), but this function will return all hits the capsule sweep intersects.
Casts a capsule against all colliders in the Scene and returns detailed information on each collider which was hit. The capsule is defined by the two spheres with `radius` around `point1` and `point2`, which form the two ends of the capsule. Hits are returned all colliders which would collide against this capsule if the capsule was moved along `direction`. This is useful when a Raycast does not give enough precision, because you want to find out if an object of a specific size, such as a character, will be able to move somewhere without colliding with anything on the way.  
  
**Notes:** For colliders that overlap the capsule at the start of the sweep, [RaycastHit.normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-normal.html) is set opposite to the direction of the sweep, [RaycastHit.distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-distance.html) is set to zero, and the zero vector gets returned in [RaycastHit.point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-point.html). You might want to check whether this is the case in your particular query and perform additional queries to refine the result. Passing a zero radius results in undefined output and doesn't always behave the same as [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html).  
  
Additional resources: [Physics.SphereCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SphereCast.html), [Physics.CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCast.html), [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Rigidbody.SweepTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SweepTest.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)[] hits;
        CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) charCtrl = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p1 = transform.position + charCtrl.center + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * -charCtrl.height * 0.5F;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p2 = p1 + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * charCtrl.height;  
  
        // Cast character controller shape 10 meters forward, to see if it is about to hit anything
        hits = Physics.CapsuleCastAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCastAll.html)(p1, p2, charCtrl.radius, transform.forward, 10);  
  
        // Change the material of all hit colliders
        // to use a transparent Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)
        for (int i = 0; i < hits.Length; i++)
        {
            RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit = hits[i];
            Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = hit.transform.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
            if (rend)
            {
                rend.material.shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Transparent/Diffuse");
                Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) tempColor = rend.material.color;
                tempColor.a = 0.3F;
                rend.material.color = tempColor;
            }
        }
    }
}

```

* * *
