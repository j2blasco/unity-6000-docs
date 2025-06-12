* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportPointToRay.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).ViewportPointToRay
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
public [Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ViewportPointToRay([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos); 
## Declaration
public [Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ViewportPointToRay([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos, [Camera.MonoOrStereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
eye | Optional argument that can be used to specify which eye transform to use. Default is Mono.  
### Description
Returns a ray going from camera through a viewport point.
Resulting ray is in world space, starting on the near plane of the camera and going through position's (x,y) coordinates on the viewport (position.z is ignored).  
  
Viewport coordinates are normalized and relative to the camera. The bottom-left of the camera is (0,0); the top-right is (1,1).
```
// Prints the name of the object camera is directly looking at
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = cam.ViewportPointToRay(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.5F, 0.5F, 0));
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, out hit))
            print("I'm looking at " + hit.transform.name);
        else
            print("I'm looking at nothing!");
    }
}

```

* * *
