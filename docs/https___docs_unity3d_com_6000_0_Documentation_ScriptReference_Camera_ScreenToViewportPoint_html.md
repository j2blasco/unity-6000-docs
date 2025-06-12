* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenToViewportPoint.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).ScreenToViewportPoint
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
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ScreenToViewportPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Description
Transforms `position` from screen space into viewport space.
Screen space is defined in pixels. The bottom-left of the screen is (0,0); the right-top is ([pixelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelWidth.html),[pixelHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelHeight.html)). The z position is in world units from the camera.  
  
Viewport space is normalized and relative to the camera. The bottom-left of the camera is (0,0); the top-right is (1,1). The z position is in world units from the camera.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.position = Camera.main.ScreenToViewportPoint(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));
    }
}

```

* * *
