* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.InvokeRepeating.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).InvokeRepeating
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
public void InvokeRepeating(string methodName, float time, float repeatRate); 
### Parameters
Parameter | Description  
---|---  
methodName | The name of a method to invoke.  
time | Start invoking after n seconds.  
repeatRate | Repeat every n seconds.  
### Description
Invokes the method `methodName` in `time` seconds, then repeatedly every `repeatRate` seconds.
To cancel InvokeRepeating use [MonoBehaviour.CancelInvoke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.CancelInvoke.html).  
  
**Note** :The time and repeatRate parameters depend on [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html). For example, if [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) is 0 InvokeRepeating will not invoke. On the other hand, if [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) is 2, InvokeRepeating will repeat twice as fast.
```
using UnityEngine;
using System.Collections.Generic;  
  
// Starting in 2 seconds.
// a projectile will be launched every 0.3 seconds  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) projectile;  
  
    void Start()
    {
        InvokeRepeating("LaunchProjectile", 2.0f, 0.3f);
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
