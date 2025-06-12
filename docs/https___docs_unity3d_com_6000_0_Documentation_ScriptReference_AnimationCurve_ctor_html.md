* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-ctor.html

# AnimationCurve Constructor
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
public AnimationCurve(params Keyframe[] keys); 
### Parameters
Parameter | Description  
---|---  
keys | An array of Keyframes used to define the curve.  
### Description
Creates an animation curve from an arbitrary number of keyframes.
This creates a curve from variable number of [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html) parameters. If you want to create curve from an array of keyframes, create an empty curve and assign [keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html) property.
```
using UnityEngine;
using System.Collections;  
  
public class AnimCurveExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve;  
  
    void Start()
    {
        curve = new AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)(new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0, 0), new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(1, 1));
        curve.preWrapMode = WrapMode.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.PingPong.html);
        curve.postWrapMode = WrapMode.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.PingPong.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(transform.position.x, curve.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)), transform.position.z);
    }
}

```

* * *
## Declaration
public AnimationCurve(); 
### Description
Creates an empty animation curve.
* * *
