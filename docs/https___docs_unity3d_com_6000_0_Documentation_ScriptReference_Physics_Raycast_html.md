* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).Raycast
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
public static bool Raycast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
origin | The starting point of the ray in world coordinates.  
direction | The direction of the ray.  
maxDistance | The max distance the ray should check for collisions.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** Returns true if the ray intersects with a Collider, otherwise false. 
### Description
Casts a ray, from point `origin`, in direction `direction`, of length `maxDistance`, against all colliders in the Scene.
To select which layers a ray should collide with, use a [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html).  
  
Specifying `queryTriggerInteraction` allows you to control whether or not Trigger colliders generate a hit, or whether to use the global [Physics.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitTriggers.html) setting.  
  
**Notes:** Raycasts will not detect Colliders for which the Raycast origin is inside the Collider. In all these examples [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html) is used rather than [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html). Refer to [Order of execution for event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html) to understand the difference between [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) and [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html), and to see how they relate to physics queries.
```
using UnityEngine;  
  
// C# example.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    LayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) layerMask = LayerMask.GetMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html)("Wall", "Character[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextCore.Text.Character.html)");  
  
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {  
  
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        // Does the ray intersect any objects excluding the player layer
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position, transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)), out hit, Mathf.Infinity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Infinity.html), layerMask))  
  
        { 
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(transform.position, transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)) * hit.distance, Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html)); 
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Did Hit"); 
        }
        else
        { 
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(transform.position, transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)) * 1000, Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html)); 
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Did not Hit"); 
        }  
  
    }
}

```

This example creates a simple Raycast, projecting forwards from the position of the object's current position, extending for 10 units.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) fwd = transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));  
  
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position, fwd, 10))
            print("There is something in front of the object!");
    }
}

```

* * *
## Declaration
public static bool Raycast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, float maxDistance, int layerMask, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction); 
### Parameters
Parameter | Description  
---|---  
origin | The starting point of the ray in world coordinates.  
direction | The direction of the ray.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the closest collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
maxDistance | The max distance the ray should check for collisions.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** Returns true when the ray intersects any collider, otherwise false. 
### Description
Casts a ray against all colliders in the Scene and returns detailed information on what was hit.
This example reports the distance between the current object and the reported Collider:
```
using UnityEngine;  
  
public class RaycastExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;  
  
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position, -Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), out hit))
            print("Found an object - distance: " + hit.distance);
    }
}

```

This example re-introduces the `maxDistance` parameter to limit how far ahead to cast the Ray:
```
using UnityEngine;  
  
public class RaycastExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;  
  
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position, -Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), out hit, 100.0f))
            print("Found an object - distance: " + hit.distance);
    }
}

```

* * *
## Declaration
public static bool Raycast([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
ray | The starting point and direction of the ray.  
maxDistance | The max distance the ray should check for collisions.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** Returns true when the ray intersects any collider, otherwise false. 
### Description
Same as above using `ray.origin` and `ray.direction` instead of `origin` and `direction`.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = Camera.main.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, 100))
            print("Hit something!");
    }
}

```

* * *
## Declaration
public static bool Raycast([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
ray | The starting point and direction of the ray.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the closest collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
maxDistance | The max distance the ray should check for collisions.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** Returns true when the ray intersects any collider, otherwise false. 
### Description
Same as above using `ray.origin` and `ray.direction` instead of `origin` and `direction`.
This example draws a line along the length of the Ray whenever a collision is detected:
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = Camera.main.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;  
  
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, out hit, 100))
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(ray.origin, hit.point);
    }
}

```

* * *
