* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AdvancedRefProbe.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Troubleshooting reflections


[](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbePerformance.html)
Optimize reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)
Reflection Probe Inspector window reference
# Troubleshooting reflections
## Box projection
Normally, the reflection **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) is assumed to be at an infinite distance from any given object. Different angles of the cubemap will be visible as the object turns but it is not possible for the object to move closer or farther away from the reflected surroundings. This often works very well for outdoor scenes but its limitations show in an indoor **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene); the interior walls of a room are clearly not an infinite distance away and the reflection of a wall should get larger the closer the object gets to it.
The **Box Projection** option allows you to create a reflection cubemap at a finite distance from the probe, thus allowing objects to show different-sized reflections according to their distance from the cubemap’s walls. The size of the surrounding cubemap is determined by the probes zone of effect, as determined by its **Box Size** property. For example, with a probe that reflects the interior of a room, you should set the size to match the dimensions of the room. 
In the Built in Render Pipeline, you can enable global **Box Projection** for a given [Graphics tier](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html) in [**Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. ](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Tier)[More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) > **Graphics** > **Tier Settings**. You can disable this setting for individual Reflection Probes in the Reflection Probe inspector if you want to create infinite projection.
![The parallax issue is fixed by using Box Projection option](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GraphicsSettings_BoxProjection.jpg) The parallax issue is fixed by using Box Projection option
## Additional resources
  * [Troubleshooting reflections in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/reflection-probes-troubleshooting.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbePerformance.html)
Optimize reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)
Reflection Probe Inspector window reference
