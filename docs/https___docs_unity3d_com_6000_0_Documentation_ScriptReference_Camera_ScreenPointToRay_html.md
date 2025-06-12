* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenPointToRay.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).ScreenPointToRay
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
public [Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ScreenPointToRay([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos); 
## Declaration
public [Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ScreenPointToRay([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos, [Camera.MonoOrStereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
pos | A 3D point, with the x and y coordinates containing a 2D screen space point in pixels. The lower left pixel of the screen is (0,0). The upper right pixel of the screen is (screen width in pixels - 1, screen height in pixels - 1). Unity ignores the z coordinate.  
eye | Optional argument that can be used to specify which eye transform to use. Default is Mono.  
### Description
Returns a ray going from camera through a screen point.
Resulting ray is in world space, starting on the near plane of the camera and going through position's (x,y) pixel coordinates on the screen.
```
//Attach this script to your Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
//This draws a line in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view going through a point 200 pixels from the lower-left corner of the screen
//To see this, enter Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html) and switch to the **Scene** tab. Zoom into your Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s position.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(200, 200, 0);  
  

    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = cam.ScreenPointToRay(pos);
        Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(ray.origin, ray.direction * 10, Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html));
    }
}

```

* * *
