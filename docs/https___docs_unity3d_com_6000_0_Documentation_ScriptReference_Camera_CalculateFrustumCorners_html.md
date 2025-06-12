* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CalculateFrustumCorners.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).CalculateFrustumCorners
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
public void CalculateFrustumCorners([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) viewport, float z, [Camera.MonoOrStereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html) eye, Vector3[] outCorners); 
### Parameters
Parameter | Description  
---|---  
viewport | Normalized viewport coordinates to use for the frustum calculation.  
z | Z-depth from the camera origin at which the corners will be calculated.  
eye | Camera eye projection matrix to use.  
outCorners | Output array for the frustum corner vectors. Cannot be null and length must be >= 4.  
### Description
Given viewport coordinates, calculates the view space vectors pointing to the four frustum corners at the specified camera depth.
The order of the corners is lower left, upper left, upper right, lower right.  
  
`CalculateFrustumCorners` can be used to efficiently calculate the world space position of a pixel in an image effect shader. See standard assets implementation of global fog.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // this example shows the different camera frustums when using asymmetric projection matrices (like those used by OpenVR).  
  
        var camera = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] frustumCorners = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[4];
        camera.CalculateFrustumCorners(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 1, 1), camera.farClipPlane, Camera.MonoOrStereoscopicEye.Mono[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Mono.html), frustumCorners);  
  
        for (int i = 0; i < 4; i++)
        {
            var worldSpaceCorner = camera.transform.TransformVector(frustumCorners[i]);
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(camera.transform.position, worldSpaceCorner, Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));
        }  
  
        camera.CalculateFrustumCorners(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 1, 1), camera.farClipPlane, Camera.MonoOrStereoscopicEye.Left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Left.html), frustumCorners);  
  
        for (int i = 0; i < 4; i++)
        {
            var worldSpaceCorner = camera.transform.TransformVector(frustumCorners[i]);
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(camera.transform.position, worldSpaceCorner, Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
        }  
  
        camera.CalculateFrustumCorners(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 1, 1), camera.farClipPlane, Camera.MonoOrStereoscopicEye.Right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Right.html), frustumCorners);  
  
        for (int i = 0; i < 4; i++)
        {
            var worldSpaceCorner = camera.transform.TransformVector(frustumCorners[i]);
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(camera.transform.position, worldSpaceCorner, Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
        }
    }
}

```

Which can be seen in the following image: ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/FrustumCorners.PNG).
* * *
