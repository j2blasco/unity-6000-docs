* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * [Performance consideration for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
  * Optimize performance of moving elements at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
Performance consideration for runtime UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
Control textures of the dynamic atlas
# Optimize performance of moving elements at runtime
When you move a large amount of elements at runtime, performance optimization is crucial, especially for applications requiring smooth and responsive interactions.
Certain CSS properties, such as top, left, width, height, or flex, can trigger layout recalculations when updated. These recalculations dirty the layout and might cascade updates across multiple elements, significantly impacting rendering performance. Use these properties sparingly and only when absolutely necessary.
## Best practices for moving elements
The most performance-efficient way to move elements is to use the [`style.translate`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html) property. This property adjusts an element’s position dynamically without recalculating the layout. Unlike other positioning methods, `style.translate` operates at the transform stage. It minimizes the computational overhead and improves rendering performance by reducing dependency on CPU-intensive processes.
## Use usage hints to reduce draw calls and geometry regeneration
To further enhance performance, leverage usage hints to optimize how elements are processed during runtime. Usage hints help:
  * Reduce draw calls.
  * Avoid unnecessary geometry regeneration.


If the transform of the element, such as position, rotation, or scale, changes frequently, set usage hint to `DynamicTransform`. This pushes transform updates directly to the GPU, bypassing CPU **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) updates and improving performance. 
You can set the usage hints in UI Builder, UXML, or C#. The following examples set the usage hints to `DynamicTransform`:
**UXML** :
```
<ui:VisualElement usage-hints="DynamicTransform" />

```

**C#** :
```
visualElement.usageHints = UsageHints.DynamicTransform;

```

The supported usage hints are:
  * [`DynamicTransform`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.DynamicTransform.html)
  * [`GroupTransform`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.GroupTransform.html)
  * [`MaskContainer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.MaskContainer.html)
  * [`DynamicColor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.DynamicColor.html)


## Flow of updating and rendering a visual element
The following diagram illustrates the flow of updating and rendering a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) at runtime:
![Flow of updating and rendering a visual element](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/flow-of-rendering-elements.png) Flow of updating and rendering a visual element
For an example that optimizes rendering and updates for frequently changing elements at runtime, refer to [Move elements at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-move-elements-at-runtime.html).
## Additional resources
  * [`usageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html)
  * [`VisualElement.usageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-usageHints.html)
  * [Move elements at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-move-elements-at-runtime.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
Performance consideration for runtime UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
Control textures of the dynamic atlas
