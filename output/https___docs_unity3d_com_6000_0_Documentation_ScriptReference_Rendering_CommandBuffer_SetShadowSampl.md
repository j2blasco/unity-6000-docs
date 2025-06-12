* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetShadowSamplingMode.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetShadowSamplingMode
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
public void SetShadowSamplingMode([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) shadowmap, [Rendering.ShadowSamplingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
shadowmap | Shadowmap render target to change the sampling mode on.  
mode | New sampling mode.  
### Description
Add a "set shadow sampling mode" command.
Shadowmap render textures are normally set up to be sampled with a comparison filter - the sampler gets a shadow-space depth value of the screen pixel and returns 0 or 1, depending on if the depth value in the shadowmap is smaller or larger. That's the default [ShadowSamplingMode.CompareDepths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.CompareDepths.html) mode and is used for rendering shadows.  
  
If you'd like to access the shadowmap values as in a regular texture, set the sampling mode to [ShadowSamplingMode.RawDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.RawDepth.html).  
  
Shadowmap's sampling mode will be reverted to default after the the last command in the current CommandBuffer.  
  
Check [SystemInfo.supportsRawShadowDepthSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRawShadowDepthSampling.html) to verify if current runtime platform supports sampling shadows this way. Notably, DirectX9 does not.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)))]
public class RawShadowmapDepth : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) m_Light;
    RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) m_ShadowmapCopy;  
  
    void Start()
    {
        RenderTargetIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) shadowmap = BuiltinRenderTextureType.CurrentActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.CurrentActive.html);
        m_ShadowmapCopy = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(1024, 1024, 0);
        CommandBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cb = new CommandBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html)();  
  
        // Change shadow sampling mode for m_Light's shadowmap.
        cb.SetShadowSamplingMode(shadowmap, ShadowSamplingMode.RawDepth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.RawDepth.html));  
  
        // The shadowmap values can now be sampled normally - copy it to a different render texture.
        cb.Blit(shadowmap, new RenderTargetIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html)(m_ShadowmapCopy));  
  
        // Execute after the shadowmap has been filled.
        m_Light.AddCommandBuffer(LightEvent.AfterShadowMap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMap.html), cb);  
  
        // Sampling mode is restored automatically after this command buffer completes, so shadows will render normally.
    }  
  
    void OnRenderImage(RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) src, RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) dest)
    {
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the shadowmap in the corner.
        Camera.main.rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 0.5f, 0.5f);
        Graphics.Blit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html)(m_ShadowmapCopy, dest);
        Camera.main.rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 1, 1);
    }
}

```

* * *
