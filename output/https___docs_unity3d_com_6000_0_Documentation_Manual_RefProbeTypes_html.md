* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbeTypes.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Types of Reflection Probe


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)
Introduction to Reflection Probes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html)
Place a Reflection Probe
# Types of Reflection Probe
Reflection probes come in three basic types as chosen by the **Type** property in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) (see the [component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html) page for further details).
  * **Baked** probes store a reflection **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) generated (“baked”) within the editor. You can trigger the baking by clicking either the _Bake_ button at the bottom of the **Reflection Probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) inspector or the **Generate Lighting** button in the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html). The reflection from a baked probe can only show objects marked as **Reflection Probe Static** in the inspector. This indicates to Unity that the objects will not move at runtime.
  * **Realtime** probes create the cubemap at runtime in the player rather than the editor. This means that the reflections are not limited to static objects and can be updated in real time to show changes in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). However, it takes considerable processing time to refresh the view of a probe so it is wise to manage the updates carefully. Unity allows you to trigger updates from a script so you can control exactly when they happen. Also, there is an option to apply **timeslicing** to probe updates so that they can take place gradually over a few frames.
  * A **Custom** probe type is also available. These probes let you bake the view in the editor, as with Baked probes, but you can also supply a custom cubemap for the reflections. Custom probes cannot be updated at runtime.


The three types are explained in detail below.
## Baked Reflection Probes
A **Baked** Reflection Probe is one whose reflection cubemap is captured in the Unity editor and stored for subsequent usage in the player (see the [Reflection Probes Introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html) for further information). Once the capture process is complete, the reflections are “frozen” and so baked probes can’t react to runtime changes in the scene caused by moving objects. However, they come with a much lower processing overhead than Realtime Probes (which do react to changes) and are acceptable for many purposes. For example, if there is only a single moving reflective object then it need only reflect its static surroundings.
## Custom Reflection Probes
By default, Custom probes work the same way as Baked probes but they also have additional options that change this behaviour.
The **Dynamic Objects** property on a custom probe’s inspector allows objects that are not marked as **Reflection Probe Static** to be included in the reflection cubemap.
**Note** : The positions of these objects are still “frozen” in the reflection at the time of baking.
The **Cubemap** property allows you to assign your own cubemap to the probe and therefore make it completely independent of what it can “see” from its view point. You could use this, say, to set a **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) or a cubemap generated from your 3D modelling app as the source for reflections.
## Realtime Reflection Probes
Baked probes are useful for many purposes and have good runtime performance but they have the disadvantage of not updating live within the player. This means that objects can move around in the scene without their reflections moving along with them. In cases where this is too limiting, you can use **Realtime** probes, which update the reflection cubemap at runtime. This effect comes with a higher processing overhead but offers greater realism.
In the editor, real-time probes have much the same workflow as baked probes, although they tend to render more quickly.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)
Introduction to Reflection Probes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html)
Place a Reflection Probe
