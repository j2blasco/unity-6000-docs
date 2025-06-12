* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-visualizing.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-landing.html)
  * Check lightmap UVs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
Generate lightmap UVs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUVs-Troubleshooting.html)
Troubleshooting automatically generated lightmap UVs
# Check lightmap UVs
It is important to be able to view the lightmap UVs that are being used, and Unity has a visualization tool to help you with this. First, open the Lighting window (menu: **Window** > **Rendering** > **Lighting**) and tick the **Auto** checkbox at the bottom. This ensures that your bake and precompute are up-to-date, and outputs the data that is needed to view the UVs. Wait for the process to finish (this can take some time for large or complex Scenes).
## Check real-time lightmap UVs
To see the UVs for the Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) system:
  * Select a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with a ****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer** component.
  * In the ****Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer)** component, under **Lightmapping** , open the **Realtime**Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap)** dropdown.
  * Double-click a lightmap texture to open the **Viewer** window.
  * In the **Viewer** window, open the dropdown and select **UV Charts**.

![UV layout for the real-time lightmap of the selected instance of this Mesh. ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-0.jpg) UV layout for the real-time lightmap of the selected instance of this Mesh. 
This displays the UV layout for the real-time lightmap of the selected instance of this Mesh. 
  * The charts are indicated by the different colored areas in the Preview (show in the image above on the right-hand side).
  * The UVs of the selected instance are laid over the charts, as a wireframe representation of the GameObject’s Mesh.
  * Dark gray texels show unused areas of the lightmap.


Multiple instances can be packed into a real-time lightmap, so some of the charts you see might actually belong to other GameObjects.
## Check baked lightmap UVs
To see the UVs for the Baked Global Illumination system:
  * Select a GameObject with a **Mesh Renderer** component.
  * In the **Mesh Renderer** component, under **Lightmapping** , open the **Baked Lightmap** dropdown.
  * Double-click a lightmap texture to open the **Viewer** window.
  * In the **Viewer** window, open the dropdown and select **Baked UV Charts**.

![Baked UVs are very different to precomputed real-time UVs.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-1.jpg) Baked UVs are very different to precomputed real-time UVs.
As you can see, the baked UVs are very different to the precomputed real-time UVs. This is because the requirements for baked and precomputed real-time UVs are different.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
Generate lightmap UVs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUVs-Troubleshooting.html)
Troubleshooting automatically generated lightmap UVs
