* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-normal.html

#  [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html).normal
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal; 
### Description
The normal of the surface the ray hit.
The normal of the surface the ray hit on the collider where the ray intersects, which may or may not match the original mesh surface depending on the collider type and settings. For primitive colliders such as BoxCollider or SphereCollider, the normal is calculated based on their simple geometric shape. For MeshCollider, if convex is set to false (non-convex), Unity can return the actual interpolated normal from the mesh surface at the hit point. If convex is true, the normal is instead approximated from the convex hull of the mesh. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Calculate the reflection of a "laser beam" off a clicked object.  
  
    // The object from which the beam is fired. The incoming beam will
    // not be visible if the camera is used for this!
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) gunObj;  
  
    void Start()
    {
        gunObj = this.GetComponent<Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)>();
    }
    
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(0))
        {
            RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
            Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = Camera.main.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));  
  
            if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, out hit))
            {
                // Find the line from the gun to the point that was clicked.
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) incomingVec = hit.point - gunObj.position;  
  
                // Use the point's normal to calculate the reflection vector.
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) reflectVec = Vector3.Reflect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Reflect.html)(incomingVec, hit.normal);  
  
                // Draw lines to show the incoming "beam" and the reflection.
                Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(gunObj.position, hit.point, Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
                Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(hit.point, reflectVec, Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
            }
        }
    }
}

```

Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Physics.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html), [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html).
* * *
