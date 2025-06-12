* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastNonAlloc.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).RaycastNonAlloc
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
public static int RaycastNonAlloc([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray, RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
ray | The starting point and direction of the ray.  
results | The buffer to store the hits into.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** The amount of hits stored into the `results` buffer. 
### Description
Cast a ray through the Scene and store the hits into the buffer.
Like [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html), but generates no garbage.  
  
The raycast query ends when there are no more hits and/or the results buffer is full. The order of the results is undefined. When a full buffer is returned it is not guaranteed that the results are the closest hits and the length of the buffer is returned. If a null buffer is passed in, no results are returned and no errors or exceptions are thrown.
* * *
## Declaration
public static int RaycastNonAlloc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
origin | The starting point and direction of the ray.  
results | The buffer to store the hits into.  
direction | The direction of the ray.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
### Returns
**int** The amount of hits stored into the `results` buffer. 
### Description
Cast a ray through the Scene and store the hits into the buffer.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The size of the array determines how many raycasts will occur
    RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)[] m_Results = new RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)[5];  
  
    // See Order of Execution for Event Functions[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html) for information on FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() and Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() related to physics queries
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // Set the layer mask to all layers
        var layerMask = ~0;  
  
        int hits = Physics.RaycastNonAlloc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastNonAlloc.html)(transform.position, transform.forward, m_Results, Mathf.Infinity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Infinity.html), layerMask);
        for (int i = 0; i < hits; i++)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hit " + m_Results[i].collider.gameObject.name);
        }
        if (hits == 0)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Did not hit");
        }
    }
}

```

* * *
