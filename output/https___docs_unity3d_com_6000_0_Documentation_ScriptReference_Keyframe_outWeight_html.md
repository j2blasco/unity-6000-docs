* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outWeight.html

#  [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html).outWeight
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
outWeight; 
### Description
Sets the outgoing weight for this key. The outgoing weight affects the slope of the curve from this key to the next key.
The weight is a value between 0 and 1. Set [weightedMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-weightedMode.html) to [WeightedMode.Out](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.Out.html) or [WeightedMode.Both](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.Both.html) to include weight when calculating the slope of the outgoing curve.  
  
Additional resources: [inWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inWeight.html).
```
using UnityEngine;  
  
public class KeyFrameWeightExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)  animCurve = null;  
  
    void Start()
    {
        Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[] ks = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[3];  
  
        ks[0] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0, 0);
        ks[0].weightedMode = WeightedMode.Out[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.Out.html);
        ks[0].outWeight = 0.5f;  
  
        ks[1] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(4, 0);
        ks[1].weightedMode = WeightedMode.Out[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.Out.html);
        ks[1].outWeight = 0f;    // Zero weight.  The segment will be linear if next keyframe inWeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inWeight.html) is also zero.  
  
        ks[2] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(6, 0);
        ks[2].weightedMode = WeightedMode.Out[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.Out.html);
        ks[2].outWeight = 1f / 3f;    // 1/3 is the default weight in WeightedMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.None.html) weightedMode.  
  
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
