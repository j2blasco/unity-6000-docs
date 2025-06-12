* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainLayer.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * Terrain Layers


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-StampTerrain.html)
Stamp Terrain
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Brush.html)
Brushes
# Terrain Layers
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer.html "Go to TerrainLayer page in the Scripting Reference")
A **Terrain Layer** is an Asset that defines a **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain)’s surface qualities. A Terrain Layer holds [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) and other properties that the Terrain’s Material uses to render the Terrain surfaces. Because Terrain Layers are Assets, you can reuse them on multiple Terrain tiles.
You can add Textures to the surface of a Terrain to create coloration and fine detail. Terrain **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) are often large, so it’s best to use a base Terrain Layer with Textures that tile over the surface and repeat seamlessly. You can use multiple Terrain Layers, each with different Textures, to build up interesting, varied Terrain surfaces.
The first Terrain Layer you apply to a Terrain automatically becomes the base layer and spreads over the whole landscape. You can paint areas with other Terrain Layers to simulate different ground surfaces, such as grass, desert, or snow. To create a gradual transition between grassy countryside and a sandy beach, you might choose to apply Textures with variable opacity.
![Terrain with sandy texture](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.4-SandyTerrain.png) Terrain with sandy texture
## Creating Terrain Layers
To create a Terrain Layer directly in the Terrain **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), click the paintbrush icon in the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) at the top of the Terrain Inspector, and select **Paint Texture** from the drop-down menu. At the bottom of the **Terrain Layers** section, click the **Edit Terrain Layers** button, and choose **Create Layer**.
![Create Layer in the Terrain Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.4-CreateLayer.png) Create Layer in the Terrain Inspector
To edit terrain layers from an overlay:
  1. In the **Terrain Tools** overlay, select **Materials Mode** ![Material Mode Menu button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-MaterialModeMenuButton.png). Materials Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Materials Mode tools on the **Terrain Tools** overlay, select **Paint Texture** ![Paint Texture](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-PaintTextureButton.png).
  3. In the **Tool Settings** overlay, select **Edit Terrain Layers**.

![Create Layer in Overlays](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-LayersExample.png) Create Layer in Overlays
When you select **Create Layer** , Unity opens the **Select Texture2D** window. Here, choose the image to use as the **Diffuse** channel of the Terrain Layer. To assign a **Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) or **Mask Map** Texture to your Terrain Layer, select the corresponding Terrain Layer in the Project view, and use its Inspector window.
Alternatively, to create a Terrain Layer Asset that isn’t automatically associated with a Terrain, right-click the Project window, and select **Create > Terrain Layer** from the context menu. Then, configure the various properties in the Inspector window for your new Terrain Layer.
For information about how the number of Terrain Layers affects rendering performance, see [Rendering performance](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainLayer.html#Performance). Even assigned Terrain Layers that you don’t actually paint onto the Terrain tile might impact the rendering performance.
## Adding Terrain Layers
Initially, a Terrain has no Terrain Layers assigned to it. By default, it uses a checkerboard Texture until you add a Terrain Layer.
After you create a Terrain Layer in your Project, click the **Edit Terrain Layers** button and select **Add Layer** to open the **Select TerrainLayer** window. Double-click on a Terrain Layer in this window to add it to your Terrain.
## Terrain Layer properties
Depending on the Material set in the [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html) and the Render Pipeline in use, you might see different options and properties in the Inspector.
![Terrain Layer settings in the Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.4-TerrainLayerSettings.png) Terrain Layer settings in the Inspector
### Diffuse settings
The Diffuse Texture represents the base color Texture of the Terrain Layer. The Alpha channel of the Diffuse Texture has different uses, which depend on the active Scriptable Render Pipeline and Shader you use to render the Terrain.  
  
For example, the High Definition Render Pipeline (HDRP) and Universal Render Pipeline (URP) use the Alpha channel for Smoothness. However, if there is a Mask Map Texture on the Terrain Layer, it uses the Alpha channel of the Diffuse Texture for Density values.
**Property** | **Description**  
---|---  
**Color Tint** | If you assign a Diffuse Texture, a new field called **Color Tint** appears in the Terrain Layer settings. Click the color picker field and select a color to use.  
  
**Color Tint** is a feature available in HDRP and URP.  
**Opacity as Density** | Specifies whether to render the Terrain Layer using the value stored in the Alpha channel of the Terrain Layer’s Diffuse Texture, instead of the usual splatmap weight or the height value from the Mask Map. Unity uses the Alpha channel value as a threshold value for layer blending.  
  
**Opacity as Density** is a feature available in HDRP and URP. This option becomes available on each Terrain Layer when you disable the **Enable Height-based Blend** option on the Terrain’s Terrain Lit Material, and when you assign Diffuse and Mask Map Textures to the Terrain Layer.  
### Normal map
The Normal Map Texture contains the normal information for your Terrain Layer. Unity uses this information in lighting calculations.
  * If you don’t assign a Normal Map Texture and enable instancing in the [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html), the Terrain uses the normals generated from the Terrain **heightmap** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap).
  * If you assign a Normal Map Texture and enable instancing, Unity uses the Normal Map Texture instead of the normals generated from the heightmap.
  * If you disable instancing on the Terrain, the built-in Terrain Material uses normals generated from the Terrain geometry, even if you assign a Normal Map Texture on the Terrain Layer.


