* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.GetRecorder.html

#  [Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html).GetRecorder
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
public [Profiling.Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) GetRecorder(); 
### Returns
**Recorder** [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) object associated with the Sampler. 
### Description
Returns [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) associated with the Sampler.
Each Sampler has only one recorder. Multiple calls to **GetRecorder** return references that control the same native Recorder object. If Sampler object is invalid, it returns invalid Recorder object as well.
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Recorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) behaviourUpdateRecorder;
    void Start()
    {
        var sampler = Sampler.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.Get.html)("BehaviourUpdate");
        behaviourUpdateRecorder = sampler.GetRecorder();
        if (behaviourUpdateRecorder.isValid)
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
**Note:** At the moment Samplers are available only in the Editor and Development Players. Use [Sampler.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-isValid.html) to verify if Sampler can be used to create a valid Recorder.  
  
Additional resources: [Sampler.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler-isValid.html), [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html), [Recorder.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder-isValid.html).
* * *
