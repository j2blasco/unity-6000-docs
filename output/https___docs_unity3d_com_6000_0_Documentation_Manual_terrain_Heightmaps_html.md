* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * Working with Heightmaps


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html)
Grass and other details
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)
Terrain Settings reference
# Working with Heightmaps
Terrain tools that affect height, such as [Raise or Lower Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-RaiseLowerTerrain.html) and [Set Height](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SetHeight.html), use a grayscale texture called a heightmap. Unity represents the height of each point on the **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) as a value in a rectangular array. It represents this array using a grayscale [heightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-types.html#TerrainHeightmaps)A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap). Heightmaps are built into the Terrain, and the values stored in a heightmap define the height of each point or vertex on the Terrain. 
![Example heightmap](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.9-ExampleHeightmap.png) Example heightmap
## Importing and exporting heightmaps
You can import and export heightmaps into the Unity Editor. This is useful when you want to use real world height data to replicate a landmark such as Mount Everest, or work on a heightmap image in an external image editor. You can also use 3D modelling applications, such as Houdini and World Machine, to generate Terrain, then import your Terrain into Unity as a heightmap.
It’s good practice to store heightmaps as RAW files. A RAW file uses a 16-bit grayscale format that’s compatible with most image and landscape editors. The Unity Editor enables you to import and export RAW heightmap files for a Terrain.
To access the import and export settings into the Editor, select the Terrain component in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), and click the **Terrain Settings** button (gear icon in the toolbar).
![Import Raw and Export Raw buttons in the Terrain Settings Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.9-TerrainSettings_TextureResolutions.png) Import Raw and Export Raw buttons in the Terrain Settings Inspector
Under **Texture Resolutions (On Terrain Data)** , there are two buttons labelled **Import Raw** and **Export Raw**. 
  * **Import Raw** allows Unity to read a heightmap from the RAW file format, and generate it in the Editor.  
  
![Import Heightmap window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.9-ImportRaw.png)
  * **Export Raw** allows Unity to write a heightmap from the Editor to the RAW file format.  
  
![Export Heightmap window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.9-ExportRaw.png)


### Import and export options
**Property** | **Description**  
---|---  
**Depth** | Determines how many bits Unity uses per pixel in the imported or exported heightmap.  
• Bit 16: Uses 16 bits (2 bytes)  
• Bit 8: Uses 8 bits (1 byte)  
**Resolution** | The texture resolution (width and height) of the imported heightmap.  
**Byte Order** | Determines how Unity orders the bytes for each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) in the imported or exported heightmap. This mainly applies to bit–16 depth heightmaps, and is platform-dependent.  
**Flip Vertically** | Determines whether Unity flips the exported heightmap vertically across the x-axis.  
**Terrain Size** | The size of Terrain that Unity will apply the imported heightmap to.  
* * *
  * 2020–06–30 Page amended 
  * Updated content to reflect new UI and options


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html)
Grass and other details
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)
Terrain Settings reference
