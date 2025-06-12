* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Texture optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
  * Introduction to mipmap streaming


[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
Optimizing GPU texture memory with mipmap streaming
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-use.html)
Enable mipmap streaming
# Introduction to mipmap streaming
Use mipmap streaming to limit the size of textures in GPU memory.
## How mipmap streaming works
For each texture in the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) view, Unity automatically calculates and loads mipmap levels only up to a specific level, instead of loading all of them. This means that Unity only transfers some mipmap levels per texture from disk to the CPU and the GPU.
Unity loads mipmap levels at the highest resolution possible, but uses lower mipmap levels if higher resolution mipmap levels don’t fit in the memory limit you set. For more information about setting a memory limit, refer to [Configure mipmap streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-configure.html).
Unity caches mipmap levels on the GPU, to avoid repeatedly loading mipmap levels from disk and the CPU.
## Limitations
  * Unity doesn’t support mipmap streaming on [terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) textures, because Unity needs the highest resolution mipmap levels at all times.
  * Unity doesn’t support mipmap streaming with texture arrays, **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) arrays, or 3D textures.
  * If you use an API such as [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html) to render a texture, Unity doesn’t have the information it needs to calculate a mipmap level. Set the mipmap level for the texture manually with the [Texture2D.requestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html) API, or disable mipmap streaming on the texture.
  * Unity might not be able to calculate the correct mipmap level for textures that don’t use the special `_ST` property for texture tiling and offset. For more information about the `_ST` property, refer to [Accessing shader properties in Cg/HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
Optimizing GPU texture memory with mipmap streaming
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-use.html)
Enable mipmap streaming
