* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)
  * Reflection Probe Inspector window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AdvancedRefProbe.html)
Troubleshooting reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
Lighting in URP
# Reflection Probe Inspector window reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html "Go to ReflectionProbe page in the Scripting Reference") **Property** | **Description**  
---|---  
**Type** | Choose whether the probe is for a **Baked** , **Custom** , or **Realtime** setup. If you select **Baked** , the **Reflection Probe** does not capture **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) at runtime that have their Reflection Probe Static flag disabled. If you want to capture dynamic GameObjects in a baked Reflection Probe, select **Custom** and enable **Dynamic Objects**.  
**Dynamic Objects** | (**Custom** type only) Forces objects not marked as **Static** to be baked in to the reflection.  
**Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) | (**Custom** type only) Sets a custom [cubemap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html) for the probe.  
**Refresh Mode** | (**Realtime** type only) Selects if and how the probe will refresh at runtime. The _On Awake_ option renders the probe only once when it first becomes active. _Every Frame_ renders the probe every frame update, optionally using **Time Slicing** (see below). The **Via Scripting** option refreshes the probe from a user script command rather than an automatic update.  
**Time Slicing** | (**Realtime** type only) How should the probe distribute its updates over time? The options are **All Faces At Once** (spreads update over nine frames), **Individual Faces** (updates over fourteen frames) and **No Time Slicing** (the update happens entirely within one frame). See below for further details.  
## Runtime Settings
**Property** | **Description**  
---|---  
**Importance** | A value that indicates the relative priority of this Reflection Probe for sorting. Unity renders probes with a higher value on top of those with a lower value where an object is in range of more than one probe. This setting also affects **Blending**. Refer to [Using Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html) for more information about reflection probe blending.  
**Intensity** | The intensity modifier that is applied to the texture of this probe in its **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).  
**Box Projection** | Check this box to enable projection for reflection UV mappings. If you use the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), you must also enable **Box Projection** in the [URP asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).  
**Box Size** | The size of the probe’s bounding box in which the probe can contribute to reflections. The size is in world space. Also used by **Box Projection**.  
**Box Offset** | The center of the probe’s bounding box in which the probe can contribute to reflections. The offset is relative to the position of the probe. Also used by **Box Projection**.  
## Cubemap Capture Settings
**Property** | **Description**  
---|---  
**Resolution** | The resolution of the captured reflection image.  
**HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) | Should High Dynamic Range rendering be enabled for the cubemap? This also determines whether probe data is saved in [OpenEXR](http://www.openexr.com/) or PNG format.  
**Shadow Distance** | Distance at which shadows are drawn when rendering the probe.  
**Clear Flags** | Option to specify how empty background areas of the cubemap will be filled. The options are **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) and **Solid Color**.  
**Background** | Background colour to which the reflection cubemap is cleared before rendering.  
**Culling Mask** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask) | Allows objects on specified layers to be included or excluded in the reflection. See the section about the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s culling mask on the [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer) page.  
**Use Occlusion Culling** | Should **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling) be used when baking the probe?  
**Clipping Planes** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane) | Near and **far clipping planes** The maximum draw distance for a camera. Geometry beyond the plane defined by this value is not rendered. The plane is perpendicular to the camera’s forward (Z) direction.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Farclippingplane) of the probe’s “camera”.  
## Additional resources
  * [Reflections in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/reflection-probes.html)
  * [Reflection and refraction in the High-Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Reflection-in-HDRP.html)


ReflectionProbe
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AdvancedRefProbe.html)
Troubleshooting reflections
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
Lighting in URP
