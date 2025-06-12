* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outTangent.html

#  [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html).outTangent
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
outTangent; 
### Description
Sets the outgoing tangent for this key. The outgoing tangent affects the slope of the curve from this key to the next key.
The outgoing tangent matches the outgoing slope of the curve. A positive value for [inTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inTangent.html) results in an upward tangent, while a negative value results in a downward tangent.  
  
Additional resources: [inTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inTangent.html).
```
using UnityEngine;  
  
public class KeyFrameTangentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)  animCurve = null;  
  
    void Start()
    {
        Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[] ks = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[3];  
  
        ks[0] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0, 0);
        ks[0].outTangent = 5f;    // +5 units on the y axis for 1 unit on the x axis.  
  
        ks[1] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(4, 0);
        ks[1].outTangent = 0f;    // straight  
  
        ks[2] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(6, 0);
        ks[2].outTangent = -5f;    // -5 units on the y axis for 1 unit on the x axis.  
  
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
