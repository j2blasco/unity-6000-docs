* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects-use.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Set GameObjects to use Reflection Probes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects.html)
Add GameObjects to reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-EnableReflectionsOfReflections.html)
Enable reflections of reflections
# Set GameObjects to use Reflection Probes
To make use of the reflection **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap), an object must have the **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) option enabled on its [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) and also be using a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that supports reflection probes. When the object passes within the volume set by the probe’s **Size** and **Probe Origin** properties, the probe’s cubemap will be applied to the object.
You can also manually set which reflection probe to use for a particular object using the settings on the object’s [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html). To do this, select one of the options for the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer’s **Reflection Probes** property (**Simple** , **Blend Probes** or **Blend Probes and Skybox**) and drag the chosen probe onto its **Anchor Override** property.
See the [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html) section in the manual for further details about principles and usage.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects.html)
Add GameObjects to reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-EnableReflectionsOfReflections.html)
Enable reflections of reflections
