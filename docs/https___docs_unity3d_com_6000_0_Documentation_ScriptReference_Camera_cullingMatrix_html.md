* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cullingMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).cullingMatrix
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) cullingMatrix; 
### Description
Sets a custom matrix for the camera to use for all culling queries.
This lasts until it is disabled by calling [ResetCullingMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetCullingMatrix.html).  
  
A custom culling matrix can be useful in situations where multiple cameras must be culled identically in order to render effects such as reflections.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cullingCamera;  
  
    void Awake()
    {
        cullingCamera = gameObject.AddComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        SetMainCameraCustomCullingMatrix(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(10.0f, 10.0f, 10.0f), Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html));
    }  
  
    void SetMainCameraCustomCullingMatrix(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) cameraPosition, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lookAtPosition)
    {
        transform.position = cameraPosition;
        transform.LookAt(lookAtPosition);
        Camera.main.cullingMatrix = cullingCamera.projectionMatrix * cullingCamera.worldToCameraMatrix;
    }  
  
    void ResetMainCameraCullingMatrix()
    {
        Camera.main.ResetCullingMatrix();
    }
}

```

* * *
