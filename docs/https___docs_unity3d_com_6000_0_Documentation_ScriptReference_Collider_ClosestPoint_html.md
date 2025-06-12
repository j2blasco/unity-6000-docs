* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.ClosestPoint.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).ClosestPoint
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ClosestPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Parameters
Parameter | Description  
---|---  
position | Location you want to find the closest point to.  
### Returns
**Vector3** The closest point on the collider, returned in world space coordinates. 
### Description
The closest point on the collider given a specified location.
This method computes the point on the Collider that is closest to a 3D location in the world. In the example below `closestPoint` is the point on the Collider and `location` is the point in 3D space. If `location` is in the Collider the `closestPoint` is inside. If the Collider is disabled, the method returns the input `position`.  
  
**Note:** The difference from [ClosestPointOnBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.ClosestPointOnBounds.html) is that the returned point is actually on the collider instead of on the bounds of the collider. ([bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-bounds.html) is a box that surrounds the collider.)
```
using UnityEngine;  
  
// Note that closestPoint is based on the surface of the collider
// and location represents a point in 3d space.
// The gizmos work in the editor.
//
// Create an origin-based cube and give it a scale of (1, 0.5, 3).
// Change the BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) size to (0.8, 1.2, 0.8).  This means that
// collisions will happen when a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gets close to the BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html).
// The ShowClosestPoint.cs script shows spheres that display the location
// and closestPoint.  Try changing the BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) size and the location
// values.  
  
// Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component attached
public class ShowClosestPoint : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) location;  
  
    public void OnDrawGizmos()
    {
        var collider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();  
  
        if (!collider)
        {
            return; // nothing to do without a collider
        }  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) closestPoint = collider.ClosestPoint(location);  
  
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(location, 0.1f);
        Gizmos.DrawWireSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireSphere.html)(closestPoint, 0.1f);
    }
}

```

**Note:** Same as [Physics.ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ClosestPoint.html) but doesn't allow passing a custom position and rotation. Instead, it uses the position of the collider. 
* * *
