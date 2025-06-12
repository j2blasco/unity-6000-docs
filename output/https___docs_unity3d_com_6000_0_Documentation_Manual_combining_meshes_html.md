* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/combining-meshes.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * Combine meshes manually


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-enable.html)
Enable dynamic batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
Profile rendering
# Combine meshes manually
You can manually combine multiple meshes into a single **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) as a [draw call optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html) technique. Unity renders the combined mesh in a single draw call instead of one draw call per mesh. This technique can be a good alternative to [draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) in cases where the meshes are close together and don’t move relative to one another. For example, for a static cupboard with lots of drawers, it makes sense to combine everything into a single mesh.
**Warning** : Unity can’t individually cull meshes you combine. This means that if one part of a combined mesh is onscreen, Unity draws the entire combined mesh. If the meshes are static and you want Unity to individually cull them, use [static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching) instead.
There are two main ways to combine meshes:
  * In your asset generation tool while authoring the mesh.
  * In Unity using [Mesh.CombineMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.CombineMeshes.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-enable.html)
Enable dynamic batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
Profile rendering
