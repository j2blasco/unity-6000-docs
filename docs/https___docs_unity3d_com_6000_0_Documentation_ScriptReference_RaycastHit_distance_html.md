* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-distance.html

#  [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html).distance
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
distance; 
### Description
The distance from the ray's origin to the impact point.
In the case of a ray, the distance represents the magnitude of the vector from the ray's origin to the impact point.  
  
In the case of a swept volume or sphere cast, the distance represents the magnitude of the vector from the origin point to the translated point at which the volume contacts the other collider.  
  
Note that [RaycastHit.point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-point.html) represents the point in space where the collision occurs.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Movable, levitating object.  
  
    // This works by measuring the distance to ground with a
    // raycast then applying a force that decreases as the object
    // reaches the desired levitation height.  
  
    // Vary the parameters below to
    // get different control effects. For example, reducing the
    // hover damping will tend to make the object bounce if it
    // passes over an object underneath.  
  
    // Forward movement force.
    float moveForce = 1.0f;  
  
    // Torque for left/right rotation.
    float rotateTorque = 1.0f;  
  
    // Desired hovering height.
    float hoverHeight = 4.0f;  
  
    // The force applied per unit of distance below the desired height.
    float hoverForce = 5.0f;  
  
    // The amount that the lifting force is reduced per unit of upward speed.
    // This damping tends to stop the object from bouncing after passing over
    // something.
    float hoverDamp = 0.5f;  
  
    // Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component.
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        // Fairly high drag makes the object easier to control.
        rb.drag = 0.5f;
        rb.angularDrag = 0.5f;
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // Push/turn the object based on arrow key input.
        rb.AddForce(Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical") * moveForce * transform.forward);
        rb.AddTorque(Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") * rotateTorque * Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));  
  
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) downRay = new Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html)(transform.position, -Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));  
  
        // Cast a ray straight downwards.
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(downRay, out hit))
        {
            // The "error" in height is the difference between the desired height
            // and the height measured by the raycast distance.
            float hoverError = hoverHeight - hit.distance;  
  
            // Only apply a lifting force if the object is too low (ie, let
            // gravity pull it downward if it is too high).
            if (hoverError > 0)
            {
                // Subtract the damping from the lifting force and apply it to
                // the rigidbody.
                float upwardSpeed = rb.velocity.y;
                float lift = hoverError * hoverForce - upwardSpeed * hoverDamp;
                rb.AddForce(lift * Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
            }
        }
    }
}

```

Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Physics.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html), [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html).
* * *
