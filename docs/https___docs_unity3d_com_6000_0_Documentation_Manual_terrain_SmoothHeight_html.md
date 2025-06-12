* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SmoothHeight.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Terrain tools](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tools.html)
  * Smooth Height


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SetHeight.html)
Set Height
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-StampTerrain.html)
Stamp Terrain
# Smooth Height
The Smooth Height tool smooths the [heightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) and softens **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) features. In the Terrain **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), select **Paint Terrain** , and select **Smooth Height** from the list of Terrain tools.
![Smooth Height tool in the Terrain Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.3.5-SmoothHeight_grey.png) Smooth Height tool in the Terrain Inspector
To access the **Set Height** tool from an overlay:
  1. In the **Terrain Tools** overlay, select **Sculpt Mode** ![Sculpt Mode Menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-SculptModeMenuButton.png). Sculpt Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Smooth Height** ![Smooth Height](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-SmoothHeightButton.png).


The **Smooth Height** tool averages out nearby areas, softens the landscape and reduces the appearance of abrupt changes; it does not significantly raise or lower Terrain height.
Smoothing is useful after you paint with brushes containing high frequency patterns. These brush patterns tend to introduce sharp, jagged edges into a landscape, but you can use the Smooth Height tool to soften that roughness.
Adjust the Blur Direction value to control which areas to soften. If you set **Blur Direction** to –1, the tool softens exterior (convex) edges of your Terrain. If you set **Blur Direction** to 1, the tool softens interior (concave) edges of your Terrain. To smooth all parts of your Terrain evenly, set **Blur Direction** to 0.
The **Brush Size** value determines the size of the Brush to use, and the **Opacity** value determines how quickly the tool smooths out the area you’re painting.
* * *
  * 2019–04–17 Page published 
  * Updated content to reflect new UI and options


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SetHeight.html)
Set Height
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-StampTerrain.html)
Stamp Terrain
