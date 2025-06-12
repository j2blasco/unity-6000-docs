* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-range.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).range
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
range; 
### Description
The range of each point of the light.  
  
Since area lights have a light emitting surface instead of a single point, the cumulative range of the light is larger than this property. This larger range can be read from the [Light.dilatedRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-dilatedRange.html) property. For non-area lights, Light.range and Light.dilatedRange return the same value. 
Additional resources: [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Pulse light's range between original range
    // and half of the original one  
  
    float duration  = 3.0f;
    float originalRange;  
  
    Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) lt;  
  
    void Start()
    {
        lt = GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();
        originalRange = lt.range;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var amplitude = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), duration);  
  
        // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) from 0..duration to 0.5..1 range.
        amplitude = amplitude / duration * 0.5f + 0.5f;  
  
        // Set light range.
        lt.range = originalRange * amplitude;
    }
}

```

* * *
