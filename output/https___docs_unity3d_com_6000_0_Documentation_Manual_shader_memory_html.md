* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-memory.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Reducing the size or number of shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
  * Control how much memory shaders use


[](https://docs.unity3d.com/6000.0/Documentation/Manual/avoid-shader-duplication.html)
Troubleshooting shader duplication from AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-debugging.html)
Debugging shaders
# Control how much memory shaders use
In your built application, Unity stores several ‘chunks’ of compressed **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variant data. Each chunk contains multiple shader variants. When Unity loads a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) at runtime, it loads all the scene’s chunks into CPU memory and decompresses them.
To reduce memory usage on platforms that have limited memory, you can limit the size of chunks and how many decompressed chunks Unity keeps in memory.
To do this, in [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings), select **Other Settings** > **Shader Variant Loading** and adjust the following settings:
  * Use **Default chunk size (MB)** to set the maximum size of compressed chunks Unity stores in your built application.
  * Use **Default chunk count** to limit how many decompressed chunks Unity keeps in memory. The default is `0`, which means there’s no limit.


See [PlayerSettings.SetDefaultShaderChunkCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkCount.html) for more information.
You can use **Override** to override the values for each platform individually. See [PlayerSettings.SetShaderChunkCountForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetShaderChunkCountForPlatform.html) for more information.
You can also use [Shader.maximumChunksOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-maximumChunksOverride.html) to override **Default chunk count** at runtime.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/avoid-shader-duplication.html)
Troubleshooting shader duplication from AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-debugging.html)
Debugging shaders
