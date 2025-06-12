* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.WorldToViewportPoint.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).WorldToViewportPoint
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) WorldToViewportPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) WorldToViewportPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Camera.MonoOrStereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
position | A 3D point in world space.  
eye | Optional argument that can be used to specify which eye transform to use. Default is Mono.  
### Description
Transforms `position` from world space into viewport space.
Viewport space is normalized and relative to the camera. The bottom-left of the camera is (0,0); the top-right is (1,1). The z position is in world units from the camera.
```
// Finds out whether target is on the left or right side of the screen
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) viewPos = cam.WorldToViewportPoint(target.position);
        if (viewPos.x > 0.5F)
            print("target is on the right side!");
        else
            print("target is on the left side!");
    }
}

```

* * *
