* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StopCoroutine.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).StopCoroutine
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
public void StopCoroutine(string methodName); 
## Declaration
public void StopCoroutine(IEnumerator routine); 
## Declaration
public void StopCoroutine([Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) routine); 
### Parameters
Parameter | Description  
---|---  
methodName | Name of coroutine.  
routine | Name of the function in code, including coroutines.  
### Description
Stops the first coroutine named `methodName`, or the coroutine stored in `routine` running on this behaviour.
StopCoroutine takes one of three arguments which specify which coroutine is stopped: 
  * A string function naming the active coroutine
  * The `IEnumerator` variable used earlier to create the coroutine.
  * The `Coroutine` to stop the manually created `Coroutine`.


**Note:** Do not mix the three arguments. If a string is used as the argument in [StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html), use the string in StopCoroutine. Similarly, use the `IEnumerator` in both [StartCoroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StartCoroutine.html) and StopCoroutine. Finally, use `StopCoroutine` with the `Coroutine` used for creation.  
  
In the CS example, the [IEnumerator](https://msdn.microsoft.com/en-us/library/system.collections.ienumerator\(v=vs.110\).aspx) type is used.
```
using UnityEngine;
using System.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // keep a copy of the executing script
    private IEnumerator coroutine;  
  
    // Use this for initialization
    void Start()
    {
        print("Starting " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        coroutine = WaitAndPrint(3.0f);
        StartCoroutine(coroutine);
        print("Done " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }  
  
    // print to the console every 3 seconds.
    // yield is causing WaitAndPrint to pause every 3 seconds
    public IEnumerator WaitAndPrint(float waitTime)
    {
        while (true)
        {
            yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(waitTime);
            print("WaitAndPrint " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        }
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space"))
        {
            StopCoroutine(coroutine);
            print("Stopped " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        }
    }
}

```

The following cs example shows how StopCoroutine(Coroutine) can be used. 
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
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.0f);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineA() started: " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));  
  
        // wait for another 1 second and then create b
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.0f);
        Coroutine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) b = StartCoroutine(coroutineB());  
  
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(2.0f);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineA() finished " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));  
  
        // B() was expected to run for 10 seconds
        // but was shut down here after 3.0f
        StopCoroutine(b);
        yield return null;
    }  
  
    IEnumerator coroutineB()
    {
        float f = 0.0f;
        float start = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineB() started " + start);  
  
        while (f < 10.0f)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineB(): " + f);
            yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.0f);
            f = f + 1.0f;
        }  
  
        // Intended to handling exit of the this coroutine.
        // However coroutineA() shuts coroutineB() down. This
        // means the following lines are not called.
        float t = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) - start;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("coroutineB() finished " + t);
        yield return null;
    }
}

```

* * *
