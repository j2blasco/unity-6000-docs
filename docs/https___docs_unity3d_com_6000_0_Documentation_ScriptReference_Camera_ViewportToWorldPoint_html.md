* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportToWorldPoint.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).ViewportToWorldPoint
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ViewportToWorldPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The 3d vector in Viewport space.  
### Returns
**Vector3** The 3d vector in World space. 
### Description
Transforms `position` from viewport space into world space.
Viewport space is normalized and relative to the camera. The bottom-left of the viewport is (0,0); the top-right is (1,1). The z position is in world units from the camera.  
  
Note that [ViewportToWorldPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportToWorldPoint.html) transforms an x-y screen position into a x-y-z position in 3D space.  
  
Provide the function with a vector where the x-y components of the vector are the screen coordinates and the z component is the distance of the resulting plane from the camera.
```
// Draw a yellow sphere at top-right corner of the near plane
// for the selected camera in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnDrawGizmosSelected()
    {
        Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p = camera.ViewportToWorldPoint(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 1, camera.nearClipPlane));
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(p, 0.1F);
    }
}

```

* * *
