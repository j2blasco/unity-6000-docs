* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoViewMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).SetStereoViewMatrix
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
public void SetStereoViewMatrix([Camera.StereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.html) eye, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix); 
### Parameters
Parameter | Description  
---|---  
eye | Specifies the stereoscopic view matrix to set.  
matrix | The matrix to be set.  
### Description
Sets a custom view matrix for a specific stereoscopic eye.
In most cases you should use the view matrices provided by the VR SDK to ensure accurate stereoscopic rendering. However, in some scenarios it can be useful to override the view matrices to achieve specific effects. For example, custom view matrices would be required to implement binoculars in VR.  
  
If custom view matrices have been set, then the Camera will analyze the view matrices to determine whether it is safe to use a single cull pass or if it must separately cull each eye. Use [Camera.areVRStereoViewMatricesWithinSingleCullTolerance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-areVRStereoViewMatricesWithinSingleCullTolerance.html) to find out which will be used.  
  
Calling [Camera.ResetStereoViewMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoViewMatrices.html) will revert the camera to using view matrices provided by the VR SDK. Note that the [Camera.stereoSeparation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoSeparation.html) will not be applied until you call [Camera.ResetStereoViewMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoViewMatrices.html).  
  
Additional resources: [Camera.ResetStereoViewMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoViewMatrices.html), [Camera.stereoSeparation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoSeparation.html), [Camera.areVRStereoViewMatricesWithinSingleCullTolerance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-areVRStereoViewMatricesWithinSingleCullTolerance.html)
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Use this for initialization
    void Start()
    {
    }  
  
    // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) is called once per frame
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();  
  
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) viewL = cam.worldToCameraMatrix;
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) viewR = cam.worldToCameraMatrix;  
  
        viewL[12] += 0.011f;
        viewR[12] -= 0.011f;
        cam.SetStereoViewMatrix(Camera.StereoscopicEye.Left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.Left.html), viewL);
        cam.SetStereoViewMatrix(Camera.StereoscopicEye.Right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.Right.html), viewR);
    }
}

```

* * *
