* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html

# Space
enumeration
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
### Description
The coordinate spaces in which to apply transformation to a GameObject.
You can pass a value from this enum as a parameter to methods such as [Transform.Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Rotate.html) and [Transform.Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Translate.html) to specify which coordinate space the transformation is applied in.  
  
World coordinate space represented by [Space.World](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) refers to the position of a GameObject relative to the origin point (0,0,0) of the x-, y-, and z-axes of the scene. The [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) property gives a GameObject's current position in world space.  
  
Use [Space.World](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) to transform a GameObject relative to its [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) and the scene axes, ignoring the GameObject's own orientation. For example, `transform.Translate(Vector3.forward, Space.World)` adds one unit to the object's [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) on the z-axis of the scene.  
  
Local coordinate space represented by [Space.Self](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) refers to the position of an object relative to its parent GameObject, including any rotation of the parent GameObject. The [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) property gives a GameObject's current position in local space, which is relative to the parent GameObject if there is one. If a GameObject has no parent, its [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) is the same as its [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html).  
  
For example, a GameObject with no parent and a [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) of (1,3,0) will also have a [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) of (1,3,0). But if a child GameObject to this first object has [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) (1,3,0), the child object's [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) is (0,0,0) because it's in the same position as the parent object.  
  
Use [Space.Self](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) to transform a GameObject relative to its [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) and its own local axes, taking its orientation into account. For example, `Transform.Translate(Vector3.forward, Space.Self)` adds one unit to the object's [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) on the z-axis of the object, which may differ from the z-axis of the scene depending on the object's orientation. Select an object in the Scene view to see its local position and axes.  
  
For more information, refer to [Transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html), [Rotation and orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html), and [Position GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html) in the Manual. 
```
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
// This example demonstrates the difference between Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) and Space.Self[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) in rotation.
// The inWorldSpace field is automatically exposed as a checkbox in the **Inspector** window labelled **In World Space**. Enable or disable the checkbox in the **Inspector** to start in world or self space, respectively.
// Press play to see the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rotating appropriately. Press space or toggle the **In World Space** checkbox to switch between world and self space.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float rotationSpeed;
    public bool inWorldSpace;  
  
    void Start()
    {
        // Set the speed of the rotation
        rotationSpeed = 20.0f;
        // Start off in World.Space
        inWorldSpace = true;
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) a little at the start to show the difference between world and local spaces
        transform.Rotate(60, 0, 60);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in world space if inWorldSpace is true
        if (inWorldSpace)
            transform.Rotate(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * rotationSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
        // Otherwise, rotate the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in local space
        else
            transform.Rotate(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * rotationSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), Space.Self[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html));  
  
        // Press the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) button to switch between world and local space states
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            // Make the current state switch to the other state
            inWorldSpace = !inWorldSpace;
            // Output the current state to the console
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("World space : " + inWorldSpace.ToString());
        }
    }
}

```

Additional resources: [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), [Transform.Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Rotate.html), [Transform.Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Translate.html). 
### Properties
Property | Description  
---|---  
[World](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) | World coordinate space, relative to the origin point (0,0,0) of the x-, y-, and z-axes of the scene.  
[Self](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) | The local coordinate system of a GameObject relative to its parent, including orientation.  
* * *
