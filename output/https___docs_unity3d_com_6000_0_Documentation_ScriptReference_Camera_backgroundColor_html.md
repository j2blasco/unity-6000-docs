* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-backgroundColor.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).backgroundColor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) backgroundColor; 
### Description
The color with which the screen will be cleared.
Only used if [clearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-clearFlags.html) are set to [CameraClearFlags.SolidColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.SolidColor.html) (or [CameraClearFlags.Skybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.Skybox.html) but the skybox is not set up).
```
// ping-pong animate background color
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color1 = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color2 = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
    public float duration = 3.0F;  
  
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        cam.clearFlags = CameraClearFlags.SolidColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.SolidColor.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float t = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), duration) / duration;
        cam.backgroundColor = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(color1, color2, t);
    }
}

```

Additional resources: [camera component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html), [Camera.clearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-clearFlags.html)
* * *
