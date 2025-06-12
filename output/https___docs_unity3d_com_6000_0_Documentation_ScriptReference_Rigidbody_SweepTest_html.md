* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SweepTest.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).SweepTest
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
## Declaration
public bool SweepTest([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, float maxDistance = Mathf.Infinity, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
direction | The direction into which to sweep the rigidbody.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
maxDistance | The length of the sweep.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True when the rigidbody sweep intersects any collider, otherwise false. 
### Description
Tests if a rigidbody would collide with anything, if it was moved through the Scene.
Tests if a rigidbody would collide with anything, if it was moved through the Scene. This is similar to doing a [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html) for all points contained in any of a Rigidbody's colliders and returning the closest of all hits (if any) reported. This is useful for AI code, say if you need to know that an object would fit through a gap without colliding with anything.  
  
Note that this function only works when a primitive collider type (sphere, cube or capsule) or a convex mesh is attached to the rigidbody object - concave mesh colliders will not work, although they can be detected in the Scene by the sweep.  
  
Additional resources: [Physics.SphereCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.SphereCast.html), [Physics.CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CapsuleCast.html), [Rigidbody.SweepTestAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SweepTestAll.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float collisionCheckDistance;
    public bool aboutToCollide;
    public float distanceToCollision;
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        if (rb.SweepTest(transform.forward, out hit, collisionCheckDistance))
        {
            aboutToCollide = true;
            distanceToCollision = hit.distance;
        }
    }
}

```

* * *
