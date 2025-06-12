* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tools.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * Terrain tools


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-CreateNeighborTerrains.html)
Create Neighbor Terrains
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-RaiseLowerTerrain.html)
Raise or Lower Terrain
# Terrain tools
To access the **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) painting tools, click on a Terrain object in the **Hierarchy** window and open an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. In the Inspector, click the **Paint Terrain** (paintbrush) icon to reveal the list of Terrain tools.
![Terrain tools drop-down menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TerrainToolsDropdown_grey.png) Terrain tools drop-down menu
You can also access Terrain painting tools from the Terrain Tools overlay in **Sculpt Mode** ![Sculpt Mode Menu button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-SculptModeMenuButton.png) or **Materials Mode** ![Material Mode Menu button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-MaterialModeMenuButton.png).
![Terrain Toolbar](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-TerrainToolbar.png) Terrain Toolbar
The Terrain component provides six distinct tools:
  * **Raise or Lower Terrain** : paint the **heightmap** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) with a paintbrush tool.
  * **Paint Holes** : hide portions of the Terrain.
  * **Paint Texture** : apply surface textures.
  * **Set Height** : adjust the heightmap toward a specific value.
  * **Smooth Height** : smooth the heightmap to soften Terrain features.
  * **Stamp Terrain** : stamp a brush shape on top of the current heightmap.


## Additional terrain tools
The [Terrain Tools package](https://docs.unity3d.com/6000.0/Documentation/Manual/TerrainTools.html), when you install it, brings additional functionality on top of the built-in terrain tools listed above. It includes erosion tools, sculpting tools, brush mask filters, and a Terrain Toolbox which provides preset file management and heightmap import features, among others.
## Custom terrain tools
The Unity API allows you to create your own custom Terrain tools to complete or override the existing tools, including the ones of the Terrain Tools package.
For more information about Terrain tool API, refer to [TerrainAPI.TerrainPaintTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.html), and to create a custom Terrain tool with overlay support, refer to [TerrainAPI.TerrainPaintToolWithOverlays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintToolWithOverlays_1.html).
The [Terrain Tools package documentation](https://docs.unity3d.com/Packages/com.unity.terrain-tools@latest/index.html?subfolder=/manual/create-custom-tools.html) also provides several Terrain API use case examples.
* * *
  * 2019–10–22 Page amended 
  * Updated screenshot to match the new UI and added the Paint Holes tool.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-CreateNeighborTerrains.html)
Create Neighbor Terrains
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-RaiseLowerTerrain.html)
Raise or Lower Terrain
