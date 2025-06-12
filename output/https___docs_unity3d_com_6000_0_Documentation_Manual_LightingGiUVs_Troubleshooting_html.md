* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUVs-Troubleshooting.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-landing.html)
  * Troubleshooting automatically generated lightmap UVs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-visualizing.html)
Check lightmap UVs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-Reference.html)
Lightmap UVs Settings in the Model Import Settings Inspector window reference
# Troubleshooting automatically generated lightmap UVs
## Pack Margin
To allow filtering, the **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) contains lighting information in texels near the chart border, so always include some margin between charts to avoid light bleeding when applying the lightmap.
The lightmap resolution defines the texel resolution of your lightmaps. **Lightmappers** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) dilate some chart texels in the lightmap to avoid black edges, so the UV charts of your **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) need to be at least two full texels apart from each other to avoid light bleeding. Use the **Pack Margin** setting to ensure you have enough margin between the UV charts of your geometry.
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-GeneratingLightmappingUVs-1.jpg)
In lightmap UV space, the padding between charts need to be at least two full texels in order to avoid UV overlapping and accidental light bleeding. In this image, the black space represents the space between charts.
## Min Lightmap Resolution and Min Object Scale
Placing UV charts too close together may cause [cross-chart texel bleeding](https://docs.unity3d.com/6000.0/Documentation/Manual/ProgressiveLightmapper-UVOverlap.html) in the final lightmap. Placing charts too far away from each other wastes memory. The ideal packing margin of an object depends on how many lightmap texels are allotted to it.
The number of texels that Unity uses for a MeshRenderer depends on the MeshRenderer’s lightmap resolution and transform scale. To calculate a good margin, Unity needs to know the expected minimum values for these properties.
A MeshRenderer’s lightmap resolution is a combination of the `Lightmap Resolution` property of the [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html) for the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that the MeshRenderer appears in, and the `Scale in Lightmap` property of the [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html). Note that this means that the same MeshRenderer can have a different lightmap resolution in different Scenes.
You can use the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) to view the lightmap resolution of a MeshRenderer in a given Scene:
  1. In the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) or Hierarchy, select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that has the MeshRenderer component.
  2. In the Inspector, navigate to the MeshRenderer component’s **Lightmapping** section.
  3. Open the **Baked Lightmap** fold-out. Unity displays the MeshRenderer’s lightmap resolution in the baked lightmap with the label **Lightmap Resolution** , and its transform scale in the baked lightmap with the label **Lightmap Object Scale**.


## Angle distortion
The following screenshots demonstrate equal resolution, but with different UVs. The first image has a high **Angle Error** , and the result contains unintended artifacts. The second image has the default **Angle Error** (8%). In Meshes with more triangles, angle distortion can significantly distort the shape.
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-GeneratingLightmappingUVs-2.png)![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-GeneratingLightmappingUVs-3.jpg)
## Area distortion
In the image below, two spot lights with the same parameters light the sides of a cylinder. The right-hand side of the cylinder has a higher **Area Error** value, which distorts the triangles and leads to a lower resolution, creating artifacts in the light.
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-GeneratingLightmappingUVs-4.png)![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightingGiUvs-GeneratingLightmappingUVs-5.jpg)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-visualizing.html)
Check lightmap UVs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-Reference.html)
Lightmap UVs Settings in the Model Import Settings Inspector window reference
