* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddExplosionForce.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).AddExplosionForce
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
public void AddExplosionForce(float explosionForce, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) explosionPosition, float explosionRadius, float upwardsModifier = 0.0f, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force)); 
### Parameters
Parameter | Description  
---|---  
explosionForce | The force of the explosion (which may be modified by distance).  
explosionPosition | The centre of the sphere within which the explosion has its effect.  
explosionRadius | The radius of the sphere within which the explosion has its effect.  
upwardsModifier | Adjustment to the apparent position of the explosion to make it seem to lift objects.  
mode | The method used to apply the force to its targets.  
### Description
Applies a force to a rigidbody that simulates explosion effects.
The explosion is modelled as a sphere with a certain centre position and radius in world space; normally, anything outside the sphere is not affected by the explosion and the force decreases in proportion to distance from the centre. However, if a value of zero is passed for the radius then the full force will be applied regardless of how far the centre is from the rigidbody.  
  
This function applies a force to the object at the point on the surface of the rigidbody that is closest to `explosionPosition`. The force acts along the direction from `explosionPosition` to the surface point on the rigidbody. If `explosionPosition` is inside the rigidbody, or the rigidbody has no active colliders, then the center of mass is used instead of the closest point on the surface.  
  
The magnitude of the force depends on the distance between `explosionPosition` and the point where the force was applied. As the distance between `explosionPosition` and the force point increases, the actual applied force decreases.  
  
The vertical direction of the force can be modified using `upwardsModifier`. If this parameter is greater than zero, the force is applied at the point on the surface of the Rigidbody that is closest to `explosionPosition` but shifted along the y-axis by negative `upwardsModifier`. Using this parameter, you can make the explosion appear to throw objects up into the air, which can give a more dramatic effect rather than a simple outward force. Force can be applied only to an active rigidbody. If a GameObject is inactive, AddExplosionForce has no effect.
```
using UnityEngine;
using System.Collections;  
  
// Applies an explosion force to all nearby rigidbodies
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float radius = 5.0F;
    public float power = 10.0F;  
  
    void Start()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) explosionPos = transform.position;
        Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[] colliders = Physics.OverlapSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphere.html)(explosionPos, radius);
        foreach (Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) hit in colliders)
        {
            Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb = hit.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
            if (rb != null)
                rb.AddExplosionForce(power, explosionPos, radius, 3.0F);
        }
    }
}

```

* * *
