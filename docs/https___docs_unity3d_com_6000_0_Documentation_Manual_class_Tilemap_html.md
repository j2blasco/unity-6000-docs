* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tilemap.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Tilemap component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
Tilemap Collider 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)
Tilemap Renderer component reference
# Tilemap component reference
The ****Tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap)** component stores and manages [Tile Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html) for creating 2D levels. It transfers the required information from the tiles placed on it to other related components such as the [Tilemap Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html) and the [Tilemap Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html).
The 2D Tilemap Editor package is automatically installed when you create a project with the [2D template](https://docs.unity3d.com/hub/manual/Templates.html). You can install the 2D Tilemap Editor directly from the Unity registry via the [Package Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install.html).
To create, edit, and pick the tiles for [painting onto a tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html), refer to the [Tile Palette](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/create-tile-palette.html) (menu: **Window** > **2D** > **Tile Palette**) documentation for more information on its features and tools.
## Properties
Property | Description  
---|---  
**Animation Frame Rate** | Set the frame rate at which tile animations play. Increasing or decreasing this value changes the frame rate of the tile animations. For example, if set to 2, tile animations play at double the base frame rate. If set to 3, tile animations play at triple the base frame rate.  
**Color** | Select a color to apply as a tint to the tiles on this tilemap. Set to white (default color) to have Unity render the tiles without tint.  
**Tile Anchor** | Enter the amount (in cells) along the xyz axes to offset tile anchor positions on the tilemap.  
**Orientation** | Select the orientation of tiles on the tilemap. Each of the following options performs the same function by orienting the tiles along the selected plane.  
**XY** | Unity orients tiles along the XY plane.  
**XZ** | Unity orients tiles along the XZ plane.  
**YX** | Unity orients tiles along the YX plane.  
**YZ** | Unity orients tiles along the YZ plane.  
**ZX** | Unity orients tiles along the ZX plane.  
**ZY** | Unity orients tiles along the ZY plane.  
**Custom** | Select this option to enable the custom orientation settings below.  
**Offset** | Set the position offset of the custom orientation. This option is only available when you set the tilemap’s **Orientation** to **Custom**.  
**Rotation** | Set the rotation of the custom orientation. This option is only available when you set the tilemap’s **Orientation** to **Custom**.  
**Scale** | Set the scale of the custom orientation. This option is only available when you set the tilemap’s **Orientation** to **Custom**.  
**Info** | Expand this to view the assets present in the tilemap.  
**Tiles** | Displays a list of [Tile Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html) present in the tilemap.  
****Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite)** | Displays a list of sprites present in the tilemap.  
## Additional resources
  * [Tilemap Renderer component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)
  * [Tile Palette preferences reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-preferences-reference.html)


Tilemap
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
Tilemap Collider 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html)
Tilemap Renderer component reference
