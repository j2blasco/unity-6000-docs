* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableRuntimeReflectionSystem.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# IScriptableRuntimeReflectionSystem
interface in UnityEngine.Experimental.Rendering
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
Defines the required members for a Runtime Reflection Systems.
You can use the empty implementation as base class, see [ScriptableRuntimeReflectionSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableRuntimeReflectionSystem.html).
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Experimental.Rendering;  
  
abstract class CustomRuntimeReflectionSystem : IScriptableRuntimeReflectionSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableRuntimeReflectionSystem.html)
{
    List<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)> m_RealtimeReflectionProbes = new List<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)>();
    List<RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)> m_RealtimeReflectionProbeTargets = new List<RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)>();  
  
    public bool TickRealtimeProbes()
    {
        for (int i = 0, c = m_RealtimeReflectionProbes.Count; i < c; ++i)
        {
            var probe = m_RealtimeReflectionProbes[i];
            var target = m_RealtimeReflectionProbeTargets[i];  
  
            RenderProbe(probe, target);  
  
            probe.realtimeTexture = target;
        }  
  
        return true;
    }  
  
    protected abstract void RenderProbe(ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) probe, RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) target);
    public abstract void Dispose();
}

```

### Public Methods
Method | Description  
---|---  
[TickRealtimeProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableRuntimeReflectionSystem.TickRealtimeProbes.html) | Update the reflection probes.  
* * *
