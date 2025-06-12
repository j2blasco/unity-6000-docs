* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder-elapsedNanoseconds.html

#  [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).elapsedNanoseconds
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
elapsedNanoseconds; 
### Description
Accumulated time of Begin/End pairs for the previous frame in nanoseconds. (Read Only)
Long-lasting operations (for example, on a preloading thread) might not end within a single frame. In this case, **elapsedNanoseconds** is calculated until the end of the frame, so you can always see activity for these operations.
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Recorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) behaviourUpdateRecorder;
    void Start()
    {
        behaviourUpdateRecorder = Recorder.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.Get.html)("BehaviourUpdate");
        behaviourUpdateRecorder.enabled = true;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (behaviourUpdateRecorder.isValid)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("BehaviourUpdate time: " + behaviourUpdateRecorder.elapsedNanoseconds);
    }
}

```

Use _elapsedNanoseconds_ to retrieve timings of a code tagged with [ProfilerMarker.Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Auto.html).
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class Example
{
    public static void TimeSynchronousMethodWithMarkers()
    {
        var recorder = Recorder.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.Get.html)("MyMarker");
        recorder.enabled = true; // Start measurements  
  
        // Call method which uses MyMarker
        // MyMethod();  
  
        recorder.enabled = false; // Stops measurements and makes data available immediately
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyMarker total time, ns: " + recorder.elapsedNanoseconds);
    }
}

```

In synchronous measurements that don't involve a frame change, _elapsedNanoseconds_ only becomes a non-zero value after the Recorder is disabled.
* * *
