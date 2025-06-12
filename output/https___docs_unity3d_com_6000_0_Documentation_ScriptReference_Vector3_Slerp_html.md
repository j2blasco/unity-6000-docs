* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Slerp.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Slerp
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slerp([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b, float t); 
### Description
Spherically interpolates between two vectors.
Interpolates between `a` and `b` by amount `t`. The difference between this and linear interpolation (aka, "lerp") is that the vectors are treated as directions rather than points in space. The direction of the returned vector is interpolated by the angle and its [magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html) is interpolated between the magnitudes of `from` and `to`.  
  
The parameter `t` is clamped to the range [0, 1].
```
// Animates the position in an arc between sunrise and sunset.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) sunrise;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) sunset;  
  
    // Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) to move from sunrise to sunset position, in seconds.
    public float journeyTime = 1.0f;  
  
    // The time at which the animation started.
    private float startTime;  
  
    void Start()
    {
        // Note the time at the start of the animation.
        startTime = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // The center of the arc
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center = (sunrise.position + sunset.position) * 0.5F;  
  
        // move the center a bit downwards to make the arc vertical
        center -= new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1, 0);  
  
        // Interpolate over the arc relative to center
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) riseRelCenter = sunrise.position - center;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) setRelCenter = sunset.position - center;  
  
        // The fraction of the animation that has happened so far is
        // equal to the elapsed time divided by the desired time for
        // the total journey.
        float fracComplete = (Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) - startTime) / journeyTime;  
  
        transform.position = Vector3.Slerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Slerp.html)(riseRelCenter, setRelCenter, fracComplete);
        transform.position += center;
    }
}

```

Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html), [SlerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SlerpUnclamped.html).
* * *
