* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-troubleshooting.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-landing.html)
  * Troubleshooting Light Probes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Moving.html)
Move Light Probes at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Reference.html)
Light Probes reference
# Troubleshooting Light Probes
## Ringing
Under certain circumstances, Light Probes exhibit an unwanted behaviour called “ringing”. This often happens when there are significant differences in the light surrounding a **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe). For example, if you have bright light on one side of a Light Probe, and no light on the other side, the light intensity can “overshoot” on the back side. This overshoot causes a light spot on the back side.
![An example of Light Probe ringing. A Point Light illuminates a sphere from one side, but the back side of the sphere appears partially lit too.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-LightProbeGroup-Ringing.png) An example of Light Probe ringing. A Point Light illuminates a sphere from one side, but the back side of the sphere appears partially lit too.
There are several ways to deal with this:
  * In the **Light Probe Group** A component that enables you to add Light Probes to GameObjects in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeGroup) component, enable **Remove Ringing**. Unity automatically removes the unintended light spots. However, this generally makes the Light Probes less accurate, and reduces light contrast, so you must check the visual results.
  * Place in-game obstacles in such a way that players can’t get to a position where they can see the light spot.
  * Avoid baking direct light into Light Probes. Direct light tends to have sharp discontinuities (such as shadow edges), which makes it unsuitable for Light Probes. To only bake indirect light, use [Mixed lighting](https://docs.unity3d.com/Manual/LightMode-Mixed.html).


## Troubleshooting Light Probe placement
Your choice of Light Probe positions must take into account that the lighting is interpolated between sets of Light Probes. Problems can arise if your Light Probes don’t adequately cover the changes in lighting across your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
The example below shows a night-time Scene with two bright street lamps on either side, and a dark area in the middle. If Light Probes are only placed near the street lamps, and none in the dark area, the lighting from the lamps “bleeds” across the dark gap, on moving objects. This is because the lighting is being interpolated from one bright point to another, with no information about the dark area in-between.
![An example of poor Light Probe placement. A street scene has a street lamp at either end, and a set of four Light Probes next to each lamp. There are no Light Probes in the dark area between the two lamps, so the dark area isnt included in the interpolation.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-LightProbeGroup-12.png) An example of poor Light Probe placement. A street scene has a street lamp at either end, and a set of four Light Probes next to each lamp. There are no Light Probes in the dark area between the two lamps, so the dark area isn’t included in the interpolation.
If you are using Realtime or Mixed lights, this problem may be less noticeable, because only the _indirect_ light bleeds across the gap. The problem is more noticable if you are using fully **baked lights** Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#baked)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BakedLights), because in this situation the direct light on moving objects is also interpolated from the Light Probes. In this example Scene, the two lamps are baked, so moving objects get their direct light from Light Probes. Here you can see the result.
![In the same scene, a moving ambulance remains brightly lit while passing through the dark area. A yellow wireframe tetrahedron shows that the interpolation occurs between one brightly lit end of the street to the other.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-LightProbeGroup-13.png) In the same scene, a moving ambulance remains brightly lit while passing through the dark area. A yellow wireframe tetrahedron shows that the interpolation occurs between one brightly lit end of the street to the other.
This is an undesired effect - the ambulance remains brightly lit while passing through a dark area, because no Light Probes were placed in the dark area.
To solve this, you should place more Light Probes in the dark area, as shown below:
![The same scene, with another set of Light Probes added halfway between the two street lamps.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-LightProbeGroup-14.png) The same scene, with another set of Light Probes added halfway between the two street lamps.
Now the Scene has Light Probes in the dark area too. As a result, the moving ambulance takes on the darker lighting as it travels from one side of the Scene to the other.
![The same scene, now with the moving ambulance, which takes on the darker lighting in the center of the scene.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-LightProbeGroup-15.png) The same scene, now with the moving ambulance, which takes on the darker lighting in the center of the scene.
* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Moving.html)
Move Light Probes at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Reference.html)
Light Probes reference
