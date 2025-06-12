* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EndThreadProfiling.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).EndThreadProfiling
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
## Declaration
public static void EndThreadProfiling(); 
### Description
Frees the internal resources used by the Profiler for the thread.
Profiler allocates memory to store information about the thread. To free that memory use _EndThreadProfiling_. Once called, Profiler stops collecting any data on the thread.  
  
**Note:** Calling this method on an internal Unity thread (such as main thread, render thread or job system threads) has no effect.
```
using UnityEngine;
using UnityEngine.Profiling;
using System.Threading;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    CustomSampler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) sampler;
    void Start()
    {
        sampler = CustomSampler.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.Create.html)("MyCustomSampler");
        var thread = new Thread(MyThreadFunc) { IsBackground = true };
        thread.Start();
    }  
  
    void MyThreadFunc()
    {
        Profiler.BeginThreadProfiling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginThreadProfiling.html)("My threads", "My thread 1");
        // Now samples will show up in the profiler timeline view
        for (int i = 0; i < 10; i++)
        {
            sampler.Begin();
            // ...
            sampler.End();
        }  
  
        // Unregister the thread before exit
        Profiler.EndThreadProfiling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EndThreadProfiling.html)();
    }
}

```

Additional resources: [Profiler.BeginThreadProfiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginThreadProfiling.html), [CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html).
* * *
