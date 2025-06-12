* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * Grass and other details


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Wind-Reference.html)
Wind reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)
Working with Heightmaps
# Grass and other details
A **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) might have grass clumps and other small objects (such as rocks) covering its surface. Unity renders these objects using textured **quads** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad) or full meshes, depending on the **level of detail** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#levelofdetail) and performance you require.
Instancing details work with all **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), including the [High Definition Render Pipeline](https://docs.unity3d.com/Manual/high-definition-render-pipeline.html) (HDRP).
![Terrain with grass](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TerrainWithGrass.png) Terrain with grass
Terrain details are available in several modes, where each mode has a different use during game development.
**Mode** | **Description**  
---|---  
Instanced mesh | Unity recommends you use this mode because it’s best suited for most scenarios that require the placement of any number of arbitrary meshes on Terrain.  
  
To add an instanced mesh, select **Add Detail Mesh** and enable the **Use GPU Instancing** option.  
Vertex Lit mesh | Doesn’t use GPU instancing for rendering. Instead, it combines all detail instances into one mesh, which results in simple shading and limitations to the number of instances you can achieve.  
  
To add a Vertex Lit mesh, select **Add Detail Mesh** and set the **Render Mode** to **Vertex Lit**.  
Grass mesh | Works similar to the vertex list mesh, but Unity treats these meshes as grass so they always have up-facing normals and move in the wind.  
  
To add a grass mesh, select **Add Detail Mesh** and set the **Render Mode** to **Grass**.  
Grass Texture | Lets you create grass quad meshes directly from Texture, which move in the wind. You don’t need to specify any custom meshes, and there’s also an option you can enable to make grass quads always face the camera for a billboard effect.  
  
Select **Add Grass Texture** for this option.  
## Paint Details
To enable grass and detail painting, select the **Paint Details** button on the Terrain **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar).
![Paint Details in the Terrain Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TerrainDetailsPaintTool.png) Paint Details in the Terrain Inspector
To access **Paint Details** from an overlay:
  1. In the **Terrain Tools** overlay, select **Foliage Mode** ![Foliage Mode Menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-FoliageModeMenuButton.png). Foliage Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Foliage Mode tools on the **Terrain Tools** overlay, select **Paint Details** ![Paint Details](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-PaintDetailsButton.png).


Initially, a Terrain has no grass or details available. In the Inspector, click the **Edit Details** button to display a menu with the **Add Detail**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh)** and **Add Grass Texture** options. Click either option to bring up a window that lets you choose **Assets** to add to the Terrain for painting.
### Add Detail Mesh
![The Add Detail Mesh window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TerrainDetailAddWindow.png) The Add Detail Mesh window
Use the **Detail**Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab)** field to select a Prefab from your Project. To create an authentic look, a random factor affects each mesh to determine the size and color. Unity uses the Perlin noise algorithm to generate such random factors.
The **Min Width** , **Max Width** , **Min Height** , and **Max Height** values specify the upper and lower scalings along the X and Y axes with which the meshes are randomly generated.
The **Align to Ground (%)** value specifies how much the detail axis aligns to the terrain normal. 0 is unaligned, and 100 is aligned to the normal.
The **Position Jitter (%)** controls the randomness of the detail distribution from ordered to random. This is only available when legacy distribution is turned off in [Quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Terrain).
The **Noise Seed** setting sets the random number generator seed. Each seed value represents a unique generation. If you set the same seed for two types of details, the generated instances become identical. The **Noise Spread** value refers to the scaling of the noise pattern over the X-Z plane, with higher values indicating more variations within a given area.
The **Hole Edge Padding (%)** setting controls how far away detail objects are from the edge of the hole area. For more information, see [DetailPrototype.holeEdgePadding](https://docs.unity3d.com/2021.2/Documentation/ScriptReference/DetailPrototype-holeEdgePadding.html).
The **Detail Density** value controls the detail’s density relative to its size. You can enable this in “Coverage” detail scatter mode, set in [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).
**Healthy Color** and **Dry Color** settings control the color variation. Unity performs linear interpolation between the healthy and dry colors, and selects a color based on the size of the mesh. For example, the system considers bigger-sized meshes to be healthier. The linear interpolation results for such meshes lean more towards the **Healthy Color** tint. These color settings disappear when you select **Use GPU Instancing** because they have no effect on instanced meshes.
The **Affected by Density Scale** checkbox determines whether the Detail Density Scale setting set in the [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html) affects this detail.
You can set the **Render Mode** to **Vertex Lit** or **Grass**.
**Render Mode** | **Description**  
---|---  
**Vertex Lit** | Renders detail meshes as solid, vertex lit **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), which don’t move in the wind.  
**Grass** | Renders detail meshes in the scene with simplified lighting similar to Grass Textures, and do move in the wind.  
**Note** : To apply a texture on a detail using Vertex Lit or Grass render mode, assign a texture to the **MainTex** material property (default property name for Base Color Map in built-in/URP). No other material properties are considered for non-instanced details.
#### Use GPU Instancing
You can specify if you want to use GPU instancing to render your detail meshes. With GPU instancing, Unity uses the material and the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) specified on the prefab for rendering. This lets you perform more customization in the shader and use [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest).
Unity still applies the Width and Height noise to each instance, but disables the **Healthy Color** /**Dry Color** noise. You can use your own color variation technique, along with other randomizations, in the shader.
Under the hood, some Unity [GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html) limitations do affect rendering. For example:
  * Your target platform needs to support GPU instancing.
  * Your shader must support GPU instancing. (Most shaders do support it.)
  * Objects are rendered in batches of 1,023 or fewer.
  * Instanced **light probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) lighting or **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) lighting aren’t supported.


Unlike regular instancing where Unity dynamically builds up the instancing constant buffer every frame, instancing details have persistent constant buffers for better CPU and GPU performance when the target hardware allows for it, at the cost of moderately increased GPU memory usage.
If you select **Use GPU Instancing** , the **Render Mode** setting becomes grayed out and unavailable.
### Add Grass Texture
![The Add Grass Texture window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TerrainGrassAddWindow.png) The Add Grass Texture window
The Add Grass Texture window
**Detail Texture** is the Texture that represents the grass. You can download Textures from the **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore), or create your own Textures. A Texture is a small image with alpha set to zero for the empty areas. Note that “Grass” is a generic term; it’s possible for a Texture to represent flowers or man-made objects such as barbed wire coils.
The **Min Width** , **Max Width** , **Min Height** , **Max Height** , **Noise Seed** , **Noise Spread** , **Hole Edge Padding (%)** , **Align to Ground (%)** , **Position Jitter (%)** , **Detail Density** , **Affected by Density Scale** , **Healthy Color** , and **Dry Color** settings work the same as they do for meshes. The Add Detail Mesh section above provides more details.
When you enable the ****Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard)** option, the grass images rotate so that they always face the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). This is useful when you want to display a dense field of grass because clumps are two-dimensional, and not visible from the side. However, with sparse grass, the rotations of individual clumps might become visible, which can create a strange visual effect.
## Remove details
To remove a detail, select the detail to remove, click the **Edit Details** button, then select **Remove**. When you remove a detail, Unity clears the data that represents the Terrain area on which you scattered that detail.
* * *
  * 2022–07–20 Page amended 
  * Added information about detail density and distribution.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Wind-Reference.html)
Wind reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)
Working with Heightmaps
