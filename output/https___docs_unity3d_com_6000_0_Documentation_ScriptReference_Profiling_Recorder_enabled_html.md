* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder-enabled.html

#  [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).enabled
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
enabled; 
### Description
Enables recording.
When enabled Recorder collects data regardless of Profiler being enabled or not.  
  
**Note:**  
Set to _false_ to make measurements available immediately for synchronous testing scenarious.
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class Example
{
    public static void TimeSynchronousMethodWithMarkers()
    {
        var recorder = Recorder.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.Get.html)("MyMarker");
        recorder.enabled = true; // Starts measurements  
  
        // Call method which uses MyMarker
        // MyMethod();  
  
        recorder.enabled = false; // Stops measurements and makes data available immediately
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyMarker total time, ns: " + recorder.elapsedNanoseconds);
    }
}

```

* * *
