* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ProgressiveLightmapper-UVOverlap.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
  * [Troubleshooting baked lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-troubleshooting.html)
  * Fix light bleeding in lightmaps


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-SeamStitching.html)
Smooth hard edges in lightmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html)
Optimize baking
# Fix light bleeding in lightmaps
Each **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) contains a number of **charts**. At run time, Unity maps these charts onto **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) faces, and uses the charts’ lighting data to calculate the final appearance. Because of the way GPU sampling works, data from one chart can bleed onto another if they are too close to each other. This usually leads to unintended artifacts such as aliasing, pixelation, and so on.
![Example of graphical artifacts due to chart bleeding](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProgressiveLightmapper-UVOverlap-183-0.png) Example of graphical artifacts due to chart bleeding
To avoid light bleeding, there must be a sufficient amount of space between charts. When a GPU samples a lightmap, the lighting system calculates the final sample value from the four texels closest to the sampled point (assuming bilinear filtering is used). These four texels are called the bilinear “neighborhood” of the sampled point. Charts are too close together if they overlap - that is, if the neighbourhood of any point inside a chart overlaps with the neighborhood of any point in another chart. In the image below, the white **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) indicate chart neighbourhoods, and red pixels indicate overlapping neighbourhoods.
![Red pixels indicate overlapping chart neighbourhoods](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProgressiveLightmapper-UVOverlap-183-1.png) Red pixels indicate overlapping chart neighbourhoods
Determining optimal chart placements and spacing can be difficult, because it depends on several parameters (such as lightmap resolution, mesh UVs, and Importer settings). For this reason, Unity provides the ability to identify these issues easily, as outlined in the following section.
## Identification
There are three ways to identify overlaps: 
  * Keep an eye on Unity’s console. If Unity detects overlapping UVs, it prints a warning message with a list of affected **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). 
  * Use the **UV Overlap** draw mode in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) View (see [GI visualizations in the Scene View](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html) for more information). When you have this mode enabled, Unity adds a red highlight to chart texels that are too close to texels of other charts. This is especially useful if you discover an artefact in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView), and want to quickly examine whether UV overlap is causing it.

![Scene View using UV Overlap draw mode \(see dropdown in top left\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProgressiveLightmapper-UVOverlap-183-2.png) Scene View using UV Overlap draw mode (see dropdown in top left)
  * Use **Baked Lightmaps Preview**. Select a GameObject and go to the Lighting window and then choose the **Baked Lightmaps** tab. Double-click the highlighted lightmap, navigate to the Preview window, and select **Baked UV Overlap** (see dropdown in upper right corner). The Preview window colours problematic texels red in this view.

![The Baked Lightmaps Preview in the Lighting window’s Baked Lightmaps tab](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProgressiveLightmapper-UVOverlap-183-3.png) The Baked Lightmaps Preview in the Lighting window’s Baked Lightmaps tab
## Solutions
There is no one single solution for UV overlap, because there are so many things that can cause it. Here are the most common solutions to consider:
  * If you provide lightmap UVs yourself, add margins using your modelling package.
  * If Unity automatically generates the lightmap UVs for a Model, you can tell Unity to increase the pack margin. The simplest way to do this is to set the **Margin Method** to **Calculate** , and set an appropriate **Min Lightmap Resolution** and **Min Object Scale**. If you prefer to set **Margin Method** to **Manual** , you can adjust the **Pack Margin** value directly. For more information on these settings, see documentation on [Generating lightmapping UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-GeneratingLightmappingUVs.html).
  * Increase the resolution of the entire lightmap. This will increase the numbers of pixels between the charts, and therefore reduce the likelihood of bleeding. The downside is that your lightmap may become too large. You can do this in the **Lighting** tab under **Lightmapper Settings**.
  * Increase the resolution of a single GameObject. This allows you to increase lightmap resolution only for GameObjects that have overlapping UVs. Though less likely, this can also increase your lightmap size. You can change a GameObject’s lightmap resolution inside its **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) under **Lightmap Settings**.

![Same mesh as before, but without bleeding artifacts](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProgressiveLightmapper-UVOverlap-183-4.jpg) Same mesh as before, but without bleeding artifacts
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-SeamStitching.html)
Smooth hard edges in lightmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html)
Optimize baking
