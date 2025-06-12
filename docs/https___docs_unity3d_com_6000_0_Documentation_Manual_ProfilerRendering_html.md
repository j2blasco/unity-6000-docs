* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerRendering.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * Rendering Profiler module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-troubleshoot.html)
Troubleshooting the Frame Time Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html)
GPU Usage Profiler module
# Rendering Profiler module reference
The Rendering **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) displays rendering statistics and information about what the CPU and GPU do to render the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). You can use these statistics to measure the resource intensity of different areas of the Scene, which is useful for optimization.
To open the Profiler window, go to menu: **Window > Analysis > Profiler**.
The chart displays the number of Batches, SetPass Calls, Triangles and Vertices your application rendered. The lower pane displays more rendering statistics, which match the ones shown in the GameView [Rendering Statistics](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html) window.
![The Rendering Profiler module](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RenderProfiler.png) The Rendering Profiler module
The Rendering Profiler module’s chart is divided into four categories as follows:
**Chart** | **Description**  
---|---  
**Batches Count** | The number of [batches](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) Unity processed during a frame.  
**SetPass Calls Count** | The number of times Unity switched which **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) pass it used to render **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) during a frame. A shader might contain several shader passes and each pass renders GameObjects in the scene differently.  
**Triangles Count** | The number of [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangle.html) Unity processed during a frame.  
**Vertices Count** | The number of [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) Unity processed during a frame.  
## Module details pane
When you click on the Rendering Profiler module, the details pane in the lower half of the window displays detailed rendering statistics. These statistics are similar to the statistics shown in the [Rendering Statistics](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html) window.
In the top left of the details pane, select Open Frame Debugger to open the [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html), which gives you information on individual drawcalls that rendered the frame.
These statistics are also available via the [ProfilerRecorder API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) and in the [Profiler Module Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html) so you can add them to a custom Profiler module.
**Statistic** | **Description** | **Accessible in Release Players**  
---|---|---  
**SetPass Calls** | The number of times Unity switched which shader pass it used to render GameObjects during a frame. A shader might contain several shader passes and each pass renders GameObjects in the scene differently. | Yes  
**Draw Calls** | The total number of draw calls Unity issued during a frame. Unity issues draw calls when it renders GameObjects to the screen. This number includes non batched draw calls as well as dynamic and static batched draw calls. | Yes  
**Batches** | The total number of [batches](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) Unity processed during a frame. This number includes both static and dynamic batches. | Yes  
**Triangles** | The number of [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html) Unity processed during a frame. | Yes  
**Vertices** | The number of [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) Unity processed during the frame. | Yes  
**(Dynamic Batching)** | This section contains statistics on [dynamic batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching). | No  
Batched Draw Calls | The number of draw calls Unity combined into dynamic batches. | No  
Batches | The number of dynamic batches Unity processed during the frame. | No  
Triangles | The number of triangles in the GameObjects included in the dynamic batches. | No  
Vertices | The number of vertices in the GameObjects included in the dynamic batches. | No  
Time | The time Unity spent creating dynamic batching structures. | No  
**(Static Batching)** | This section contains statistics on [static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching). | No  
Batched Draw Calls | The number of draw calls Unity combined into static batches. | No  
Batches | The number of static batches Unity processed during a frame. | No  
Triangles | The number of triangles in the GameObjects included in the static batches. | No  
Vertices | The number of vertices in the GameObjects included in the static batches. | No  
**(Instancing)** | This section contains statistics on [GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html). | No  
Batched Draw Calls | The number of draw calls Unity combined into instance batches. | No  
Batches | The number of batches Unity processed to render [instanced](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html) GameObjects during a frame. | No  
Triangles | The number of triangles in the instanced GameObjects. | No  
Vertices | The number of vertices in the instanced GameObjects. | No  
**Used Textures** | The number of [textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) Unity used during the frame and the amount of memory the textures used. | No  
****Render Textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture)** | The number of [RenderTextures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html) Unity used during the frame and the amount of memory the RenderTextures used. | Yes  
**Render Textures Changes** | The number of times Unity set one or multiple RenderTextures as render targets during the frame. | Yes  
**Used Buffers** | The total number of GPU buffers and memory they used. This includes vertex, index and compute buffers and all internal buffers required for rendering. | Yes  
**Vertex Buffer Upload In Frame** | The amount of geometry that the CPU uploaded to the GPU in the frame. This represents the vertex/normal/texcoord data. There might already be some geometry on the GPU. This statistic only includes geometry that Unity transfers in a frame. | Yes  
**Index Buffer Upload In Frame Count** | The amount of geometry that the CPU uploaded to the GPU in the frame. This represents the triangle indices data. There might already be some geometry on the GPU. This statistic only includes geometry that Unity transfers in a frame. | Yes  
**Shadow Casters Count** | The number of GameObjects that cast shadows in a frame. If a GameObject casts multiple shadows (because multiple lights light it), it has one entry per shadow it casts. | Yes  
## Availability in Players
The Rendering module **Profiler counters** Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilercounter) are also available in Players. Use the [ProfilerRecorder API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) to access Render Profiler module information in Players. High level counters are also available in Release Player.
The following example contains a simple script that collects `SetPass Calls Count`, `Draw Calls Count` and `Vertices Count` metrics and displays those as TextArea.
```
using System.Text;
using Unity.Profiling;
using UnityEngine;
 
public class RenderStatsScript : MonoBehaviour
{
    string statsText;
    ProfilerRecorder setPassCallsRecorder;
    ProfilerRecorder drawCallsRecorder;
    ProfilerRecorder verticesRecorder;

    void OnEnable()
    {
        setPassCallsRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Render, "SetPass Calls Count");
        drawCallsRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Render, "Draw Calls Count");
        verticesRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Render, "Vertices Count");
    }
 
    void OnDisable()
    {
        setPassCallsRecorder.Dispose();
        drawCallsRecorder.Dispose();
        verticesRecorder.Dispose();
    }

    void Update()
    {
        var sb = new StringBuilder(500);
        if (setPassCallsRecorder.Valid)
            sb.AppendLine($"SetPass Calls: {setPassCallsRecorder.LastValue}");
        if (drawCallsRecorder.Valid)
            sb.AppendLine($"Draw Calls: {drawCallsRecorder.LastValue}");
        if (verticesRecorder.Valid)
            sb.AppendLine($"Vertices: {verticesRecorder.LastValue}");
        statsText = sb.ToString();
    }
 
    void OnGUI()
    {
        GUI.TextArea(new Rect(10, 30, 250, 50), statsText);
    }
}

```

The Rendering Profiler module information belongs to the [ProfilerCategory.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Render.html) **Profiler category** Identifies the workload data for a Unity subsystem (for example, Rendering, Scripting and Animation categories). Unity applies color-coding to categories to visually distinguish between the types of data in the **Profiler** window.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilercategory).
If you want to highlight the selected Rendering counters in a custom module, use the [Module Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html) to configure the chart and detailed view.
## Additional resources
  * [Profiler window introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-troubleshoot.html)
Troubleshooting the Frame Time Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html)
GPU Usage Profiler module
