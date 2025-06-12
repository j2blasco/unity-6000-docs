* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnRenderImage.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnRenderImage(RenderTexture,RenderTexture)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Parameters
Parameter | Description  
---|---  
source | A [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) containing the source image.  
destination | The [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) to update with the modified image.  
### Description
[Event function](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) that Unity calls after a [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) has finished rendering, that allows you to modify the Camera's final image.
In the Built-in Render Pipeline, Unity calls `OnRenderImage` on MonoBehaviours that are attached to the same GameObject as an enabled [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) component, after the Camera finished rendering. You can use `OnRenderImage` to create a fullscreen post-processing effect. These effects work by reading the pixels from the source image, using a Unity shader to modify the appearance of the pixels, and then rendering the result into the destination image. You would typically use [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html) to perform these steps.  
  
If multiple scripts on the same Camera implement `OnRenderImage`, Unity calls them in the order that they appear in the Camera Inspector window, starting from the top. The `destination` of one operation is the `source` of the next one; internally, Unity creates one or more temporary RenderTextures to store these intermediate results.  
  
On Android, to avoid banding or to use alpha in fullscreen effects, set [PlayerSettings.use32BitDisplayBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-use32BitDisplayBuffer.html) to `true`.  
  
`OnRenderImage` is not supported in the Scriptable Render Pipeline. To create custom fullscreen effects in the Universal Render Pipeline (URP), use the [ScriptableRenderPass](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRenderPass.html) API. To create custom fullscreen effects in the High Definition Render Pipeline (HDRP), use a [Fullscreen Custom Pass](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Custom-Pass.html).  
  
For information about using Unity's pre-built post-processing effects, see [Post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // A Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) with the Unity shader you want to process the image with
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;  
  
    void OnRenderImage(RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) src, RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) dest)
    {
        // Read pixels from the source RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), apply the material, copy the updated results to the destination RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)
        Graphics.Blit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html)(src, dest, mat);
    }
}

```

* * *
