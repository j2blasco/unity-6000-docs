* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.MoveTowards.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).MoveTowards
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) MoveTowards([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) current, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) target, float maxDistanceDelta); 
### Parameters
Parameter | Description  
---|---  
current | The position to move from.  
target | The position to move towards.  
maxDistanceDelta | Distance to move `current` per call.  
### Returns
**Vector3** The new position. 
### Description
Calculate a position between the points specified by `current` and `target`, moving no farther than the distance specified by `maxDistanceDelta`.
Use the [MoveTowards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.MoveTowards.html) member to move an object at the `current` position toward the `target` position. By updating an object’s position each frame using the position calculated by this function, you can move it towards the target smoothly. Control the speed of movement with the `maxDistanceDelta` parameter. If the `current` position is already closer to the `target` than [maxDistanceDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-maxDistanceDelta.html), the value returned is equal to `target`; the new position does not overshoot `target`. To make sure that object speed is independent of frame rate, multiply the `maxDistanceDelta` value by [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) (or [Time.fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html) in a FixedUpdate loop).  
  
Note that if you set [maxDistanceDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-maxDistanceDelta.html) to a negative value, this function returns a position in the opposite direction from the `target`.
```
using UnityEngine;  
  
// Vector3.MoveTowards[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.MoveTowards.html) example.  
  
// A cube can be moved around the world. It is kept inside a 1 unit by 1 unit
// xz space. A small, long cylinder is created and positioned away from the center of
// the 1x1 unit. The cylinder is moved between two locations. Each time the cylinder is
// positioned the cube moves towards it. When the cube reaches the cylinder the cylinder
// is re-positioned to the other location. The cube then changes direction and moves
// towards the cylinder again.
//
// A floor object is created for you.
//
// To view this example, create a new 3d Project and create a Cube placed at
// the origin. Create Example.cs and change the script code to that shown below.
// Save the script and add to the Cube.
//
// Now run the example.  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Adjust the speed for the application.
    public float speed = 1.0f;  
  
    // The target (cylinder) position.
    private Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Awake()
    {
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the cube at the origin.
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f);  
  
        // Create and position the cylinder. Reduce the size.
        var cylinder = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cylinder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cylinder.html));
        cylinder.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.15f, 1.0f, 0.15f);  
  
        // Grab cylinder values and place on the target.
        target = cylinder.transform;
        target.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.8f, 0.0f, 0.8f);  
  
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the camera.
        Camera.main.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.85f, 1.0f, -3.0f);
        Camera.main.transform.localEulerAngles = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(15.0f, -20.0f, -0.5f);  
  
        // Create and position the floor.
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) floor = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
        floor.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, -1.0f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Move our position a step closer to the target.
        var step =  speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html); // calculate distance to move
        transform.position = Vector3.MoveTowards[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.MoveTowards.html)(transform.position, target.position, step);  
  
        // Check if the position of the cube and sphere are approximately equal.
        if (Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(transform.position, target.position) < 0.001f)
        {
            // Swap the position of the cylinder.
            target.position *= -1.0f;
        }
    }
}

```

* * *
