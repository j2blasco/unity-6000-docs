* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-StampTerrain.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Terrain tools](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tools.html)
  * Stamp Terrain


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SmoothHeight.html)
Smooth Height
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainLayer.html)
Terrain Layers
# Stamp Terrain
Use the **Stamp Terrain** tool to stamp a brush shape on top of the current [heightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap). In the **Terrain Inspector** , click on the **Paint Terrain** icon and select **Stamp Terrain** from the drop-down menu.
![Stamp Terrain tool in the Terrain Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.3.6-StampTerrain.png) Stamp Terrain tool in the Terrain Inspector
To access the **Stamp**Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain)** tool from an overlay:
  1. In the **Terrain Tools** overlay, select **Sculpt Mode** ![Sculpt Mode Menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-SculptModeMenuButton.png). Sculpt Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Stamp Terrain** ![Stamp Terrain button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-StampTerrainButton.png).


**Stamp Terrain** is useful if you create a custom brush using a Texture that represents a heightmap with a specific geological feature, such as a hill.
With the **Stamp Terrain** tool, you can choose an existing brush and apply it with a single click. Each click raises the Terrain to the set **Stamp Height** in the shape of the selected brush. To multiply the **Stamp Height** by a percentage, move the **Opacity** slider to change its value. For example, a **Stamp Height** of 200 and an **Opacity** of 50% sets the height of each stamp to 100.
The **Max <–> Add** slider lets you choose whether to pick the maximum height, or add the height of your stamp to the Terrain’s current height.
  * If you set the **Max <–> Add** value to 0, then stamp onto the Terrain, Unity compares the height of your stamp to the current height of the stamped area, and sets the final height to the value that is higher.
  * If you set the **Max <–> Add** value to 1, then stamp onto the Terrain, Unity adds the height of your stamp to the current height of the stamped area, so that the final height is the sum of both values.


Enable the **Subtract** checkbox to subtract the height of any stamps you apply to the Terrain from the existing height of the stamped area. Note that **Subtract** works only if your **Max <–> Add** value is greater than zero, for example, if you set the **Max <–> Add** value to 1. If the stamp height exceeds the current height of the stamped area, the system levels the height to zero.
* * *
  * 2019–04–18 Page published 
  * Updated content to reflect new UI and options


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SmoothHeight.html)
Smooth Height
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainLayer.html)
Terrain Layers
