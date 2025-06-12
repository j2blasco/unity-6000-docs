* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-reflectionProbeChanged.html

#  [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).reflectionProbeChanged
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html "Go to ReflectionProbe Component in the Manual")
### Description
Adds a delegate to get notifications when a Reflection Probe is added to a Scene or removed from a Scene.
Additional resources: [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html), [ReflectionProbeEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.ReflectionProbeEvent.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ReflectionProbeManager : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static void OnReflectionProbeEvent(ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) probe, ReflectionProbe.ReflectionProbeEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.ReflectionProbeEvent.html) eventType)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("A ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) event has occured: " + eventType);
    }  
  
    void Start()
    {
        ReflectionProbe.reflectionProbeChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-reflectionProbeChanged.html) += OnReflectionProbeEvent;
    }  
  
    void OnDestroy()
    {
        ReflectionProbe.reflectionProbeChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-reflectionProbeChanged.html) -= OnReflectionProbeEvent;
    }
}

```

* * *
