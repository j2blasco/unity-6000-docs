* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ComputePenetration.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).ComputePenetration
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
public static bool ComputePenetration([Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) colliderA, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) positionA, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotationA, [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) colliderB, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) positionB, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotationB, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out float distance); 
### Parameters
Parameter | Description  
---|---  
colliderA | The first collider.  
positionA | Position of the first collider.  
rotationA | Rotation of the first collider.  
colliderB | The second collider.  
positionB | Position of the second collider.  
rotationB | Rotation of the second collider.  
direction | Direction along which the translation required to separate the colliders apart is minimal.  
distance | The distance along direction that is required to separate the colliders apart.  
### Returns
**bool** True, if the colliders overlap at the given poses. 
### Description
Compute the minimal translation required to separate the given colliders apart at specified poses.
Translating the first collider by direction * distance will separate the colliders apart if the function returned true. Otherwise, direction and distance are not defined.  
  
One of the colliders has to be BoxCollider, SphereCollider CapsuleCollider or a convex MeshCollider. The other one can be any type.  
  
Note that you aren't restricted to the position and rotation the colliders have at the moment of the call. Passing position or rotation that is different from the currently set one doesn't have an effect of physically moving any colliders thus has no side effects on the Scene.  
  
Doesn't depend on any spatial structures to be updated first, so is not bound to be used only within FixedUpdate timeframe.  
  
Ignores backfaced triangles and doesn't respect [Physics.queriesHitBackfaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitBackfaces.html).  
  
This function is useful to write custom depenetration functions. One particular example is an implementation of a character controller where a specific reaction to collision with the surrounding physics objects is required. In this case, one would first query for the colliders nearby using OverlapSphere and then adjust the character's position using the data returned by ComputePenetration.
```
using UnityEngine;  
  
// Visualises the minimum translation vectors required to separate apart from other colliders found in a given radius
// Attach to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) attached.
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)()]
public class ShowPenetration : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float radius = 3f; // show penetration into the colliders located inside a sphere of this radius
    public int maxNeighbours = 16; // maximum amount of neighbours visualised  
  
    private Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[] neighbours;  
  
    public void Start()
    {
        neighbours = new Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[maxNeighbours];
    }  
  
    public void OnDrawGizmos()
    {
        var thisCollider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();  
  
        if (!thisCollider)
            return; // nothing to do without a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) attached  
  
        int count = Physics.OverlapSphereNonAlloc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphereNonAlloc.html)(transform.position, radius, neighbours);  
  
        for (int i = 0; i < count; ++i)
        {
            var collider = neighbours[i];  
  
            if (collider == thisCollider)
                continue; // skip ourself  
  
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) otherPosition = collider.gameObject.transform.position;
            Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) otherRotation = collider.gameObject.transform.rotation;  
  
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction;
            float distance;  
  
            bool overlapped = Physics.ComputePenetration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ComputePenetration.html)(
                thisCollider, transform.position, transform.rotation,
                collider, otherPosition, otherRotation,
                out direction, out distance
            );  
  
            // draw a line showing the depenetration direction if overlapped
            if (overlapped)
            {
                Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
                Gizmos.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawRay.html)(otherPosition, direction * distance);
            }
        }
    }
}

```

* * *
