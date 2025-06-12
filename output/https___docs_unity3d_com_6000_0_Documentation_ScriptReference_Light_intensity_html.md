* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-intensity.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).intensity
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
intensity; 
### Description
The Intensity of a light is multiplied with the Light color.
The value can be between 0 and 8. This allows you to create over bright lights.
```
using UnityEngine;  
  
public class example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) myLight;  
  
    void Start()
    {
        myLight = GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        myLight.intensity = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), 8);
    }
}

```

* * *
