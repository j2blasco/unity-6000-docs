* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-platform-and-mesh.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * [Performance consideration for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
  * Platform and mesh considerations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
Control textures of the dynamic atlas
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-examples.html)
UI Toolkit runtime examples
# Platform and mesh considerations
Things to consider when building UI for different platforms and **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) tessellation.
## Consider device capabilities
Some Android devices and the Web platform can’t partially patch index buffers. If your audience uses such devices or if you target the Web platform, UI Toolkit rendering is still functional but performance may be degraded. To avoid performance degradation, don’t animate too many elements at the same time and [profile on device](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html).
## Avoid mesh tessellation
It’s computationally expensive to build mesh tessellation for **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). Any time the size (width/height) of the element changes, its geometry re-builds, which can be an issue with animations or frequent resizing.
Generally speaking, [transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html) and texture aren’t good choices in terms of flexibility and re-use. However, when you animate, to get better performance, do the following:
  * Use [transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html) instead of width or other layout properties
  * Use textures or 2D **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) instead of rounded corners and borders


## Additional resources
  * [`Transform`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)
  * [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
Control textures of the dynamic atlas
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-examples.html)
UI Toolkit runtime examples
