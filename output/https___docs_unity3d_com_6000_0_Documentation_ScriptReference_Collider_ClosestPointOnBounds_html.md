* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.ClosestPointOnBounds.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).ClosestPointOnBounds
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ClosestPointOnBounds([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Description
The closest point to the bounding box of the attached collider.
This can be used to calculate hit points when applying explosion damage.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float hitPoints = 100.0F;
    public Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) coll;
    void Start()
    {
        coll = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
    }  
  
    void ApplyHitPoints(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) explosionPos, float radius)
    {
        // The distance from the explosion position to the surface of the collider.
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) closestPoint = coll.ClosestPointOnBounds(explosionPos);
        float distance = Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(closestPoint, explosionPos);  
  
        // The damage should decrease with distance from the explosion.
        float damage = 1.0F - Mathf.Clamp01[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp01.html)(distance / radius);
        hitPoints -= damage * 10.0F;
    }
}

```

* * *
