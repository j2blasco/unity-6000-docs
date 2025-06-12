* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).StartCoroutine
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
public [Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) StartCoroutine(IEnumerator routine); 
### Description
Starts a Coroutine.
The execution of a coroutine can be paused at any point using the yield statement. When a yield statement is used, the coroutine pauses execution and automatically resumes at the next frame. See the [ Coroutines](https://docs.unity3d.com/6000.0/Documentation/Manual/Coroutines.html) documentation for more details.  
  
Coroutines are excellent when modeling behavior over several frames. The StartCoroutine method returns upon the first yield return, however you can yield the result, which waits until the coroutine has finished execution. There is no guarantee coroutines end in the same order they started, even if they finish in the same frame.  
  
Yielding of any type, including null, results in the execution coming back on a later frame, unless the coroutine is stopped or has completed.  
  
Note: You can stop a coroutine using MonoBehaviour.StopCoroutine and MonoBehaviour.StopAllCoroutines. Coroutines are also stopped when the MonoBehaviour is destroyed or if the GameObject the MonoBehaviour is attached to is disabled. Coroutines are not stopped when a MonoBehaviour is disabled.  
  
See also: [Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html), [YieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/YieldInstruction.html)  
  
An example of [StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html):
```
using UnityEngine;
using System.Collections;  
  

public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // In this example we show how to invoke a coroutine and
    // continue executing the function in parallel.  
  
    private IEnumerator coroutine;  
  
    void Start()
    {
        // - After 0 seconds, prints "Starting 0.0"
        // - After 0 seconds, prints "Before WaitAndPrint Finishes 0.0"
        // - After 2 seconds, prints "WaitAndPrint 2.0"
        print("Starting " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));  
  
        // Start function WaitAndPrint as a coroutine.  
  
        coroutine = WaitAndPrint(2.0f);
        StartCoroutine(coroutine);  
  
        print("Before WaitAndPrint Finishes " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }  
  
    // every 2 seconds perform the print()
    private IEnumerator WaitAndPrint(float waitTime)
    {
        while (true)
        {
            yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(waitTime);
            print("WaitAndPrint " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        }
    }
}

```

Another example:
```
// In this example we show how to invoke a coroutine and wait until it
// is completed  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        // - After 0 seconds, prints "Starting 0.0"
        // - After 2 seconds, prints "WaitAndPrint 2.0"
        // - After 2 seconds, prints "Done 2.0"
        print("Starting " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));  
  
        // Start function WaitAndPrint as a coroutine. And wait until it is completed.
        // the same as yield return WaitAndPrint(2.0f);
        yield return StartCoroutine(WaitAndPrint(2.0f));
        print("Done " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }  
  
    // suspend execution for waitTime seconds
    IEnumerator WaitAndPrint(float waitTime)
    {
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(waitTime);
        print("WaitAndPrint " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

* * *
## Declaration
public [Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) StartCoroutine(string methodName, object value = null); 
### Description
Starts a coroutine named `methodName`.
In most cases you want to use the StartCoroutine variation above. However StartCoroutine using a string method name lets you use [StopCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StopCoroutine.html) with a specific method name. The downside is that the string version has a higher runtime overhead to start the coroutine and you can pass only one parameter.
```
// In this example we show how to invoke a coroutine using a string name and stop it.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        StartCoroutine("DoSomething", 2.0f);
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1);
        StopCoroutine("DoSomething");
    }  
  
    IEnumerator DoSomething(float someParameter)
    {
        while (true)
        {
            print("DoSomething Loop");  
  
            // Yield execution of this coroutine and return to the main loop until next frame
            yield return null;
        }
    }
}

```

A created coroutine can start another coroutine. These two coroutines can operate together in many ways. This includes both coroutines running in parallel. Alternatively one coroutine can stop the other while it continues itself. The example below shows one coroutine pausing as it starts another one. When the second coroutine finishes it restarts the first one.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(coroutineA());
    }  
  
    IEnumerator coroutineA()
    {
        // wait for 1 second
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineA created");
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.0f);
        yield return StartCoroutine(coroutineB());
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineA running again");
    }  
  
    IEnumerator coroutineB()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineB created");
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(2.5f);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineB enables coroutineA to run");
    }
}

```

* * *
