* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-material.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).material
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
[PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html) material; 
### Description
The material used by the collider.
If material is shared by colliders, it will duplicate the material and assign it to the collider.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Expose properties in the inspector for easy adjustment.
    float dynFriction;
    float statFriction;  
  
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) coll;  
  
    void Start()
    {
        coll = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();  
  
        coll.material.dynamicFriction = dynFriction;
        coll.material.staticFriction = statFriction;
    }
}

```

* * *
