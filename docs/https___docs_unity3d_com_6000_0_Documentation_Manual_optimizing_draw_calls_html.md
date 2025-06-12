* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * Introduction to optimizing draw calls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
Optimizing draw calls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
GPU instancing
# Introduction to optimizing draw calls
To draw geometry on the screen, Unity issues draw calls to the graphics API. A draw call tells the graphics API what to draw and how to draw it. Each draw call contains all the information the graphics API needs to draw on the screen, such as information about textures, **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), and buffers. Draw calls can be resource intensive, but often the preparation for a draw call is more resource intensive than the draw call itself. 
To prepare for a draw call, the CPU sets up resources and changes internal settings on the GPU. These settings are collectively called the render state. Changes to the render state, such as switching to a different material, are the most resource-intensive operations the graphics API performs.
Because render-state changes are resource intensive, it is important to optimize them. The main way to optimize render-state changes is to reduce the number of them. There are two ways to do this:
  * Reduce the total number of draw calls. When you decrease the number of draw calls, you also decrease the number of render-state changes between them.
  * Organize draw calls in a way that reduces the number of changes to the render state. If the graphics API can use the same render state to perform multiple draw calls, it can group draw calls together and not need to perform as many render-state changes.


Optimizing draw calls and render-state changes has a number of benefits for your application. Mainly, it improves frame times, but it also:
  * Reduces the amount of electricity your application requires. For battery-powered devices, this reduces the rate at which batteries run out. It also reduces the amount of heat a device produces when running your application.
  * Improves maintainability of future development on your application. When you optimize draw calls and render-state changes earlier and maintain them at an optimized level, you can add more **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) without producing large performance overheads.


## Optimization priority
You can use multiple draw call optimization methods in the same scene but be aware that Unity prioritizes draw call optimization methods in a particular order. If you mark a GameObject to use more than one draw call optimization method, Unity uses the highest priority method.
The only exception to this is the [SRP Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html) in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) or the High-Definition Render Pipeline (HDRP). When you use the SRP Batcher, Unity also supports **static batching** A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching) for [GameObjects that are SRP Batcher compatible](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher-Materials.html). Unity prioritizes draw call optimizations in the following order:
  1. SRP Batcher and static batching
  2. GPU instancing
  3. Dynamic batching


If you mark a GameObject for static batching and Unity successfully batches it, Unity disables GPU instancing for that GameObject, even if the renderer uses an instancing shader. When this happens, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window displays a warning message that suggests that you disable static batching. Similarly, if Unity can use GPU instancing for a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), Unity disables **dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) for that mesh.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
Optimizing draw calls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
GPU instancing
