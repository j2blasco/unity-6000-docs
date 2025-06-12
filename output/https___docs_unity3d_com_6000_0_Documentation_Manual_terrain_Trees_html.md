* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * Add trees to the terrain


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Colliders.html)
Add collision to trees
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)
Animate trees with Wind Zones
# Add trees to the terrain
Use the Paint Trees tool to place trees on the **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) and customize their painting. You can paint trees with a brush or mass place trees across the entire terrain tile.
As an example, use the [free Unity Terrain - HDRP Demo Scene](https://assetstore.unity.com/packages/3d/environments/unity-terrain-hdrp-demo-scene-213198), which has six SpeedTree models. You can also create trees with the [Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html) (for the Built-In Render Pipeline).
## The Paint Trees tool
To access tree painting:
  1. In the **Hierarchy** window, select the terrain.
  2. In the terrain’s ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, from the **Terrain** **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar), select **Paint Trees**.


### Select trees
To add trees to the terrain, add a tree prototype to the Paint Tree tool:
  1. Select **Edit Trees** > **Add Tree**.
  2. Select a tree.


The **Add Tree** window has different options based on the tree you’re adding:
  * **Bend Factor** : Adjust the tree’s responsiveness to the wind in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Trees from the SpeedTree Modeler don’t have a **Bend Factor** ; only Tree Editor trees do. Refer to [Animate trees with Wind Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html) for more information.
  * ****NavMesh** A mesh that Unity generates to approximate the walkable areas and obstacles in your environment for path finding and AI-controlled navigation. [More info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-areas)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#NavMesh) **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) Index**: SpeedTree uses level of detail (LOD) groups. The Unity Editor manages the transitions between groups, but if you’re placing trees that are never going to be near the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), or if you need to limit the display quality of trees without editing the model, you can select a specific **LOD group** A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup). The options are: 
    * **First** : The highest LOD, for trees that are close to the player.
    * **Last** : The lowest LOD, for trees that are far away from the player.
    * **Custom** : To select a different level.
Refer to [Tree level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-LOD.html) for more information.
  * **Cast Shadows** : For Tree Editor trees. This is not editable; it lists the option selected in the tree’s **Mesh Renderer** > **Lighting** > **Cast Shadows** setting.


### Customize trees for painting
Customize tree placement and characteristics. Except for **Brush Size** and **Tree Density** , the settings apply to both mass placed trees and brush painted trees.
**Property** | **Function**  
---|---  
**Brush Size** | The size of the area each brush stroke covers with trees.  
**Tree Density** | How far apart trees must be. This limits the number of trees a single brush stroke adds. Note that the limit is by brush stroke, not area, so repeated brush strokes in the same area create higher densities. Note also that the larger the brush, the farther apart the trees, even if the density is 100.  
**Tree Height** | A range for tree height randomization. Use a wide range for a varied look, and a narrow range for a uniform look. To specify a value instead of a range, disable **Random**. The possible values are a scale of `0.01` to `2` of the tree’s original height.  
**Lock Width to Height** | By default, a tree’s width is locked to its height so that trees are always scaled uniformly. To specify a width, disable **Lock Width to Height**.  
**Tree Width** | A range for tree width randomization. Use a wide range for a varied look, and a narrow range for a uniform look. To specify a value instead of a range, disable **Random**. The possible values are a scale of `0.01` to `2` of the tree’s original width.  
**Random Tree Rotation** | If your tree has a level of detail (LOD) Group (for example, a tree imported from SpeedTree), use the **Random Tree Rotation** setting to help create the impression of a random, natural-looking forest. Disable this option if you want to place trees with a fixed rotation.  
**Color Variation** | The amount of random shading applied to trees. This works only if the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) reads the `_TreeInstanceColor` property. All trees created with Tree Editor read the `_TreeInstanceColor` property, because they all use built-in shaders. Some SpeedTree trees might not read it.  
**Tree Contribute Global Illumination** | Non-editable; indicates whether the tree asset’s **Lighting** > **Contribute Global Illumination** option is enabled.  
### Mass place trees
You can place trees across the entire terrain tile in a single action. Refer to Customize trees for painting (above) for information about customizing trees before painting.
To place trees on an entire terrain tile:
  1. Select tree assets as explained above. Note that mass placing uses all the trees in the **Trees** list, not just the highlighted tree.
  2. Select **Mass Place Trees**. The **Place Trees** window opens.
  3. Enter the number of trees you want to place.
  4. To keep the trees you already have, check the **Keep Existing Trees** box. If you don’t check this box, Unity removes all existing trees and replaces them with the new trees.


You can use the brush tools to add or remove trees that you mass placed.
### Paint trees with a brush
You can paint trees onto the terrain with a brush. 
To paint trees:
  1. Select trees as explained above.
  2. Refer to Customize trees for painting (above) for information about the brush settings and customizing trees for painting.
  3. Paint trees on the terrain using the brush.
  4. To remove: 
     * All trees from an area: hold **Shift** as you paint.
     * Only the tree selected in the **Trees** list: hold **Ctrl** as you paint.


## Edit trees
You can edit the tree’s properties before you place it, or between painting strokes. For example, for SpeedTree trees, you can change the LOD group you use when painting different parts of the terrain. 
To edit a tree:
  1. In the **Trees** list, select the tree you want to edit.
  2. Select **Edit Trees** > **Edit Tree**. The **Edit Tree** window opens. It has the same options as the **Add Tree** window.


## Update imported trees
If you change an imported tree in a separate 3D modeling application, you need to refresh the tree in the Paint Tool to update its appearance on the terrain.
To update the trees, in the Terrain tile’s **Inspector** window, go to **Paint Trees** > **Trees** > **Refresh**.
**Note:** Trees from SpeedTree use their own shader to animate wind movement. The Unity Editor adds this shader only to trees that SpeedTree exports with the file type `spm` or `st8`. If you edit the trees using a different 3D modeling software and export them as `fbx` or `obj` files, the Unity Editor assigns them built-in shaders, and the wind effect is lost. To preserve the wind animation, always use SpeedTree to edit and re-export SpeedTree trees.
## Additional resources
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * [Add collision to trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Colliders.html)
  * [Tree level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-LOD.html)
  * [Animate trees with Wind Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)
  * [Terrain Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-Colliders.html)
Add collision to trees
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)
Animate trees with Wind Zones
