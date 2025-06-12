* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inWeight.html

#  [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html).inWeight
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
inWeight; 
### Description
Sets the incoming weight for this key. The incoming weight affects the slope of the curve from the previous key to this key.
The weight is a value between 0 and 1. Set [weightedMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-weightedMode.html) to [WeightedMode.In](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.In.html) or [WeightedMode.Both](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.Both.html) to include weight when calculating the slope of the incoming curve.  
  
Additional resources: [outWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outWeight.html).
```
using UnityEngine;  
  
public class KeyFrameWeightExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)  animCurve = null;  
  
    void Start()
    {
        Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[] ks = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[3];  
  
        ks[0] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0, 0);
        ks[0].weightedMode = WeightedMode.In[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.In.html);
        ks[0].inWeight = 0.5f;  
  
        ks[1] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(4, 0);
        ks[1].weightedMode = WeightedMode.In[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.In.html);
        ks[1].inWeight = 0f;    // Zero weight.  The segment will be linear if previous keyframe outWeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outWeight.html) is also zero.  
  
        ks[2] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(6, 0);
        ks[2].weightedMode = WeightedMode.In[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.In.html);
        ks[2].inWeight = 1f / 3f;    // 1/3 is the default weight in WeightedMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.None.html) weightedMode.  
  
        animCurve = new AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)(ks);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (animCurve != null)
            transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), animCurve.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)), 0);
    }
}

```

* * *
