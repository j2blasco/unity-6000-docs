* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html

# WaitForSeconds
class in UnityEngine
/
Inherits from:[YieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/YieldInstruction.html)
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
Suspends the coroutine execution for the given amount of seconds using scaled time.
The real time suspended is equal to the given time divided by [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html). See [WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html) if you wish to wait using unscaled time. [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html) can only be used with a `yield` statement in coroutines.  
  
There are some factors which can mean the actual amount of time waited does not precisely match the amount of time specified:  
**1.** Start waiting at the `end` of the current frame. If you start [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html) with duration 't' in a long frame (for example, one which has a long operation which blocks the main thread such as some synchronous loading), the coroutine will return 't' seconds after the end of the frame, not 't' seconds after it was called.  
**2.** Allow the coroutine to resume on the first frame after 't' seconds has passed, not exactly after 't' seconds has passed.
```
using UnityEngine;
using System.Collections;  
  
public class WaitForSecondsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //Start the coroutine we define below named ExampleCoroutine.
        StartCoroutine(ExampleCoroutine());
    }  
  
    IEnumerator ExampleCoroutine()
    {
        //Print the time of when the function is first called.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Started Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) at timestamp : " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));  
  
        //yield on a new YieldInstruction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/YieldInstruction.html) that waits for 5 seconds.
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(5);  
  
        //After we have waited 5 seconds print the time again.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Finished Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) at timestamp : " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

Additional resources: [MonoBehaviour.StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html), [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html), [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html), [WaitForFixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForFixedUpdate.html), [WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html), [WaitUntil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil.html), [WaitWhile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html).
### Constructors
Constructor | Description  
---|---  
[WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds-ctor.html) | Suspends the coroutine execution for the given amount of seconds using scaled time.  
### Inherited Members
* * *
