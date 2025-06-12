* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.Blit.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).Blit
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
public void Blit([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest); 
## Declaration
public void Blit([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat); 
## Declaration
public void Blit([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, int pass); 
## Declaration
public void Blit([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scale, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) offset); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, int pass); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scale, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) offset); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, int sourceDepthSlice, int destDepthSlice); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scale, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) offset, int sourceDepthSlice, int destDepthSlice); 
## Declaration
public void Blit([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat, int pass, int destDepthSlice); 
### Parameters
Parameter | Description  
---|---  
source | The source texture or [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html).  
dest | The destination [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html).  
mat | The material to use. If you don't provide `mat`, Unity uses a default material.  
pass | If the value is `-1`, Unity draws all the passes in `mat`. Otherwise, Unity draws only the pass you set `pass` to. The default value is `-1`.  
scale | The scale to apply.  
offset | The offset to apply.  
sourceDepthSlice | The element in the source texture to copy from, for example the texture in a texture array. You can't use `sourceDepthSlice` to specify a face in a Cubemap.  
destDepthSlice | The element in the destination texture to copy from, for example the texture in a texture array. You can't use `destDepthSlice` to specify a face in a Cubemap.  
### Description
Adds a command to use a shader to copy the pixel data from a texture into a render texture.
This method adds a command to copy pixel data from a texture on the GPU to a render texture on the GPU. This is one of the fastest ways to copy a texture.  
  
When you use `Graphics.Blit`, Unity does the following: 
  1. Sets the [active render texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) to the `dest` texture.
  2. Passes `source` to the `mat` material as the `_MainTex` property.
  3. Uses the material's shader to draw a full-screen surface from the `source` texture to the `dest` texture.


If you provide a `mat` material that doesn't have a `_MainTex` property, `Blit` doesn't use `source`.  
  
You can use `Graphics.Blit` to create [post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html), by setting `mat` to a material with a custom shader.  
  
`Blit` changes [RenderTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html). Store the active render texture before you use `Blit` if you need to use it afterwards.  
  
Avoid setting `source` and `dest` to the same render texture, as this may cause undefined behaviour. Use [Custom Render Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html) with double buffering instead, or use two render textures and alternate between them to implement double buffering manually.  
  
In linear color space, set [GL.sRGBWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-sRGBWrite.html) before using `Blit`, to make sure the sRGB-to-linear color conversion is what you expect.  
  
To blit to the screen in the Built-in Render Pipeline, follow these steps: 
  1. Set `dest` to `null`. Unity now uses `Camera.main.targetTexture` as the destination texture.
  2. Set the [Camera.targetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetTexture.html) property of [Camera.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html) to `null`.


To blit to the screen in the Universal Render Pipeline (URP) or the High Definition Render Pipeline (HDRP), you must call [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html) or [CommandBuffer.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.Blit.html) inside a method that you call from the [RenderPipelineManager.endContextRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html) callback.  
  
If you want to use a depth or stencil buffer that is part of the `source` (Render)texture, or blit to a subregion of a texture, you have to manually write an equivalent of the [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html) function - i.e. [Graphics.SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html) with destination color buffer and source depth buffer, setup orthographic projection ([GL.LoadOrtho](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)), setup material pass ([Material.SetPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPass.html)) and draw a quad ([GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)).  
  
Often the previous content of the Blit `dest` does not need to be preserved. In this case, it is recommended to activate the `dest` render target explicitly with the appropriate load and store actions using SetRenderTarget. The Blit dest should then be set to [BuiltinRenderTextureType.CurrentActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.CurrentActive.html).  
  
Additional resources: [Graphics.BlitMultiTap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.BlitMultiTap.html), [Post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html).
* * *
