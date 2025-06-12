* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.CancelInvoke.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).CancelInvoke
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
public void CancelInvoke(); 
### Description
Cancels all Invoke calls on this MonoBehaviour.
```
using UnityEngine;
using System.Collections.Generic;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) projectile;  
  
    void Start()
    {
        // Starting in 2 seconds, a projectile will be launched every 0.3 seconds
        InvokeRepeating("LaunchProjectile", 2, 0.3F);
    }  
  
    void LaunchProjectile()
    {
        // Create a projectile GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and set its velocity to a random direction
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instance = Instantiate(projectile);
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rigidbody = instance.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        rigidbody.velocity = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 5;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Cancel all Invoke calls
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("Fire1"))
            CancelInvoke();
    }
}

```

* * *
## Declaration
public void CancelInvoke(string methodName); 
### Description
Cancels all Invoke calls with name `methodName` on this behaviour.
```
using UnityEngine;
using System.Collections.Generic;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) projectile;  
  
    void Start()
    {
        // Starting in 2 seconds, a projectile will be launched every 0.3 seconds
        InvokeRepeating("LaunchProjectile", 2, 0.3F);
    }  
  
    void LaunchProjectile()
    {
        // Create a projectile GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and set its velocity to a random direction
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instance = Instantiate(projectile);
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rigidbody = instance.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        rigidbody.velocity = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 5;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Cancel only the LaunchProjectile invoke
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("Fire1"))
            CancelInvoke("LaunchProjectile");
    }
}

```

* * *
