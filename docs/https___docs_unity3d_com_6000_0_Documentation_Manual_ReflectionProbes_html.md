* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Introduction to Reflection Probes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
Reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbeTypes.html)
Types of Reflection Probe
# Introduction to Reflection Probes
A **Reflection Probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) is rather like a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) that captures a spherical view of its surroundings in all directions. The captured image is then stored as a [Cubemap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) that can be used by objects with reflective materials. Several reflection probes can be used in a given **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and objects can be set to use the cubemap produced by the nearest probe. The result is that the reflections on the object can change convincingly according to its environment.
![A Reflection Probe showing reflections from a nearby object](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ReflectionProbeScene.jpg) A Reflection Probe showing reflections from a nearby object
CG films and animations commonly feature highly realistic reflections, which are important for giving a sense of “connectedness” among the objects in the scene. However, the accuracy of these reflections comes with a high cost in processor time and while this is not a problem for films, it severely limits the use of reflective objects in real-time games.
Traditionally, games have used a technique called _reflection mapping_ to simulate reflections from objects while keeping the processing overhead to an acceptable level. This technique assumes that all reflective objects in the scene can “see” (and therefore reflect) the exact same surroundings. This works quite well for the game’s main character (a shiny car, say) if it is in open space but is unconvincing when the character passes into different surroundings; it looks strange if a car drives into a tunnel but the sky is still visibly reflected in its windows.
Unity improves on basic reflection mapping through the use of **Reflection Probes** , which allow the visual environment to be sampled at strategic points in the scene. You should generally place them at every point where the appearance of a reflective object would change noticeably (eg, tunnels, areas near buildings and places where the ground colour changes). When a reflective object passes near to a probe, the reflection sampled by the probe can be used for the object’s reflection map. Furthermore, when several probes are nearby, Unity can interpolate between them to allow for gradual changes in reflections. Thus, the use of reflection probes can create quite convincing reflections with an acceptable processing overhead.
## How Reflection Probes Work
The visual environment for a point in the scene can be represented by a [cubemap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html). This is conceptually like a box with flat images of the view from six directions (up, down, left, right, forward and backward) painted on its interior surfaces.
![Inside surfaces of a skybox cubemap \(front face removed\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CubemapDiagram.svg) Inside surfaces of a skybox cubemap (front face removed)
For an object to show the reflections, its **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) must have access to the images representing the cubemap. Each point of the object’s surface can “see” a small area of cubemap in the direction the surface faces (ie, the direction of the surface normal vector). The shader uses the colour of the cubemap at this point in calculating what colour the object’s surface should be; a mirror material might reflect the colour exactly while a shiny car might fade and tint it somewhat.
As mentioned above, traditional reflection mapping makes use of only a single cubemap to represent the surroundings for the whole scene. The cubemap can be painted by an artist or it can be obtained by taking six “snapshots” from a point in the scene, with one shot for each cube face. Reflection probes improve on this by allowing you to set up many predefined points in the scene where cubemap snapshots can be taken. You can therefore record the surrounding view at any point in the scene where the reflections differ noticeably.
In addition to its view point, a probe also has a zone of effect defined by an invisible box shape in the scene. A reflective object that passes within a probe’s zone has its reflection cubemap supplied temporarily by that probe. As the object moves from one zone to another, the cubemap changes accordingly.
## Default Reflection Probes
When you add a new scene, Unity automatically creates a hidden default Reflection Probe that stores Unity’s built-in Default **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) cubemap.
The data in the hidden Reflection Probe is fixed. For example, if you change the **Skybox Material** in the Lighting window, the data in the probes doesn’t change, so environment lighting on objects stays the same.
To stop using the hidden Reflection Probe, select **Generate Lighting** or **Clear Baked Data** in the Lighting window. Unity then creates and uses a new default baked Reflection Probe (the ambient Reflection Probe). This Reflection Probe is an asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), and updates when you select **Generate Lighting**.
## Additional resources
  * [Reflections in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/reflection-probes.html)
  * [Lighting data](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmap-data-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
Reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbeTypes.html)
Types of Reflection Probe
