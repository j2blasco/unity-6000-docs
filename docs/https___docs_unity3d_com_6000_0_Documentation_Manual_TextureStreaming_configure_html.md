* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-configure.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Texture optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureLoading.html)
  * [Optimizing GPU texture memory with mipmap streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
  * Configure mipmap streaming 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-use.html)
Enable mipmap streaming
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-override-mipmap-level.html)
Override the mipmap level of a texture
# Configure mipmap streaming
## Set which cameras use mipmap streaming
By default, all **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) use mipmap streaming when you enable it.
### Disable mipmap streaming on a single camera
Follow these steps:
  1. Select a camera in your scene.
  2. In the **Inspector** window, select **Add Component** > **Streaming Controller**.
  3. Disable the **Streaming Controller** component.


### Enable mipmap streaming on a single camera
Follow these steps:
  1. Go to **Edit** > **Project Settings** > **Quality**.
  2. In the **Textures** section, under **Mipmap Streaming** , disable **Add All Cameras**.
  3. Add a **Streaming Controller** component to the camera, and make sure it’s enabled.


## Set which mipmap levels a camera uses
Use the **Mipmap Bias** setting in a **Streaming Controller** component to force Unity to load smaller or larger mipmap levels than the ones mipmap streaming automatically chooses.
Unity adds the **Mipmap Bias** value to mipmap levels from textures in the camera view. For example, if you set **Mipmap Bias** to 2 and mipmap streaming chooses mipmap level 1 for a texture, Unity loads mipmap level 3 (1 + 2).
You can also use the [StreamingController.streamingMipmapBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StreamingController-streamingMipmapBias.html) API to control this setting.
## Set the memory budget for textures
To set the maximum GPU memory that Unity uses for textures, follow these steps:
  1. Go to **Edit** > **Project Settings** > **Quality**.
  2. In the **Textures** section, set the **Memory Budget** value in MB.


The memory budget is for both mipmap streaming, and all the mipmap levels of textures that don’t use mipmap streaming. For example, if you set **Memory Budget** to 100 MB, and you have 90 MB of textures that don’t use mipmap streaming, the memory budget for mipmap streaming is 10 MB.
To avoid exceeding the memory budget, Unity does the following:
  * Loads lower-resolution mipmap levels for textures. This can cause textures to pop or load slowly.
  * Removes unused mipmap levels from GPU memory, to make room for mipmap levels it needs.


You can use the **Max Level Reduction** property to stop Unity removing mipmap levels smaller than a certain level. This value is also the mipmap level Unity loads at first startup. For example, if you set **Max Level Reduction** to 2, Unity loads only mipmap levels at level 2 and larger, and keeps them in memory.
Unity must keep mipmap levels above the **Max Level Reduction** value in GPU memory. This might mean Unity exceeds the memory budget.
### Estimate a memory budget
To estimate a memory budget for your project, follow these steps:
  1. While your project runs, use the [Texture.desiredTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-desiredTextureMemory.html) API to get the total size of the textures Unity loads.
  2. Set **Memory Budget** to slightly higher than that value.


This lets you make sure Unity has enough texture memory available for the most resource-intensive areas of your scene, and prevent textures from dropping to a lower resolution. If you have extra memory available, you can set a larger memory budget so that Unity can keep texture data that’s not visible in your scene in a GPU cache.
**Note:** If you use `Texture.desiredTextureMemory` in the Editor, the total size might include textures Unity uses to render Editor windows.
### Set the memory budget at runtime
You can use the following APIs to set and control the memory budget at runtime:
  * [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html), for example `QualitySettings.streamingMipmapsActive`.
  * [Texture2D.streamingTextureDiscardUnusedMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTextureDiscardUnusedMips.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-use.html)
Enable mipmap streaming
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-override-mipmap-level.html)
Override the mipmap level of a texture
