* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * Light component Inspector window reference for the Built-In-Render-Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/blend-reflection-probes-birp.html)
Blend Reflection Probes in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-optimize-builtin.html)
Optimize lighting in the Built-In Render Pipeline
# Light component Inspector window reference for the Built-In-Render-Pipeline
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html "Go to Light page in the Scripting Reference")
Unity displays different properties in the Light **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) depending on the [render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) that your Project uses.
## Light settings
Property: | Function:  
---|---  
**Type** | The current type of light. Possible values are **Directional** , **Point** , **Spot** and **Area** (Rectangle or Disc light). For information on these values, see [Types of Light](https://docs.unity3d.com/6000.0/Documentation/Manual/Lighting.html).  
**Range** | Define how far the light emitted from the center of the object travels (**Point** and **Spot** lights only).  
**Spot Angle** | Define the angle (in degrees) at the base of a spot light’s cone (**Spot** light only).  
**Color** | Use the color picker to set the color of the emitted light.  
**Mode** | Specify the [Light Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html). Possible modes are **Realtime** , **Mixed** and **Baked**. For information on these values, see [Light Modes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightMode).  
**Intensity** | Set the brightness of the light. The default value for a **Directional** light is 0.5. The default value for a **Point** , **Spot** or **Area** (Rectangle or Disc)light is 1.  
**Indirect Multiplier** | Use this value to vary the intensity of indirect light. If you set **Indirect Multiplier** to a value lower than **1,** the bounced light becomes dimmer with every bounce. A value higher than **1** makes light brighter with each bounce. This is useful, for example, when a dark surface in shadow (such as the interior of a cave) needs to be brighter to make detail visible. If you want to use [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html), but want to limit a single real-time Light so that it only emits direct light, set its **Indirect Multiplier** to **0**.  
## Shadows
Property: | Function:  
---|---  
**Shadow Type** | Determine whether this Light casts Hard Shadows, Soft Shadows, or no shadows at all. **Hard Shadows** produces shadows with a sharp edge. Hard shadows aren’t realistic compared to **Soft Shadows** but they involve less processing, and are acceptable for many purposes. Soft shadows also tend to reduce the “blocky” aliasing effect from the shadow map.  
Baked Shadow Angle | If **Mode** is set to **Baked** or **Mixed** , **Type** is set to **Directional** , and **Shadow Type** is set to **Soft Shadows** , this property adds some artificial softening to the edges of shadows and gives them a more natural look.  
Baked Shadow Radius | If **Mode** is set to **Baked** or **Mixed** , **Type** is set to **Point** or **Spot** ,and **Shadow Type** is set to **Soft Shadows** , this property adds some artificial softening to the edges of shadows and gives them a more natural look.  
Realtime Shadows | These properties are available when **Mode** is set to **Realtime** or **Mixed** , and **Shadow Type** is set to **Hard Shadows** or **Soft Shadows**. Use these properties to control real-time shadow rendering settings.  
Strength | Use the slider to control how dark the shadows cast by this Light are, represented by a value between 0 and 1. This is set to 1 by default.  
Resolution | Control the rendered resolution of shadow maps. A higher resolution increases the fidelity of shadows, but requires more GPU time and memory usage.  
Bias | Use the slider to control the distance at which shadows are pushed away from the light, defined as a value between 0 and 2. This is useful for avoiding false self-shadowing artifacts. See [Shadow troubleshooting](https://docs.unity3d.com/Manual/ShadowPerformance.html) for more information. This is set to 0.05 by default.  
Normal Bias | Use the slider to control distance at which the shadow casting surfaces are shrunk along the surface normal, defined as a value between 0 and 3. This is useful for avoiding false self-shadowing artifacts. See documentation on Shadow mapping and the bias property for more information. This is set to 0.4 by default.  
  
Near Plane | Use the slider to control the value for the near clip plane when rendering shadows, defined as a value between 0.1 and 10. This value is clamped to 0.1 units or 1% of the light’s **Range** property, whichever is lower. This is set to 0.2 by default.  
## Additional settings
Property: | Function:  
---|---  
**Cookie** | Specify a Texture mask through which shadows are cast (for example, to create silhouettes, or patterned illumination for the Light). For more information, see [Cookies](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html).  
**Draw Halo** | Tick this box to draw a spherical [Halo](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html)The glowing light areas around light sources, used to give the impression of small dust particles in the air. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Halo) of light with a diameter equal to the **Range** value. You can also use the Halo component to achieve this. Note that the Halo component is drawn in addition to the halo from the Light component, and that the Halo component’s **Size** parameter determines its radius, not its diameter.  
**Flare** | If you want to set a [Flare](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html) to be rendered at the Light’s position, place an Asset in this field to be used as its source.  
**Render Mode** | Use this drop-down to set the rendering priority of the selected Light. This can affect lighting fidelity and performance.  
Auto | The rendering method is determined at run time, depending on the brightness of nearby lights and the current [Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) settings.  
Important | The light is always rendered at per-pixel quality. Use **Important** mode only for the most noticeable visual effects (for example, the headlights of a player’s car).  
Not Important | The light is always rendered in a faster, vertex/object light mode.  
****Culling Mask** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask)** | Use this to selectively exclude groups of objects from being affected by the Light. For more information, see [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer).  
## Additional resources
  * [Light component Inspector window reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/light-component.html)
  * [Lights in the High-Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Light-Component.html)


Light
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/blend-reflection-probes-birp.html)
Blend Reflection Probes in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-optimize-builtin.html)
Optimize lighting in the Built-In Render Pipeline
