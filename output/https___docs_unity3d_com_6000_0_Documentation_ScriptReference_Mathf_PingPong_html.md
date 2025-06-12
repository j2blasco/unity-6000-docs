* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).PingPong
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static float PingPong(float t, float length); 
### Description
PingPong returns a value that increments and decrements between zero and the length. It follows the triangle wave formula where the bottom is set to zero and the peak is set to `length`.
PingPong requires the value `t` to be a self-incrementing value. For example, Time.time and Time.unscaledTime.  
  
The example below shows a simple use case with the light intensity going from 0 to 8 to 0 continuously.
```
using UnityEngine;  
  
public class PingPongExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
The example below shows some outputs as example.
```
using UnityEngine;  
  
public class OutputExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints 2
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(2, 5));  
  
        // Prints 3
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(7, 5));
 
        // Prints 1
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(11, 5));
    }
}
```

* * *
