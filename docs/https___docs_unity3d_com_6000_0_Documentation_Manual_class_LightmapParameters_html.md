* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting reference](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-reference.html)
  * Lightmap Parameters Asset Inspector window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html)
Lighting Settings Asset Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html)
Debug Draw Modes for lighting reference
# Lightmap Parameters Asset Inspector window reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html "Go to LightmapParameters page in the Scripting Reference")
## Properties
When you click on a **Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) Parameters Asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window displays the values defined in that Asset. The parameters and their descriptions are listed in the table below.
### Realtime GI
These parameters configure [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html).
See [render pipeline feature comparison](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html) for more information about support for **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) across **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
**Property** | **Function**  
---|---  
**Resolution** | This value scales the **Realtime Resolution** value in the Scene tab of the Lighting Window (menu: **Window** > **Rendering** > **Lighting** > **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)) to give the final resolution of the lightmap in texels per unit of distance.  
**Cluster Resolution** | The ratio of the cluster resolution (the resolution at which the light bounces are calculated internally) to the final lightmap resolution. See documentation on [GI Visualizations in the Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html) for more information.  
**Irradiance Budget** | This value determines the precision of the incoming light data used to light each texel in the lightmap. Each texel’s lighting is obtained by sampling a “view” of the Scene from the texel’s position. Lower values of irradiance budget result in a more blurred sample. Higher values increase the sharpness of the sample. A higher irradiance budget improves the lighting, but this increases run-time memory usage and might increase CPU usage.  
**Irradiance Quality** | Use the slider to define the number of rays that are cast and used to compute which clusters affect a given output lightmap texel. Higher values offer visual improvements in the lightmap, but increase precomputing time in the Unity Editor. The value does not affect runtime performance.  
**Modelling Tolerance** | This value controls the minimum size of gaps in **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) geometry that allows light to pass through. Make this value lower to allow light to pass through smaller gaps in your environment.  
**Edge Stitching** | If enabled, this property indicates that UV charts in the lightmap should be joined together seamlessly, to avoid unwanted visual artifacts.  
**Is Transparent** | If enabled, the object appears transparent during the Global Illumination calculations. Back-faces do not contribute to these calculations, and light travels through the surface. This is useful for invisible emissive surfaces.  
**System Tag** | A group of objects whose lightmap Textures are combined in the same lightmap atlas is known as a “system”. The Unity Editor automatically defines additional systems and their accompanying atlases if all the objects can’t be fitted into a single atlas. However, it is sometimes useful to define separate systems yourself (for example, to ensure that objects inside different rooms are grouped into one system per room). Change the **System Tag** number to force new system and lightmap creation. The exact numeric sequence values of the tag are not significant.  
### Baked GI
These parameters configure [lightmapping](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html).
See [render pipeline feature comparison](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html) for more information about support for lightmapping across render pipelines.
**Property** | **Function**  
---|---  
**Anti-aliasing Samples** | Determines the number of sub-texel positions to use when sampling a lightmap texel. Set the value above 1 to use supersampling to improve lightmap quality and reduce artifacts related to aliasing.  
•A value of 1 disables super sampling.  
•A value of 4 provides 2x2 supersampling. This is the default value which removes most aliasing artifacts.  
•A value of 16 provides 4x4 supersampling. Use these values to remove artifacts, like jagged edges in direct lighting. This can happen when you use baked shadows.  
  
**Note** : A higher anti-aliasing sample value uses more memory. This means that if you use a high sample number in a large Scene with large lightmap texture sizes, the lightmap bake might not complete.  
**Backface Tolerance** | Specifies the percentage of front-facing geometry sampling ray hits a texel must have for Unity to consider it valid. This makes it possible for Unity to invalidate a texel if too many of the rays cast from it hit backfaces (e.g. if the texel is inside geometry). A value of 1.0 means that Unity considers a texel invalid when any of its rays hits a backface, for example. When a texel is invalid, Unity clones valid values from surrounding texels to prevent artifacts. Lower this value to solve lighting problems caused by backface samples. Use the Texel Validity [Scene View Draw Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html) to adjust this value.  
**Pushoff** | Pushes ray origins away from geometry along the normal based on the value you specify in modelling units. Unity applies this value to all baked lightmaps. It affects direct light, indirect light, and baked **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion). Adjust this setting to reduce self-occlusion and self-shadowing artifacts.  
**Baked Tag** | Groups specific sets of objects in atlases. As with the System Tag, the exact numeric value is not significant. Unity never puts **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with different **Baked Tag** values in the same atlas. However, there is no guarantee that objects with the same tag end up in the same atlas because there may be too many objects with that tag to fit into one atlas. See image A (below) for an example of this. You do not need to set this value when you use the multi-scene bake API because Unity groups automatically in that case. You can use **Baked Tag** to replicate some of the behavior of the **Lock Atlas** option. See [Baked Tags: Details](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baked-tags.html) for more information.  
**Limit Lightmap Count** | Applies a limit to the number of lightmaps that Unity can use to pack together GameObjects with the same Baked Global Illumination settings. When you enable this limit, a related setting appears called **Max Lightmaps**. That setting determines the lightmap limit. The [Lightmapping Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html) define the size of these lightmaps.  
  
Unity considers GameObjects to have the same Baked Global Illumination settings if they have equal values for **Anti-aliasing Samples** , **Pushoff** , **Baked Tag** , and **Backface Tolerance**. This means that Unity might pack together GameObjects associated with different Lightmap Parameter Assets.   
  
To pack GameObjects into a set number of lightmaps, Unity scales down UV layouts until all fit within the specified number of lightmaps. This process may reduce lightmap resolution.  
## Baked AO
These parameters configure Baked Ambient Occlusion.
**Property** | **Function**  
---|---  
**Quality** | The number of rays cast when evaluating baked ambient occlusion (AO). A higher numbers of rays increases AO quality but also increases bake time.  
**Anti-aliasing Samples** | The number of samples to take when doing anti-aliasing of AO. A higher number of samples increases the AO quality but also increases the bake time.  
## General GI
**Property** | **Function**  
---|---  
**Backface Tolerance** | The percentage of rays shot from an output texel that must hit front faces for the lighting system to consider them usable. This allows Unity to invalidate a texel if too many of the rays cast from it hit back faces ( (for example, if the texel is inside some geometry). The lighting system clones valid values from the surrounding texels to avoid unintended artifacts.  
  
If **Backface Tolerance** is 0.0, the lighting system rejects the texel only if it sees nothing but backfaces. If it is 1.0, the lighting system rejects the ray origin if it has even one ray that hits a backface.  
LightmapParameters
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html)
Lighting Settings Asset Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html)
Debug Draw Modes for lighting reference
