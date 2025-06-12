* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SparseTextures.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Texture optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureLoading.html)
  * Sparse Textures


[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-analyze.html)
Analyze mipmap streaming
[](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html)
Streaming Virtual Texturing
# Sparse Textures
**Sparse textures** (also known as “tiled textures” or “mega-textures”) are textures that are too large to fit in graphic memory in their entirety. To handle them, Unity breaks the main texture down into smaller rectangular sections known as “tiles”. Individual tiles can then be loaded as necessary. For example, if the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) can only see a small area of a sparse texture, then only the tiles that are currently visible need to be in memory.
Aside from the tiling, a sparse texture behaves like any other texture in usage. **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) can use them without special modification and they can have mipmaps, use all texture filtering modes, etc. If a particular tile cannot be loaded for some reason then the result is undefined; some GPUs show a black area where the missing tile should be but this behaviour is not standardised.
Not all hardware and platforms support sparse textures. For example, on DirectX systems they require [DX11.2](http://msdn.microsoft.com/en-us/library/windows/desktop/dn312084.aspx) (Windows 8.1) and a fairly recent GPU. On OpenGL they require [ARB_sparse_texture](http://www.opengl.org/registry/specs/ARB/sparse_texture.txt) extension support. Sparse textures only support non-compressed **texture formats** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat).
See the [SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html) script reference page for further details about handling sparse textures from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
## Example Project
A minimal example project for sparse textures is available [here](https://docs.unity3d.com/6000.0/Documentation/uploads/Examples/SparseTextureExample.zip).
![Sparse texture as shown in the example project](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SparseTextureExample.jpg) Sparse texture as shown in the example project
The example shows a simple procedural texture pattern and lets you move the camera to view different parts of it. Note that the project requires a recent GPU and a DirectX 11.2 (Windows 8.1) system, or using OpenGL with _ARB_sparse_texture_ support.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-analyze.html)
Analyze mipmap streaming
[](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html)
Streaming Virtual Texturing
