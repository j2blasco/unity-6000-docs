* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.Get.html

#  [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).Get
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
public static [Profiling.Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) Get(string samplerName); 
### Parameters
Parameter | Description  
---|---  
samplerName | Sampler name.  
### Returns
**Recorder** [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) object for the specified Sampler. 
### Description
Use this function to get a Recorder for the specific Profiler label.
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
Additional resources: [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html), [Sampler.GetRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.GetRecorder.html).
* * *
