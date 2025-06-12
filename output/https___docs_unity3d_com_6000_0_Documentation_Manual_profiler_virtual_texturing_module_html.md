* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-virtual-texturing-module.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Texture optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureLoading.html)
  * [Streaming Virtual Texturing](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html)
  * Virtual Texturing Profiler module


[](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-error-material.html)
Virtual Texturing error material
[](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
Textures reference
# Virtual Texturing Profiler module
The Virtual Texturing **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module displays statistics about [Streaming Virtual Texturing](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html) in your application. Virtual Texturing reduces the amount of GPU memory that your application uses, and the loading times of textures in your application if there are a lot of high resolution textures in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
To open the Profiler window, go to menu: **Window > Analysis > Profiler**.
**Note:** To use the Virtual Texturing Profiler module, in your project’s **Player Settings** , you must enable **Virtual Texturing** (**Edit > Project Settings > Player > Other Settings**).
![Virtual Texturing Profiler module](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-virtual-texturing.png) Virtual Texturing Profiler module
The chart displays information about the texture tiles that are on screen while your application is running, and how much memory the textures use. When you select the Virtual Texturing module, the lower pane of the Profiler window displays statistics such as how much cache size the virtual textures use.
The Virtual Texturing Profiler module’s chart is divided into the following categories:
**Chart** | **Description**  
---|---  
**Required Tiles** | The number of texture tiles that were visible on screen. These are the tiles that the **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) tried to sample to render the selected frame.  
**Max Cache Mip Bias** | The automatic mipmap bias applied to all textures with the same **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat). If this value isn’t zero, then the cache isn’t large enough to hold all the tiles of that format that are visible. The higher the mipmap bias, the lower the texture quality.  
**Max Cache Demand** | The highest cache demand of all GPU caches in the selected frame.  
**Missing Streaming Tiles** | The number of tiles that were visible on the screen but weren’t in video memory. Your application streams these tiles from the disk or copies them from main memory as soon as possible.  
**Missing Disk Data** | The remaining data (in bytes) that your application needed to read from the disk to satisfy the selected frame.  
## Module details pane
When you click on the Virtual Texturing Profiler module, the details pane in the lower half of the window displays further detailed statistics. These statistics are also available via the [ProfilerRecorder API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) and in the [Profiler Module Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html) so you can add them to a [custom Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-modules.html).
The statistics in the details pane are as follows:
**Statistic** | **Description**  
---|---  
**System Statistics** | This section of the details pane displays information about your application’s texture tiles and the resources they used during the Profiler capture. These statistics are available for both player builds, and profiling Play mode in the Unity Editor.  
Tiles required this frame | The number of texture tiles that were visible on screen. These are the tiles that the shaders tried to sample to render the selected frame. If all these tiles are in the GPU cache then Unity renders the frame with the highest possible texture quality for the cache size.   
  
Unless the Scene was frozen, then some of the tiles weren’t in the GPU memory yet. In this case, the virtual texturing sample uses a lower quality sample from a higher mipmap that’s in memory, until the higher quality sample arrives in memory.  
  
The cache mipmap bias affects the number of required tiles. If the mipmap bias isn’t zero for all caches then the number of required tiles is lower than the number required for the optimal texture quality.  
Max Cache Mip Bias | The mipmap bias of the GPU cache with the highest mipmap bias. If this isn’t zero then at least one of the caches isn’t large enough to hold all the texture tiles to render the selected frame at the optimal texture quality.  
Max Cache Demand | The highest cache demand of all GPU caches the selected frame represented as a percentage of the GPU. The GPU cache that has the highest demand might need to be larger to avoid mipmap biasing for this cache.  
  
If the Max Cache Demand statistic is a low percentage then the caches might be too large for the render resolution and content. The main downside of this is that your application is using more GPU memory than it needs but this isn’t a problem if your application isn’t memory constrained.  
Total CPU Cache Size | The amount of memory that Unity allocated to stored texture tiles after it loaded them from disk.  
Total GPU Cache Size | The size of all GPU caches that the Virtual Texturing module allocated in the selected frame. Unity creates a GPU cache when a material that uses a texture of that texture format is rendered.  
Atlases | The number of virtual texture spaces or atlases (maximum of 64). Unity atlasses the textures that are streamed with virtual texturing into large virtual texture spaces. This is automatic and transparent.  
**Player Build Statistics** | This section of the details pane displays information about your application’s texture tiles that are only available when you profile a build of your application.  
Missing Disk Data | The remaining data (in bytes) that the application needed to read from disk to satisfy the selected frame. There might be more disk read requests queued up from requests in previous frames that aren’t visible anymore. As such, this is the minimum amount of data that the application reads from disk if no new tiles become visible. The actual amount of data the application reads might be larger.  
Missing Streaming Tiles | The number of tiles that were visible on the screen but weren’t in memory yet. These tiles were streamed from disk as soon as possible. This number might be higher if, for example, the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) moves. This statistic falls to zero if the scene and camera froze and no new tiles were visible.  
Read From Disk | The number of bytes of disk read operations that Unity completed in the selected frame.  
**Per Cache Statistics** | Displays statistics about the cache. Only available when you profile a build of your application.  
Cache Format | The [graphics formats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) that the textures in your application used.  
Demand | The amount of cache demand each [graphics format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) used. **Note:** This statistic is not available in custom profilers  
Bias | The amount of mipmap bias cache each [graphics format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) used. **Note:** This statistic is not available in custom profilers  
## Additional resources
  * [Profiler window introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-error-material.html)
Virtual Texturing error material
[](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
Textures reference
