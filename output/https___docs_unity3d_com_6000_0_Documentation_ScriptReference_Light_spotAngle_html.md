* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-spotAngle.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).spotAngle
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
spotAngle; 
### Description
The angle of the spot light's cone in degrees.
This is used primarily for [Spot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.Spot.html) lights and has no effect for [Point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.Point.html) lights Additional resources: [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Change spot angle randomly between 'minAngle' and 'maxAngle'
    // each 'interval' seconds.  
  
    float interval = 0.3f;
    float minAngle = 10;
    float maxAngle = 90;
    float timeLeft;  
  
    Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) lt;  
  

    void Start()
    {
        lt = GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();
        lt.type = LightType.Spot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.Spot.html);  
  
        timeLeft = interval;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        timeLeft -= Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        if (timeLeft < 0.0)
        {
            // time to change!
            timeLeft = interval;
            lt.spotAngle = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(minAngle, maxAngle);
        }
    }
}

```

* * *
