* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * Reflections


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)
Troubleshooting shadows
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)
Introduction to Reflection Probes
# Reflections
Techniques and resources for using Reflection Probes to capture and display reflections on **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
**Page** | **Description**  
---|---  
[Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) | Understand how Unity bakes a spherical view of a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) into a Reflection Probe, then uses it to quickly calculate reflections on GameObjects.  
[Types of Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbeTypes.html) | Compare the differences between Baked, Custom, and Realtime Reflection Probes.  
[Place a Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html) | Add, position and resize a Reflection Probe in a scene.  
[Add GameObjects to reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects.html) | Set GameObjects to contribute to Baked and Realtime Reflection Probes, and update Reflection Probes when GameObjects move.  
[Set GameObjects to use Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects-use.html) | Set GameObjects to sample the **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) texture stored in a Reflection Probe.  
[Enable reflections of reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-EnableReflectionsOfReflections.html) | Enable interreflections, for example for two mirrors placed close together and facing each other.  
[Optimize reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbePerformance.html) | Speed up baking time and rendering time for Reflection Probes.  
[Troubleshooting reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/AdvancedRefProbe.html) | Solve common issues with reflections, for example incorrect reflection size in indoor scenes.  
[Reflection Probe Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html) | Explore the properties and settings in the Render Probe **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to customize Reflection Probes.  
## Additional resources
  * [Reflections in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/reflection-probes.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Lighting data](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmap-data-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)
Troubleshooting shadows
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)
Introduction to Reflection Probes
