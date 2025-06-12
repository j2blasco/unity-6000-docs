* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SetHeight.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Terrain tools](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tools.html)
  * Set Height


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-PaintTexture.html)
Paint Texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SmoothHeight.html)
Smooth Height
# Set Height
Use the **Set Height** tool to adjust the height of an area on the **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) to a specific value. To access the tool, click on the **Paint Terrain** icon, and select the **Set Height** tool from the drop-down menu.
![Set Height tool in the Terrain Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/1.3.4-SetHeight_grey.png) Set Height tool in the Terrain Inspector
To access the **Set Height** tool from an overlay:
  1. In the **Terrain Tools** overlay, select **Sculpt Mode** ![Sculpt Mode Menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-SculptModeMenuButton.png). Sculpt Mode tools display at the end of the **Terrain Tools** overlay.
  2. From the available Sculpt Mode tools on the **Terrain Tools** overlay, select **Set Height** ![Set Height](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/terrainOverlays-SetHeightButton.png).


When you paint with the **Set Height** tool, it lowers areas of the Terrain currently above the target height, and raises areas below that height. **Set Height** is useful for creating flat, level areas in a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), such as plateaus or man-made features like roads, platforms, and steps.
Choose a property from the **Space** drop-down menu to specify whether the height offset is relative to **Local** or **World** space.
**Property** | **Description**  
---|---  
**World** The area in your scene in which all objects reside. Often used to specify that coordinates are world-relative, as opposed to object-relative.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#World) | Select this to set the height offset to the value you enter in the **Height** field. However, be aware that the **Set Height** tool cannot lower a Terrain below its Transform Position Y coordinate, even if you enter a value lower than the Y coordinate.  
**Local** | Select this to set the height offset relative to the Terrain. For example, if you enter 100 in the **Height** field, the height offset is the sum of the Terrain’s Transform Position Y coordinate and 100 (`terrain.transform.position.y` + 100). The **Height** value you enter must range from 0 to the **Terrain Height** value in the [Terrain settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Enter a numerical value in the **Height** field, or use the **Height** property slider, to manually set a height. Alternatively, press Shift and click on the Terrain to sample the height at the cursor position, similar to how you would use the Eyedropper tool in an image editor.
If you press the **Flatten Tile** button under the **Height** field, it levels the whole Terrain tile to the height you specified. This is useful to set a raised ground level if, for example, you want the landscape to include both hills above the ground level and valleys below it. If you press the **Flatten All** button, it levels all Terrain tiles in the Scene.
The **Brush Size** value determines the size of the Brush to use, while the **Opacity** value determines how quickly the height of the area you’re painting reaches the set target height.
You can also use **heightmaps** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) to edit the height of your Terrain. For more information, see [Working with Heightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html).
* * *
  * 2019–10–22 Page amended 
  * Updated content to match the new UI and added information about the Space option.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-PaintTexture.html)
Paint Texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-SmoothHeight.html)
Smooth Height
