* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html

# LayerMask
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Specifies Layers to use in a [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html).
A [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) can use up to 32 [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html)s supported by the Editor. The first 8 of these `Layers` are specified by Unity; the following 24 are controllable by the user.  
  
Bitmasks represent the 32 Layers and define them as `true` or `false`. Each bitmask describes whether the `Layer` is used. As an example, bit 5 can be set to 1 (`true`). This will allow the use of the built-in `Water` setting.  
  
`Edit->Settings->Tags and Layers` option shows the use of the 32 bitmasks. Each `Layer` is shown with a string setting. As an example `Built-in Layer 0` is set as `Default`; `Built-in Layer 1` is set as `TransparentFX`. New named `Layer`s are added above bitmask layer 8. A selected `GameObject` will show the chosen `Layer` at top right of the Inspector. The example below has `User Layer 13` set to "Wall". This causes the assigned `GameObject` to be treated as part of a building.  
  
In the following script example, [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html) sends a ray into the world. [Camera.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html) can be rotated around the y-axis and fire a ray. Three [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)s represent walls that can be hit by the fired ray. Each [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has [GameObject.layer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-layer.html) set to the "Wall" [layerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask-layerMask.html). 
```
using UnityEngine;  
  
// Fire a gun at 3 walls in the scene.
//
// The Raycast will be aimed in the range of -45 to 45 degrees. If the Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) hits any of the
// walls true will be returned . The three walls all have a Wall Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) attached.  The left
// and right keys, and the space key, are all used to aim and fire.
//
// Quad floor based at (0, -0.5, 0), rotated in x by 90 degrees, scale (8, 8, 8).
// ZCube wall at (0, 0.5, 6), scale (3, 2, 0.5).
// LCube wall at (-3, 0, 3), scale (0.5, 1, 4).
// RCube wall at (3, 1.5, 3), scale (1, 4, 4).  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float cameraRotation;  
  
    void Start()
    {
        Camera.main.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0.5f, 0);
        cameraRotation = 0.0f;
    }  
  
    // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the camera based on what the user wants to look at.
    // Avoid rotating more than +/-45 degrees.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)("left"))
        {
            cameraRotation -= 1f;
            if (cameraRotation < -45.0f)
            {
                cameraRotation = -45.0f;
            }
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)("right"))
        {
            cameraRotation += 1f;
            if (cameraRotation > 45.0f)
            {
                cameraRotation = 45.0f;
            }
        }  
  
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the camera
        Camera.main.transform.localEulerAngles = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, cameraRotation, 0.0f);
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform = Camera.main.transform;  
  
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)("space"))
        {
            // Check for a Wall.
            LayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) mask = LayerMask.GetMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html)("Wall");  
  
            // Check if a Wall is hit.
            if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position, transform.forward, 20.0f, mask))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Fired and hit a wall");
            }
        }
    }
}

```

**Note:** [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) is a bitmask. Use [LayerMask.GetMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html) and [LayerMask.LayerToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html) to generate the bitmask. 
### Properties
Property | Description  
---|---  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask-value.html) | Converts a layer mask value to an integer value.  
### Static Methods
Method | Description  
---|---  
[GetMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.GetMask.html) | Given a set of layer names as defined by either a Builtin or a User Layer in the Tags and Layers manager, returns the equivalent layer mask for all of them.  
[LayerToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.LayerToName.html) | Given a layer number, returns the name of the layer as defined in either a Builtin or a User Layer in the Tags and Layers manager.  
[NameToLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.NameToLayer.html) | Given a layer name, returns the layer index as defined by either a Builtin or a User Layer in the Tags and Layers manager.  
### Operators
Operator | Description  
---|---  
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask-operator_int.html) | Implicitly converts an integer to a LayerMask.  
* * *
