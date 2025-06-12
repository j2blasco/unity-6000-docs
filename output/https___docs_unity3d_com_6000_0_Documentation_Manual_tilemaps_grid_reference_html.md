* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/grid-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * Grid component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html)
Tile palette editor reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
2D Physics
# Grid component reference
The **Grid** component is a guide which helps to align **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), such as [Tiles](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)A simple class that allows a sprite to be rendered on a Tilemap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tile), based on a selected layout. The component transforms Grid cell positions to the corresponding **local coordinates** of the GameObject. The [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) component then converts these local coordinates to world space or **global coordinates**.
Property | Function  
---|---  
**Cell Size** | The size of a cell on this Grid.  
**Cell Gap** | Enter the size (in Unity units) of gaps between cells on this Grid. If a negative number with an absolute value higher than the **Cell Size** is entered, then Unity will automatically change the absolute value to match the **Cell Size** instead.  
For example, if **Cell Size** is (1, 1, 0) and **Cell Gap** is set to (–2, –2, 0), the Editor will automatically change the **Cell Gap** values to (–1, –1, 0) instead.  
**Cell Layout** | Select an option from the drop-down menu to define the shape and arrangement of cells on this Grid.  
**Rectangle** | Cells are rectangular.  
**Hexagon** | Cells are hexagonal.  
**Isometric** | Cells are rhombus-shaped for an isometric layout.  
**Isometric Z as Y** | Similar to the **Isometric Grid** layout, but Unity converts the Z position of cells to their local Y coordinate.  
**Cell Swizzle** | Select the order that Unity reorders the XYZ cell coordinates to for transform conversions. See the Wikipedia article on [Swizzling](https://en.wikipedia.org/wiki/Swizzling_\(computer_graphics\)) for more details.  
**XYZ** | The Grid component uses the default XYZ cell coordinates.  
**XZY** | The Grid component reorders the XYZ coordinates to XZY.  
**YXZ** | The Grid component reorders the XYZ coordinates to YXZ.  
**YZX** | The Grid component reorders the XYZ coordinates to YZX.  
**ZXY** | The Grid component reorders the XYZ coordinates to ZXY.  
**ZYX** | The Grid component reorders the XYZ coordinates to ZYX.  
* * *
  * Page content and screenshots updated for [2020.1](https://docs.unity3d.com/2020.1/Documentation/Manual/30_search.html?q=newin20201) NewIn20201
  * Tilemaps added in [2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172) NewIn20172


Grid
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html)
Tile palette editor reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
2D Physics
