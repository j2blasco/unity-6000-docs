* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-angularVelocity.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).angularVelocity
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) angularVelocity; 
### Description
The angular velocity vector of the rigidbody measured in radians per second.
In most cases you should not modify it directly, as this can result in unrealistic behaviour. Note that if the Rigidbody has rotational constraints set, the corresponding angular velocity components are set to zero in the mass space (ie relative to the inertia tensor rotation) at the time of the call. Additionally, setting the angular velocity of a kinematic rigidbody is not allowed and will have no effect.
```
// Change the material depending on the speed of rotation
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) fastWheelMaterial;
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) slowWheelMaterial;
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;
    public MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) rend;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rend = GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (rb.angularVelocity.magnitude < 5)
            rend.sharedMaterial = slowWheelMaterial;
        else
            rend.sharedMaterial = fastWheelMaterial;
    }
}

```

* * *
