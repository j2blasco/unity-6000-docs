* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Shader Material Inspector window reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
  * Lit Shader Material Inspector window reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/blending-modes.html)
Blending Modes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/simple-lit-shader.html)
Simple Lit Shader Material Inspector window reference for URP
# Lit Shader Material Inspector window reference for URP
The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window for this **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) contains these elements:
  * **[Surface Options](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html#surface-options)**
  * **[Surface Inputs](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html#surface-inputs)**
  * **[Advanced](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html#advanced)**


## Surface Options
The **Surface Options** control how URP renders the Material on a screen.
**Property** | **Description**  
---|---  
**Workflow Mode** | Use this drop-down menu to choose a workflow that fits your Textures, either [**Metallic**](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterMetallic.html) and [**Specular**](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterSpecular.html).  
When you have made your choice, the main Texture options in the rest of the Inspector now follow your chosen workflow. For information on metallic or specular workflows, refer to the [Manual page for the Standard built-in Shader in Unity](https://docs.unity3d.com/Manual/StandardShaderMetallicVsSpecular.html).  
  
**Note** : This option affects batching performance.  
**Surface Type** | Use this drop-down to apply an **Opaque** or **Transparent** surface type to the material. This determines which render pass URP renders the material in. **Opaque** surface types are always fully visible, regardless of what’s behind them. URP renders opaque materials first. **Transparent** surface types are affected by their background, and they can vary according to which type of transparent surface type you choose. URP renders transparent materials in a separate pass after opaque objects. If you select **Transparent** , the **Blending Mode** drop-down appears.  
  
**Note** : This option affects batching performance.  
**Blending Mode** | Select how Unity calculates the color of each pixel of a transparent material when it blends the material with the background. The options are the following: 
  * Alpha
  * Premultiply
  * Additive
  * Multiply

For more information, refer to [Blending Modes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/blending-modes.html).  
  
**Note** : This option affects batching performance.  
**Preserve Specular Lighting** | Indicates whether Unity preserves specular highlights on a GameObject or not. This applies even when your surface is transparent which means that only the reflected light is visible.  
  
This property only appears when the **Surface Type** is set to Transparent and **Blending Mode** is set to either Alpha or Additive.  
**Render Face** | Use this drop-down to determine which sides of your geometry to render.  
**Front Face** renders the front face of your geometry and [culls](https://docs.unity3d.com/Manual/SL-CullAndDepth.html) the back face. This is the default setting.   
**Back Face** renders the back face of your geometry and culls the front face.   
**Both** makes URP render both faces of the geometry. This is good for small, flat objects, like leaves, where you might want both sides visible.  
**Alpha Clipping** | Makes your material act like a [Cutout](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterRenderingMode.html) Shader. Use this to create a transparent effect with hard edges between the opaque and transparent areas. For example, to create blades of grass. To achieve this effect, URP doesn’t render alpha values below the specified **Threshold** , which appears when you enable **Alpha Clipping**. You can set the **Threshold** by moving the slider, which accepts values from 0 to 1. All values above your threshold are fully opaque, and all values below your threshold are invisible. For example, a threshold of 0.1 means that URP doesn’t render alpha values below 0.1. The default value is 0.5.  
  
**Note** : This option affects batching performance.  
**Receive Shadows** | Tick this box to enable your GameObject to have shadows cast upon it by other objects. If you disable this option, the GameObject will not have shadows on it.  
  
**Note** : This option affects batching performance.  
## Surface Inputs
The **Surface Inputs** describe the surface itself. For example, you can use these properties to make your surface look wet, dry, rough, or smooth.
**Note** : If you’re used to the [Standard Shader](https://docs.unity3d.com/Manual/Shader-StandardShader.html) in the built-in Unity **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), these options are similar to the Main Maps settings in the [Material Editor](https://docs.unity3d.com/Manual/StandardShaderContextAndContent.html).
**Property** | **Description**  
---|---  
**Base Map** | Adds color to the surface, also known as the diffuse map. To assign a Texture to the **Base Map** setting, click the object picker next to it. This opens the Asset Browser, where you can select from the Textures in your Project. Alternatively, you can use the [color picker](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InspectorColorPicker.html). The color next to the setting shows the tint on top of your assigned Texture. To assign another tint, you can click this color swatch. If you select **Transparent** or **Alpha Clipping** under **Surface Options** , your material uses the Texture’s alpha channel or color.  
**Metallic / Specular Map** | Shows a map input for your chosen **Workflow Mode** in the **Surface Options**.  
For the [**Metallic Map**](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterMetallic.html) workflow, the map gets the color from the **Base Map** assigned above. Use the slider to control how metallic the surface appears. 1 is fully metallic, like silver or copper, and 0 is fully dielectric, like plastic or wood. You can generally use values between 0 and 1 for dirty or corroded metals.  
For the [**Specular Map**](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterSpecular.html) setting, you can assign a texture to it by clicking the object picker next to it. This opens the Asset Browser, where you can select from the Textures in your Project. Alternatively, you can use the [color picker](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InspectorColorPicker.html).  
For both workflows, you can use the **Smoothness** slider to control the spread of highlights on the surface. 0 gives a wide, rough highlight. 1 gives a small, sharp highlight like glass. Values between produce semi-glossy looks. For example, 0.5 produces a plastic-like glossiness.  
Use the **Source** drop-down menu to select where the shader samples a smoothness map from. Options are: **Metallic Alpha** (alpha channel from the metallic map), and **Albedo Alpha** (alpha channel from the base map). The default value is **Metallic Alpha**.  
If the selected source has the alpha channel, the shader samples the channel and multiplies each sample by the **Smoothness** value.  
  
**Note** : This option affects batching performance.  
**Normal Map** | Adds a normal map to the surface. With a [normal map](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterNormalMap.html), you can add surface details like bumps, scratches and grooves. To add the map, click the object picker next to it. The normal map picks up ambient lighting in the environment.   
The float value next to the setting is a multiplier for the effect of the **Normal Map**. Low values decrease the effect of the normal map. High values create stronger effects.  
  
**Note** : This option affects batching performance.  
**Height Map** | URP implements the parallax mapping technique which uses the [height map](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterHeightMap.html) to achieve surface-level occlusion effect by shifting the areas of the visible surface texture. To add the map, click the object picker next to it.   
The float value next to the setting is a multiplier for the effect of the **Height Map**. Low values decrease the effect of the height map. High values create stronger effects.  
  
**Note** : This option affects batching performance.  
**Occlusion Map** | Select an [occlusion map](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterOcclusionMap.html). This simulates shadows from ambient light and reflection, which makes lighting look more realistic as less light reaches corners and crevices of objects. To select the occlusion map, click the object picker next to it.  
  
**Note** : This option affects batching performance.  
**Emission** | Makes the surface look like it emits lights. When enabled, the **Emission Map** and **Emission Color** settings appear.  
To assign an **Emission Map** , click the object picture next to it. This opens the Asset Browser, where you can select from the textures in your Project.  
For **Emission Color** , you can use the [color picker](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InspectorColorPicker.html) to assign a tint on top of the color. This can be more than 100% white, which is useful for effects like lava, that shines brighter than white while still being another color.  
If you haven’t assigned an **Emission Map** , the **Emission** setting only uses the tint you’ve assigned in **Emission Color**.  
If you don’t enable **Emission** , URP sets the emission to black and doesn’t calculate emission.  
  
**Note** : This option affects batching performance.  
**Tiling** | A 2D multiplier value that scales the Texture to fit across a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) according to the U and V axes. This is good for surfaces like floors and walls. The default value is 1, which means no scaling. Set a higher value to make the Texture repeat across your mesh. Set a lower value to stretch the Texture. Try different values until you reach your desired effect.  
**Offset** | The 2D offset that positions the Texture on the mesh. To adjust the position on your mesh, move the Texture across the U or V axes.  
## Detail Inputs
Use the **Detail Inputs** settings to add extra details to the surface.
**Requirement** : GPU supporting shader model 2.5 or higher.
**Property** | **Description**  
---|---  
**Mask** | Select a texture that defines areas where Unity overlays the Detail maps over the Surface Inputs maps. The mask uses the alpha channel of the selected texture. The **Tiling** and **Offset** settings have no effect on the mask.  
**Base Map** | Select the texture containing the surface details. Unity blends this map with the Surface Base Map using the overlay mode.  
**Normal Map** | Select the texture containing the normal vector data. Use a [normal map](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterNormalMap.html) to add surface details like bumps, scratches and grooves.  
Use the slider next to the setting to change the intensity of the effect of the map. The default value is 1.  
**Tiling** | Use this setting to scale the **Base Map** and the **Normal Map** on the mesh along the U and V axes, so that the maps fit the mesh best. The default value is 1. Select a value higher than one to make the maps repeat themselves across the mesh. Set a value lower than 1 to stretch the maps.  
**Offset** | The offset that moves the **Base Map** and the **Normal Map** on the mesh along the U and V axes.  
## Advanced
The **Advanced** settings affect the underlying calculations of your rendering. They do not have a visible effect on your surface.
**Property** | **Description**  
---|---  
**Specular Highlights** | Enable this to allow your material to have specular highlights from direct lighting, for example [Directional, Point, and Spot lights](https://docs.unity3d.com/Manual/Lighting.html). This means that your material reflects the shine from these light sources. Disable this to leave out these highlight calculations, so your Shader renders faster. By default, this feature is enabled.  
  
**Note** : This option affects batching performance.  
**Environment Reflections** | Sample reflections using the nearest [Reflection Probe](https://docs.unity3d.com/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), or, if you have set one in the [Lighting](https://docs.unity3d.com/Manual/GlobalIllumination.html) window, the [Lighting Probe](https://docs.unity3d.com/Manual/LightProbes.html). If you disable this, you will have fewer Shader calculations, but this also means that your surface has no reflections.  
  
**Note** : This option affects batching performance.  
**Enable GPU Instancing** | Makes URP render meshes with the same geometry and material in one batch, when possible. This makes rendering faster. URP can’t render Meshes in one batch if they have different materials or if the hardware doesn’t support GPU instancing.  
**Sorting Priority** | Use this slider to determine the chronological rendering order for a material. URP renders materials with lower values first. You can use this to reduce overdraw on devices by making the pipeline render materials in front of other materials first, so it doesn’t have to render overlapping areas twice. This works similarly to the [render queue](https://docs.unity3d.com/ScriptReference/Material-renderQueue.html) in the built-in Unity render pipeline.  
## Channel packing
This Shader uses [channel packing](http://wiki.polycount.com/wiki/ChannelPacking), so you can use a single RGBA texture for the metallic, smoothness and occlusion properties. When you use texture packing, you only have to load one texture into memory instead of three separate ones. When you write your texture maps in a program like Substance or Photoshop, you can pack the maps like this:
Channel | Property  
---|---  
**Red** | Metallic  
**Green** | Occlusion  
**Blue** | None  
**Alpha** | Smoothness  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/blending-modes.html)
Blending Modes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/simple-lit-shader.html)
Simple Lit Shader Material Inspector window reference for URP
