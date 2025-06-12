* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.BlitMultiTap.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).BlitMultiTap
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
public static void BlitMultiTap([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, params Vector2[] offsets); 
## Declaration
public static void BlitMultiTap([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, int destDepthSlice, params Vector2[] offsets); 
## Declaration
public static void BlitMultiTap([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [Rendering.GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, params Vector2[] offsets); 
## Declaration
public static void BlitMultiTap([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [Rendering.GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, int destDepthSlice, params Vector2[] offsets); 
### Parameters
Parameter | Description  
---|---  
source | Source texture.  
dest | Destination [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html), or `null` to blit directly to screen.  
mat | Material to use for copying. Material's shader should do some post-processing effect.  
offsets | Variable number of filtering offsets. Offsets are given in pixels.  
destDepthSlice | The texture array destination slice to blit to.  
### Description
Copies source texture into destination, for multi-tap shader.
This is mostly used for implementing some [post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html). For example, Gaussian or iterative Cone blurring samples source texture at multiple different locations.  
  
BlitMultiTap sets `dest` to be the active render target (changing [RenderTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) and [GraphicsTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture-active.html)), sets `source` as `_MainTex` property on the material, and draws a full-screen quad. Each vertex of the quad has multiple texture coordinates set up, offset by `offsets` pixels.  
  
BlitMultiTap has the same limitations as [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html).  
  
Additional resources: [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html), [post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html).
* * *
