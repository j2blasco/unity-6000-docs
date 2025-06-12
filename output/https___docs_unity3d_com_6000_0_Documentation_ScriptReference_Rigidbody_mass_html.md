* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-mass.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).mass
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
mass; 
### Description
The mass of the rigidbody.
Different Rigidbodies with large differences in mass can make the physics simulation unstable.  
  
Higher mass objects push lower mass objects more when colliding. Think of a big truck, hitting a small car.  
  
A common mistake is to assume that heavy objects fall faster than light ones. This is not true as the speed is dependent on gravity and damping.
```
// Expose mass to allow adjustment from
// the inspector.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float mass;
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rb.mass = mass;
    }
}

```

* * *
