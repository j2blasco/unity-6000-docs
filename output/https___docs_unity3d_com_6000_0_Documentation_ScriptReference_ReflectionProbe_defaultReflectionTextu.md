* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultReflectionTexture.html

#  [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).defaultReflectionTexture
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
Adds a delegate to get notifications when the default specular Cubemap is changed.
Additional resources: [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ReflectionProbeManager : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static void OnSetDefaultReflection(Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) cubemap)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Default reflection cubemap was changed.");
    }  
  
    void Start()
    {
        ReflectionProbe.defaultReflectionTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultReflectionTexture.html) += OnSetDefaultReflection;
    }  
  
    void OnDestroy()
    {
        ReflectionProbe.defaultReflectionTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultReflectionTexture.html) -= OnSetDefaultReflection;
    }
}

```

* * *