### Normal scale settings
If you assign a Normal Map Texture, a new field called **Normal Scale** appears in the Terrain Layer settings. This value acts as a scaling factor for the normal values present in the Normal Map. A value of 0 means that the normals stored in the Normal Map have a scale of 0, while a value of 1 means that the normals are at full scale or influence.  
  
Examples and results of different Normal Scale values:
**Property** | **Description**  
---|---  
**Normal Scale** = 0 | • Multiplies the unpacked normal value by 0.  
• The strength, and thus the length, of the normal will be 0, and has no effect on lighting calculations. The mesh triangle on the Terrain effectively uses the mesh normal for lighting calculations.  
**Normal Scale** = 1 | • Multiplies the unpacked normal value by 1.  
• The strength of the normal will be 100%.  
**Normal Scale** = 2 | • Multiplies the unpacked normal value by 2.  
• The strength of the normal will be 200%, and appear twice as pronounced as normals with a Normal Scale of 1.  
**Normal Scale** = –1 | • Multiples the unpacked normal value by –1.  
• The strength of the normal will be at 100% but negated, making the normals point in the opposite direction from normals with a Normal Scale of 1.  
### Mask map
The TerrainLit Shader, which is part of the HDRP and URP, uses this Mask Map Texture data. Custom Terrain shaders might also use this Texture for user-defined purposes, such as ambient occlusion or height-based blending.  
  
For the HDRP and URP TerrainLit Shader, the RGBA channels of the Mask Map Texture correspond to R, G, B, or A.
**Property** | **Description**  
---|---  
**R** | Metallic  
**G** | **Ambient Occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion)  
**B** | Height  
**A** | Smoothness (Diffuse Alpha becomes Density)  
**Channel Remapping** | If you assign a Mask Map Texture, a new heading called **Channel Remapping** appears in the Terrain Layer settings. Click the triangle next to that heading to display the fields for minimum and maximum RGBA values. Unity uses these ranges to remap values in each channel of the Mask Map Texture.  
### Visual settings
The visual properties of the Terrain Layer.
**Property** | **Description**  
---|---  
**Specular** | The specular highlight color of the Terrain Layer.  
**Metallic** | The overall metallic value of the Terrain Layer.  
**Smoothness** | The overall smoothness value of the Terrain Layer.  
### Tile settings
The tiling settings that apply to all Textures the Terrain Layer uses.
**Property** | **Description**  
---|---  
**Size** | The size of the Textures in Terrain space, and how often the Textures tile.  
**Offset** | A base offset that Unity applies to the sample location for each Texture in the Terrain Layer.  
## **Texture painting**
Unity applies the first Terrain Layer you add to the entire landscape. If you add multiple Terrain Layers, use the [Paint Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-PaintTexture.html) tool to apply subsequent Textures to your Terrain.
If you add a new Terrain tile without any Terrain Layers, and paint on it, the system automatically adds the selected Terrain Layer to that new Terrain tile. Because this is the first Terrain Layer, that Texture becomes the base layer, and fills the entire Terrain tile.
In the Terrain Inspector, under **Brushes** , there is a box that displays the available Brushes, along with the **Brush Size** and **Opacity** options underneath. See [Creating and Editing Terrains](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html) for more information about these tools.
## **Rendering performance**
The number of Terrain Layers you assign to a Terrain tile might impact the performance of the renderer. The maximum recommended number of Terrain Layers depends on which [render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) your Project uses.
  * If your Project uses the [Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html) or [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html), you can use four Terrain Layers per Texture pass, with no limit on the number of passes. This means that though you can to use as many Terrain Layers as you want, each pass increases the time spent rendering the Terrain. For maximum performance, limit each of your Terrain tiles to four Terrain Layers.
  * If your Project uses the [High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/6000.0/Documentation/Manual/high-definition-render-pipeline.html), you can add up to eight Terrain Layers per Terrain tile, and the system renders them in a single pass. No additional passes are possible. If you add more than eight Terrain Layers, they appear in the **Inspector** window, but they don’t render in the Editor or at runtime. Any areas painted with these extra layers appear black. To make additional layers visible, remove one or more of the existing layers from the Terrain Layer list.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-StampTerrain.html)
Stamp Terrain
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Brush.html)
Brushes
