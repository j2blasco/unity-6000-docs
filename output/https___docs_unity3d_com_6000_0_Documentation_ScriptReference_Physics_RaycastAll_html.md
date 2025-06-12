* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).RaycastAll
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
public static RaycastHit[] RaycastAll([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
ray | The starting point and direction of the ray.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**RaycastHit[]** An array of RaycastHit objects. Note that the order of the results is undefined. 
### Description
Casts a ray through the Scene and returns all hits. Note that order of the results is undefined.
Additional resources: [Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)[] hits;
        hits = Physics.RaycastAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html)(transform.position, transform.forward, 100.0F);  
  
        for (int i = 0; i < hits.Length; i++)
        {
            RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit = hits[i];
            Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = hit.transform.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
            if (rend)
            {
                // Change the material of all hit colliders
                // to use a transparent shader.
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
**Notes:** Raycasts will not detect colliders for which the raycast origin is inside the collider.
* * *
## Declaration
public static RaycastHit[] RaycastAll([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
origin | The starting point of the ray in world coordinates.  
direction | The direction of the ray.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Description
Additional resources: [Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html).
See example above.
* * *
