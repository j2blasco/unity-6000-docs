* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * Performance consideration for runtime UI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html)
FAQ for input and event systems with UI Toolkit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
Optimize performance of moving elements at runtime
# Performance consideration for runtime UI
This section describes how you can improve the performance for runtime UI.
**Topic** | **Description**  
---|---  
[Use usage hints to reduce draw calls and geometry regeneration](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html) | Use usage hints to set how an element is used at runtime. Usage hints can reduce draw calls and avoid geometry regeneration.  
[Control textures of the dynamic atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-control-textures-of-the-dynamic-atlas.html) | Use an atlas to reduce the number of batches broken by texture changes and achieve good performance.  
[Platform and mesh consideration](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-platform-and-mesh.html) | Consider device capabilities and avoid **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) tessellation.  
## Additional resources
  * [Panel Settings asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
  * [`usageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-usageHints.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-faq-event-and-input-system.html)
FAQ for input and event systems with UI Toolkit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
Optimize performance of moving elements at runtime
