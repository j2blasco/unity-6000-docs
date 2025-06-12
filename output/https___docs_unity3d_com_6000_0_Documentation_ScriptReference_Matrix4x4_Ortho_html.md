* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Ortho.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).Ortho
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
## Declaration
public static [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) Ortho(float left, float right, float bottom, float top, float zNear, float zFar); 
### Parameters
Parameter | Description  
---|---  
left | Left-side x-coordinate.  
right | Right-side x-coordinate.  
bottom | Bottom y-coordinate.  
top | Top y-coordinate.  
zNear | Near depth clipping plane value.  
zFar | Far depth clipping plane value.  
### Returns
**Matrix4x4** The projection matrix. 
### Description
Create an orthogonal projection matrix.
The returned matrix, when used as a Camera's projection matrix, creates a projection of the area between `left`, `right`, `top` and `bottom`, with `zNear` and `zFar` as the near and far depth clipping planes into a cube going from (left, bottom, near) = (-1, -1, -1) to (right, top, far) = (1, 1, 1).  
  
The returned matrix embeds a z-flip operation whose purpose is to cancel the z-flip performed by the camera view matrix. If the view matrix is an identity or some custom matrix that doesn't perform a z-flip, consider multiplying the third column of the projection matrix (i.e. m02, m12, m22 and m32) by -1.  
  
Projection matrices in Unity follow [OpenGL](https://en.wikipedia.org/wiki/OpenGL) convention, i.e. clip space near plane is at `z=-1`, and far plane is at `z=1`.  
  
Note that depending on the graphics API used, projection matrices in shaders can follow different convention, for example the D3D-style clip space has near plane at zero and far plane at one; and "reversed Z" projection has near plane at one and far plane at zero. To calculate projection matrix value suitable for passing to shader variables, use [GL.GetGPUProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // create orthographic matrix
        var matrix = Matrix4x4.Ortho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Ortho.html)(-4, 4, -2, 2, 1, 100);
        // will print:
        // 0.25000 0.00000  0.00000  0.00000
        // 0.00000 0.50000  0.00000  0.00000
        // 0.00000 0.00000 -0.02020 -1.02020
        // 0.00000 0.00000  0.00000  1.00000
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("projection matrix\n" + matrix);  
  
        // get shader-compatible projection matrix value
        var shaderMatrix = GL.GetGPUProjectionMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html)(matrix, false);
        // on a Direct3D-like graphics API, will print:
        // 0.25000 0.00000  0.00000  0.00000
        // 0.00000 0.50000  0.00000  0.00000
        // 0.00000 0.00000 0.01010 1.01010
        // 0.00000 0.00000 0.00000 1.00000
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("shader projection matrix\n" + shaderMatrix);
    }
}
```

Additional resources: [Perspective](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Perspective.html), [Camera.projectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-projectionMatrix.html), [GL.LoadPixelMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadPixelMatrix.html), [GL.LoadProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadProjectionMatrix.html), [GL.GetGPUProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html).
* * *
