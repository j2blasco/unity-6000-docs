* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * [Batching static GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html)
  * Enable static batching


[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)
Introduction to static batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
Batching moving GameObjects
# Enable static batching
Unity can perform **static batching** A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching) at build time and at runtime. As a general rule, if the **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) exist in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) before you build your application, use the [Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html#editor) to batch your GameObjects at build time. If you create the GameObjects and their meshes at runtime, use the [runtime API](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html#runtime). 
When you use the runtime API, you can change the transform properties of the root of a static batch. This means that you can move, rotate, or scale the entire combination of meshes that make up a static batch. You can’t change the transform properties of the individual meshes. 
To use static batching for a set of GameObjects, the GameObjects must be eligible for static batching. In addition to the criteria described in the [common usage information](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html), make sure that:
  * The GameObject is active.
  * The GameObject has a [Mesh Filter](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshFilter) component, and that component is enabled.
  * The Mesh Filter component has a reference to a [Mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh).
  * The mesh has a vertex count greater than 0.
  * The mesh has not already been combined with another Mesh.
  * The GameObject has a [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component, and that component is enabled.
  * The Mesh Renderer component does not use any Material with a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that has the `DisableBatching` tag set to true.
  * Meshes you want to batch together use the same vertex attributes. For example Unity can batch meshes that use vertex position, vertex normal, and one UV with one another, but not with meshes that use vertex position, vertex normal, UV0, UV1, and vertex tangent.


**Note** : To use runtime static batching you must also set the mesh to have read/write enabled.
For information about the performance implications for static batching, see [Performance implications](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html#performance-implications).
## Static batching at build time
You can enable static batching at build time in the Editor.
To perform static batching at build time:
  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , enable **Static Batching**.
  3. In the Scene view or Hierarchy, select the GameObject that you want to batch and view it in the Inspector.  
**Tip** : You can select multiple GameObjects at the same time to enable static batching for all of them.
  4. In the GameObject’s [Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html), enable **Batching Static**.


Unity automatically batches the specified static meshes into the same draw call if they fulfill the criteria described in the [common usage information](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html).
![The Static Editor Flags checkbox in the Inspector for a GameObject.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StaticTagInspector.png) The Static Editor Flags checkbox in the Inspector for a GameObject.
**Note** : If you perform static batching at build time, Unity doesn’t use any CPU resources at runtime to generate the mesh data for the static batch.
## Static batching at runtime
To batch static meshes at runtime, Unity provides the [StaticBatchingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.html) class. The static [StaticBatchingUtility.Combine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.Combine.html) method combines the GameObjects you pass in and prepares them for static batching. This is especially useful for meshes that you procedurally generate at runtime. 
Unlike static batching at build time, batching at runtime doesn’t require you to enable the **Static Batching** Player Setting. For information on how to use this API, see [StaticBatchingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)
Introduction to static batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
Batching moving GameObjects
