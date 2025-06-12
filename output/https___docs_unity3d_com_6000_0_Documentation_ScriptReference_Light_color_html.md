* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-color.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).color
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color; 
### Description
Specifies the color emitted by the light.
To modify the light intensity you change the light's color luminance. Lights always add illumination, so a light with a black color is the same as no light at all.  
  
For more information, refer to [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html). 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) lt;  
  
    void Start()
    {
        lt = GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();
    }  
  
    // Darken the light completely over a period of 2 seconds.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        lt.color -= (Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html) / 2.0f) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }
}

```

Another example:
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Interpolate light color between two colors back and forth
    float duration = 1.0f;
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color0 = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color1 = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);  
  
    Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) lt;  
  
    void Start()
    {
        lt = GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // set light color
        float t = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), duration) / duration;
        lt.color = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(color0, color1, t);
    }
}

```

* * *
