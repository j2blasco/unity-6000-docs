* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreCollision.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).IgnoreCollision
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
public static void IgnoreCollision([Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider1, [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider2, bool ignore = true); 
### Parameters
Parameter | Description  
---|---  
collider1 | Any collider.  
collider2 | Another collider you want to have `collider1` to start or stop ignoring collisions with.  
ignore | Whether or not the collisions between the two colliders should be ignored or not.  
### Description
Makes the collision detection system ignore all collisions between `collider1` and `collider2`.
This is useful, say, for preventing projectiles from colliding with the object that fires them.  
  
Note that [IgnoreCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreCollision.html) is not persistent. This means ignore collision state will not be stored in the editor when saving a scene.  
  
If `ignore` is false, collisions can occur. Set `ignore` to true to ignore collisions.  
  
Additional resources: [Physics.IgnoreLayerCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreLayerCollision.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) bulletPrefab;  
  
    void Start()
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) bullet = Instantiate(bulletPrefab) as Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html);
        Physics.IgnoreCollision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreCollision.html)(bullet.GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>(), GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>());
    }
}

```

* * *
