* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphere.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).OverlapSphere
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
public static Collider[] OverlapSphere([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius, int layerMask = AllLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
position | Center of the sphere.  
radius | Radius of the sphere.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) defines which layers of colliders to include in the query.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**Collider[]** Returns an array with all colliders touching or inside the sphere. 
### Description
Computes and stores colliders touching or inside the sphere.
Additional resources: [Physics.AllLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.AllLayers.html). Allocates memory. Consider using [Physics.OverlapSphereNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphereNonAlloc.html) instead.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ExplosionDamage(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, float radius)
    {
        Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[] hitColliders = Physics.OverlapSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphere.html)(center, radius);
        foreach (var hitCollider in hitColliders)
        {
            hitCollider.SendMessage("AddDamage");
        }
    }
}

```

Additional resources: Ray cast with layers section of [ Use of layers in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/use-layers.html).
* * *
