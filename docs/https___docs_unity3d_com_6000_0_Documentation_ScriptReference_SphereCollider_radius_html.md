* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider-radius.html

#  [SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html).radius
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html "Go to SphereCollider Component in the Manual")
radius; 
### Description
The radius of the sphere measured in the object's local space.
The sphere radius will be scaled by the transform's scale.
```
using UnityEngine;  
  
//Always attach a SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) component to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //This declares your SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html)
    SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) myCollider;  
  
    void Start()
    {
        //Assigns the attached SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) to myCollider
        myCollider = GetComponent<SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html)>();
    }  
  
    void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        //This increases the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) radius when the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) collides with a trigger Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)
        myCollider.radius += 2f;
    }
}

```

* * *
