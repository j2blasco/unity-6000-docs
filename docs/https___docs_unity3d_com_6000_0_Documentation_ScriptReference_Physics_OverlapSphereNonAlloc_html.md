* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphereNonAlloc.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).OverlapSphereNonAlloc
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
public static int OverlapSphereNonAlloc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius, Collider[] results, int layerMask = AllLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
position | Center of the sphere.  
radius | Radius of the sphere.  
results | The buffer to store the results into.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) defines which layers of colliders to include in the query.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**int** Returns the amount of colliders stored into the `results` buffer. 
### Description
Computes and stores colliders touching or inside the sphere into the provided buffer.
Does not attempt to grow the buffer if it runs out of space. The length of the buffer is returned when the buffer is full. Like [Physics.OverlapSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphere.html), but generates no garbage. Additional resources: [Physics.AllLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.AllLayers.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ExplosionDamage(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, float radius)
    {
        int maxColliders = 10;
        Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[] hitColliders = new Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[maxColliders];
        int numColliders = Physics.OverlapSphereNonAlloc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphereNonAlloc.html)(center, radius, hitColliders);
        for (int i = 0; i < numColliders; i++)
        {
            hitColliders[i].SendMessage("AddDamage");
        }
    }
}

```

Additional resources: Ray cast with layers section of [ Use of layers in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/use-layers.html).
* * *
