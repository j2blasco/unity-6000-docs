* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cameraToWorldMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).cameraToWorldMatrix
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) cameraToWorldMatrix; 
### Description
Matrix that transforms from camera space to world space (Read Only).
Use this to calculate where in the world a specific camera space point is.  
  
Note that camera space matches OpenGL convention: camera's forward is the negative Z axis. This is different from Unity's convention, where forward is the positive Z axis.
```
// Draw a yellow sphere in Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view at distance/
// units along camera's viewing direction.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float distance = -1.0F;
    void OnDrawGizmosSelected()
    {
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) m = Camera.main.cameraToWorldMatrix;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p = m.MultiplyPoint(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, distance));
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(p, 0.2F);
    }
}

```

* * *
