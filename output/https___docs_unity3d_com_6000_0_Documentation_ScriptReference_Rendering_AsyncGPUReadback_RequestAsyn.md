* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestAsync.html

#  [AsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.html).RequestAsync
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
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) src, int size, int offset); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) src, int size, int offset); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) dstFormat); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) dstFormat); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, int x, int width, int y, int height, int z, int depth); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, int x, int width, int y, int height, int z, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) dstFormat); 
## Declaration
public static Awaitable<AsyncGPUReadbackRequest> RequestAsync([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int mipIndex, int x, int width, int y, int height, int z, int depth, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) dstFormat); 
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
z | Depth in pixels for [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) being fetched. Number of layers for TextureCube, TextureArray and TextureCubeArray.  
depth | Depth in pixels for [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) being fetched. Number of layers for TextureCube, TextureArray and TextureCubeArray.  
### Description
Retrieves data asynchronously from a GPU resource.
See [AsyncGPUReadback.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.Request.html).
* * *
