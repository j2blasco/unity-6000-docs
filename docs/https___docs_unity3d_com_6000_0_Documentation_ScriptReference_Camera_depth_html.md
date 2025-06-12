* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-depth.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).depth
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
depth; 
### Description
Camera's depth in the camera rendering order.
Cameras with lower depth are rendered before cameras with higher depth.  
  
Use this to control the order in which cameras are drawn if you have multiple cameras and some of them don't cover the full screen.  
  
Additional resources: [camera component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html), [Camera.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-rect.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        // Set this camera to render after the main camera
        cam.depth = Camera.main.depth + 1;
    }
}

```

* * *
