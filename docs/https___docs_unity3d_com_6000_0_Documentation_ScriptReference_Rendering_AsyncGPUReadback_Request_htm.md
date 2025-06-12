* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.Request.html

#  [AsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.html).Request
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
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, int size, int offset, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, int size, int offset, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) dstFormat, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) dstFormat, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, int x, int width, int y, int height, int z, int depth, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, int x, int width, int y, int height, int z, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) dstFormat, Action<AsyncGPUReadbackRequest> callback); 
## Declaration
public static [Rendering.AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) Request([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, int x, int width, int y, int height, int z, int depth, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) dstFormat, Action<AsyncGPUReadbackRequest> callback); 
### Parameters
Parameter | Description  
---|---  
src | Resource to read the data from.  
size | Size in bytes of the data to be retrieved from the [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).  
offset | Offset in bytes in the [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).  
mipIndex | Index of the mipmap to be fetched.  
dstFormat | Target [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) of the data. If the target format is different from the format stored on the GPU, the conversion is automatic.  
x | Starting X coordinate in pixels of the Texture data to be fetched.  
width | Width in pixels of the Texture data to be fetched.  
y | Starting Y coordinate in pixels of the Texture data to be fetched.  
height | Height in pixels of the Texture data to be fetched.  
z | Start Z coordinate in pixels for the [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) being fetched. Index of Start layer for TextureCube, [Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.html) and TextureCubeArray being fetched.  
depth | Depth in pixels for [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) being fetched. Number of layers for TextureCube, TextureArray and TextureCubeArray.  
callback | An optional delegate System.Action called once the request is fullfilled. The completed request is passed as parameter to the System.Action.  
### Returns
**AsyncGPUReadbackRequest** Returns an [AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) that you can use to determine when the data is available. Otherwise, a request with an error is returned. 
### Description
Retrieves data asynchronously from a GPU resource.
If a request with an error is returned, calling [AsyncGPUReadbackRequest.hasError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-hasError.html) returns true.  
  
For texture data, the extents are checked against the size of the source texture. If graphics [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html) are set low enough to generate reduced size textures, then the reduced size must be requested. Use QualitySettings.masterTextureLimit to adjust the width and height (and x,y if required), by bit shifting right.  
  
For texture data, use the [SystemInfo.IsFormatSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.IsFormatSupported.html) method with the [GraphicsFormatUsage.ReadPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUsage.ReadPixels.html) flag to query if the format is supported.  
  
If you use this function to request data about a temporary render texture, don't release the texture using [RenderTexture.ReleaseTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ReleaseTemporary.html) until the request is complete.
* * *
