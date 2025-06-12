* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ConvertToEquirect.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).ConvertToEquirect
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
## Declaration
public void ConvertToEquirect([RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) equirect, [Camera.MonoOrStereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
equirect | RenderTexture to render the equirect format to.  
eye | A Camera eye corresponding to the left or right eye for stereoscopic rendering, or neither for monoscopic rendering.  
### Description
Converts the render texture to equirectangular format (both stereoscopic or monoscopic equirect). The left eye will occupy the top half and the right eye will occupy the bottom. The monoscopic version will occupy the whole texture. Texture dimension must be of type [TextureDimension.Cube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TextureDimension.Cube.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class CreateEquirect : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) cubemap;
    public RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) cubemap2;
    public RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) equirect;
    public bool renderStereo = true;
    public float stereoSeparation = 0.064f;  
  
    void LateUpdate()
    {
        //assume cubemap and cubemap2 are rendered using Camera.RenderToCubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderToCubemap.html)() for left/right eyes  
  
        if (equirect == null)
            return;  
  
        if (renderStereo)
        {
            cubemap.ConvertToEquirect(equirect, Camera.MonoOrStereoscopicEye.Left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Left.html));
            cubemap2.ConvertToEquirect(equirect, Camera.MonoOrStereoscopicEye.Right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Right.html));
        }
        else
        {
            cubemap.ConvertToEquirect(equirect, Camera.MonoOrStereoscopicEye.Mono[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Mono.html));
        }
    }
}

```

* * *
