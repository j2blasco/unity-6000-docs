* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html

# WaitWhile
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
Suspends the coroutine execution until the supplied delegate evaluates to `false`.
WaitWhile can only be used with a `yield` statement in coroutines.  
  
The supplied delegate will be executed each frame after [MonoBehaviour.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) and before [MonoBehaviour.LateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html). When the delegate finally evaluates to `false`, the coroutine will proceed with its execution.
```
using UnityEngine;
using System.Collections;  
  
public class WaitWhileExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int frame;  
  
    void Start()
    {
        StartCoroutine(Example());
    }  
  
    IEnumerator Example()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Waiting for prince/princess to rescue me...");
        yield return new WaitWhile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html)(() => frame < 10);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Finally I have been rescued!");
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (frame <= 10)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Frame: " + frame);
            frame++;
        }
    }
}

```

Additional resources: [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html), [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html), [WaitForFixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForFixedUpdate.html), [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html), [WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html), [WaitUntil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil.html).
### Constructors
Constructor | Description  
---|---  
[WaitWhile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile-ctor.html) | Initializes a yield instruction with a given delegate to be evaluated.  
### Inherited Members
### Properties
Property | Description  
---|---  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) | Indicates if coroutine should be kept suspended.  
* * *
