* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).Linecast
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
public static bool Linecast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) end, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
start | Start point.  
end | End point.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Description
Returns true if there is any collider intersecting the line between `start` and `end`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Physics.Linecast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html)(transform.position, target.position))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("blocked");
        }
    }
}

```

* * *
## Declaration
public static bool Linecast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) end, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
start | Start point.  
end | End point.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
### Description
Returns true if there is any collider intersecting the line between `start` and `end`.
If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)). [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) is used to selectively ignore colliders when casting a ray.
* * *
