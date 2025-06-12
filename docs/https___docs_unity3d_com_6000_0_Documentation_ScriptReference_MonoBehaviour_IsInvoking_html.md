* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.IsInvoking.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).IsInvoking
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
## Declaration
public bool IsInvoking(string methodName); 
### Description
Is any invoke on `methodName` pending?
```
using UnityEngine;
using System.Collections.Generic;  
  
// Instantiates a projectile two seconds after the spacebar was pressed.
// LaunchProjectile is called when a previous RigidBody has finished the Invoke.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) projectile;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)) && !IsInvoking("LaunchProjectile"))
            Invoke("LaunchProjectile", 2.0f);
    }  
  
    void LaunchProjectile()
    {
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) instance = Instantiate(projectile);
        instance.velocity = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 5;
    }
}

```

* * *
## Declaration
public bool IsInvoking(); 
### Description
Is any invoke pending on this MonoBehaviour?
* * *
