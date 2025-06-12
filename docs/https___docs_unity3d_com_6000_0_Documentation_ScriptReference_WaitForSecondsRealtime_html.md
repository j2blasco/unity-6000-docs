* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html

# WaitForSecondsRealtime
class in UnityEngine
/
Inherits from:[CustomYieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html)
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
Suspends the coroutine execution for the given amount of seconds using unscaled time.
See [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html) if you wish to wait using scaled time.  
WaitForSecondsRealtime can only be used with a `yield` statement in coroutines.
```
using UnityEngine;
using System.Collections;  
  
public class WaitForSecondsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(Example());
    }  
  
    IEnumerator Example()
    {
        print(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        yield return new WaitForSecondsRealtime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html)(5);
        print(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

See Also [MonoBehaviour.StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html).
### Properties
Property | Description  
---|---  
[waitTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime-waitTime.html) | The given amount of seconds that the yield instruction will wait for.  
### Constructors
Constructor | Description  
---|---  
[WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime-ctor.html) | Creates a yield instruction to wait for a given number of seconds using unscaled time.  
### Inherited Members
### Properties
Property | Description  
---|---  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) | Indicates if coroutine should be kept suspended.  
* * *
