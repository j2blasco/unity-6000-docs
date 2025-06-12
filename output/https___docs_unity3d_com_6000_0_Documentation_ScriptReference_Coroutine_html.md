* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html

# Coroutine
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
[MonoBehaviour.StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html) returns a Coroutine. Instances of this class are only used to reference these coroutines, and do not hold any exposed properties or functions.
A coroutine is a function that can suspend its execution (yield) until the given [YieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/YieldInstruction.html) finishes.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator WaitAndPrint()
    {
        // suspend execution for 5 seconds
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(5);
        print("WaitAndPrint " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }  
  
    IEnumerator Start()
    {
        print("Starting " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));  
  
        // Start function WaitAndPrint as a coroutine
        yield return StartCoroutine("WaitAndPrint");
        print("Done " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

This example shows a normal Start:
```
using UnityEngine;
using System.Collections;  
  
// In this example we show how to invoke a coroutine and execute
// the function in parallel.  Start does not need IEnumerator.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private IEnumerator coroutine;  
  
    void Start()
    {
        // - After 0 seconds, prints "Starting 0.0 seconds"
        // - After 0 seconds, prints "Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) started"
        // - After 2 seconds, prints "Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) ended: 2.0 seconds"
        print("Starting " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + " seconds");  
  
        // Start function WaitAndPrint as a coroutine.  
  
        coroutine = WaitAndPrint(2.0f);
        StartCoroutine(coroutine);  
  
        print("Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) started");
    }  
  
    private IEnumerator WaitAndPrint(float waitTime)
    {
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(waitTime);
        print("Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) ended: " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + " seconds");
    }
}

```

### Inherited Members
* * *
