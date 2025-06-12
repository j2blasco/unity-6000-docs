* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-landing.html)
  * Rendering Statistics window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html)
Frame Debugger Event Information reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
Audio
# Rendering Statistics window reference
The Game view includes a Rendering Statistics window that displays real-time rendering information about your application during Play mode. To open this window, click the **Stats** button in the top right corner of the Game view. Unity displays the Statistics window as an overlay in the top right of the Game view. The rendering statistics shown in the Graphics section window are useful for optimizing performance. The exact set of statistics available varies according to the build target.
![Statistics window showing real-time rendering statistics. ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameViewStats.png) Statistics window showing real-time rendering statistics. 
## **Statistics**
The Graphics section of the Statistics window contains the following information:
**Statistic** | **Description**  
---|---  
****FPS** See first person shooter, frames per second.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FPS)** | The current number of frames Unity is able to draw per second.  
**CPU** |  **Main** : The total amount of time taken to process one frame. This number includes the time Unity takes to process the frame update of your application and the time Unity takes in the Editor to update the Scene view, other Editor Windows, or process Editor-only tasks.  
**Render** : The amount of time taken to render one frame. This number includes the time Unity takes to process the frame update for the Game view; it doesn’t include the time Unity takes in the Editor.  
**Batches** | The total number of [draw call batches](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) Unity processes during a frame. This number includes static, dynamic, and [instance](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html) batches.  
**Saved by batching** | The number of draw calls Unity combined into batches. To ensure good draw call batching, share materials between different ****GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)** as often as possible. Batches group draw calls with the same render state, so changing the material causes Unity to create a new batch.  
**Tris** | The number of [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html) Unity processes during a frame. This value is important when [optimizing for low-end hardware](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance.html).  
**Verts** | The number of [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) Unity processes during a frame. This value is important when [optimizing for low-end hardware](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance.html).  
**Screen** | The resolution of the screen, along with the amount of memory the screen uses.  
**SetPass** | The number of times Unity switches which **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) pass it uses to render GameObjects during a frame. A shader might contain several shader passes and each pass renders GameObjects differently. Each pass requires Unity to bind a new shader, which might introduce CPU overhead.  
**Shadow casters** | The number of GameObjects in the frame that cast shadows.  
**Visible skinned meshes** | The number of [Skinned Mesh Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html) in the frame.  
**Animation components playing** | The number of [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html) components playing during the frame.  
****Animator components** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent) playing** | The number of [Animator](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html) components playing during the frame.  
For more detailed information about your application’s rendering performance, see the [Rendering module of the Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerRendering.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html)
Frame Debugger Event Information reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
Audio
