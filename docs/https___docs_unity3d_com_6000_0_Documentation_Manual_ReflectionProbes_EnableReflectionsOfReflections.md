* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-EnableReflectionsOfReflections.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Enable reflections of reflections


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects-use.html)
Set GameObjects to use Reflection Probes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbePerformance.html)
Optimize reflections
# Enable reflections of reflections
You may have seen a situation where two mirrors are placed fairly close together and facing each other. Both mirrors reflect not only the mirror opposite but also the reflections produced by that mirror. The result is an endless progression of reflections between the two; reflection between objects like this are known as **Interreflections**.
Reflection probes create the **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) by taking a snapshot of the view from their position. However, with a single snapshot, the view cannot show interreflections and so additional snapshots must be taken for each stage in the interreflection sequence.
The number of times that a reflection can “bounce” back and forth between two objects is controlled in the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html); go to **Environment** > **Environment Reflections** and edit the **Bounces** property. This is set globally for all probes, rather than individually for each probe. With a reflection bounce count of 1, reflective objects viewed by a probe are shown as black. With a count of 2, the first level of interreflection are visible, with a count of 3, the first two levels will be visible, and so on. 
Note that the reflection bounce count also equals the number of times the probe must be baked with a corresponding increase in the time required to complete the full bake. You should therefore set the count higher than one only when you know that reflective objects will be clearly visible in one or more probes.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes-set-gameobjects-use.html)
Set GameObjects to use Reflection Probes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RefProbePerformance.html)
Optimize reflections
