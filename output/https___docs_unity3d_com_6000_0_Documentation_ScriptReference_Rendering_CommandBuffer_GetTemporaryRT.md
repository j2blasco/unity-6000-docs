* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.GetTemporaryRTArray.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).GetTemporaryRTArray
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
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format, int antiAliasing, bool enableRandomWrite, bool useDynamicScale); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format, int antiAliasing, bool enableRandomWrite); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format, int antiAliasing); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format, [RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html) readWrite, int antiAliasing); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format, [RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html) readWrite); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices); 
## Declaration
public void GetTemporaryRTArray(int nameID, int width, int height, int slices, int depthBuffer, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filter, [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format, [RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html) readWrite, int antiAliasing, bool enableRandomWrite); 
### Parameters
Parameter | Description  
---|---  
nameID | Shader property name for this texture.  
width | Width in pixels, or -1 for "camera pixel width".  
height | Height in pixels, or -1 for "camera pixel height".  
slices | Number of slices in texture array.  
depthBuffer | Depth buffer bits (0, 16 or 24).  
filter | Texture filtering mode (default is Point).  
format | Format of the render texture (default is ARGB32).  
readWrite | Color space conversion mode.  
antiAliasing | Anti-aliasing (default is no anti-aliasing).  
enableRandomWrite | Should random-write access into the texture be enabled (default is false).  
useDynamicScale | Whether to enable [DynamicResolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution.html) for the texture array.  
### Description
Add a "get a temporary render texture array" command.
This creates a temporary render texture array with given parameters, and sets it up as a global shader property with nameID. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to create the integer name.  
  
Release the temporary render texture array using [ReleaseTemporaryRT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.ReleaseTemporaryRT.html), passing the same nameID. Any temporary textures that were not explicitly released will be removed after camera is done rendering, or after [Graphics.ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBuffer.html) is done.  
  
After getting a temporary render texture array, you can set it as active ([SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetRenderTarget.html)) or blit to/from it ([Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.Blit.html)). You do not explicitly need to preserve active render targets during command buffer execution (current render targets are saved & restored afterwards).  
  
Additional resources: [ReleaseTemporaryRT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.ReleaseTemporaryRT.html), [SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetRenderTarget.html), [Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.Blit.html).
* * *
