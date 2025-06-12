* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Invoke.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).Invoke
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
public void Invoke(string methodName, float time); 
### Description
Invokes the method `methodName` in time seconds.
If time is set to 0 and Invoke is called before the first frame update, the method is invoked at the next Update cycle before [MonoBehaviour.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html). In this case, it's better to call the function directly.  
  
Note: Setting time to negative values is identical to setting it to 0.  
  
In other cases, the order of execution of the method depends on the timing of the invocation.  
  
If you need to pass parameters to your method, consider using [Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) instead. Coroutines also provide better performance.
```
using UnityEngine;
using System.Collections.Generic;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Launches a projectile in 2 seconds  
  
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) projectile;  
  
    void Start()
    {
        Invoke("LaunchProjectile", 2.0f);
    }  
  
    void LaunchProjectile()
    {
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) instance = Instantiate(projectile);
        instance.velocity = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 5.0f;
    }
}

```

* * *
