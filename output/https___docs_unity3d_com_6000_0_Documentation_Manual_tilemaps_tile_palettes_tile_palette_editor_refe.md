* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * [Tile palettes](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-landing.html)
  * Tile palette editor reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-preferences-reference.html)
Tile palette preferences reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/grid-reference.html)
Grid component reference
# Tile palette editor reference
You can use different features and tools in the **Tile Palette** editor window to create and edit [tile palettes](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/create-tile-palette.html) and the way you paint on [tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap).
To open the **Tile Palette** window, go to **Window > 2D > Tile Palette**. If you have created a [Tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html), select it in the **Hierarchy** window and the **Open Tile Palette** overlay appears in the **Scene** view. Select the **Open Tile Palette** in the overlay to open the **Tile Palette** window.
Use these tools to paint tiles on a tilemap. Specific instructions on how to use these tools are available on their respective pages.
![The Tile Palette editor window with labelled sections.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-window_labelled.png) The **Tile Palette** editor window with labelled sections.
A: The **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) displaying the palette tools available.  
B: The **Active Target** dropdown menu and overlay toggle buttons.  
C: The main window where you view and edit the active tile palette’s contents.  
D: The **Brush**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window.
## Tile Palette toolbar 
Select a tool from the toolbar to when painting on the tilemap for additional properties and effects. You can also use these tools to edit the active [tile palette](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/create-tile-palette.html) itself by [unlocking the tile palette for editing](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html#mainwindow). Refer to each tool’s documentation for more information about their specific uses and features.
Control | Description | Shortcut key  
---|---|---  
![Select tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-select-tool.png)  
**[Select tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/select-tool/select-tool-landing.html)** | Use the **Select** tool to select a tile on the Active Tilemap or click and drag over multiple tiles to select more at once. | **S**  
![Move tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-move-tool.png)  
**[Move tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/move-tiles-with-move-tool.html)** | Use the **Move** tool to move a tile selection made with the **Select tool**. **Note:** The **Move tool** can’t select tiles itself. | **M**  
![Paint tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-paintbrush-tool.png)  
**[Paint tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/paint-tiles-with-paint-tool.html)** | Use the **Paint** tool to select a tile on the tile palette, or click and drag over multiple tiles to select more at once. Then click on the tilemap in the scene to paint with the selected tiles. | **B**  
![Box Fill tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-boxfill-tool.png)  
**[Box Fill tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/fill-area-with-box-fill-tool.html)** | Use the **Box Fill** tool to select a tile on the tile palette, or click and drag over multiple tiles to select more at once. Then click and drag the **Box Fill** tool over the tilemap in the scene to draw a rectangular shape, which is then filled with the selected tile(s) when you release the tool. | **U**  
![Pick tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-picker-tool.png)  
**[Pick Tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/create-brush-picks-from-tiles-pick-tool.html)** | Use the **Pick** tool to pick a tile from the tilemap or tile palette, or click and drag over multiple tiles to select more at once. The active tool switches to the **Paint** tool once you make the selection and you can paint on the tilemap with the selected tile(s). | **I**  
![Eraser tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-eraser-tool.png)  
**[Eraser tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/remove-tiles-with-eraser-tool.html)** | Use the **Eraser** tool to erase tiles by selecting them with this tool. To erase many tiles at once, first click and drag the **Eraser** tool to a larger size in the tile palette, then paint over tiles you want to erase on the tilemap. | **D**  
![Flood Fill tool](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-floodfill-tool.png)  
**[Flood Fill tool](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tools/fill-area-with-flood-fill-tool.html)** | Use the **Flood Fill** tool to fill a contiguous area of empty cells or identical tiles with the selected tile. Select the tile to use as the fill by selecting it from the tile palette. This tool can’t be used with more than one tile. | **G**  
![Rotate Counter-Clockwise](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-rotate-counter-clockwise.png) | Rotates the active brush counterclockwise. | **[**  
![Rotate Clockwise](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-rotate-clockwise.png) | Rotates the active brush clockwise. | **]**  
![Flip X](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-flip-x.png) | Flips the active brush along the x-axis. | **Shift+[**  
![Flip Y](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-tile-palette-flip-y.png) | Flips the active brush along the y-axis. | **Shift+]**  
## Active Target dropdown menu and overlay buttons 
Control | Description  
---|---  
![The Active Target dropdown menu.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-dropdown.png)  
**Active Target** | This displays the current active Tilemap the editor is targeting, and lists the name of available tilemaps in this project. Select from the list of tilemaps to make that tilemap the **Active Target**.  
![Brush picks overlay toggle button.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-brush-pick-overlay-button.png)  
**Brush picks overlay toggle** | Select this to display or hide the tile palette’s [**Brush Picks**](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/brushes/brush-picks/tile-palette-brush-picks.html) overlay in the **Scene** view.  
![Clipboard overlay toggle button.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-clipboard-overlay-button.png)  
**Tile Palette clipboard overlay toggle** | Select this to display or hide the [Tile Palette Clipboard overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html#tile-palette-clipboard-overlay) in **Scene** view.  
### Active Target dropdown
The following control options are available in the **Active Target** dropdown and when you select **Create New Tilemap**.
Control | Description  
---|---  
![Visibility toggle.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-palette-editor-visible-eye-icon.png)  
**Visibility toggle** | Select this to reveal or hide the target tilemap in the **Scene** view.  
![Ping button.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2d-palette-editor-picker-icon.png)  
**Ping button** | Select this to highlight the target tilemap in the **Hierarchy** window to help you identify the target tilemap.  
**Create New Tilemap** | Select the type of tilemap you want to create and name it at creation. If you don’t enter a name, Unity names the newly created tilemap as “**Tilemap** ” by default and appends a number to it if there are duplicate tilemaps with the same name.  
**From Tile Palette** | Select this to create a tilemap based on the tile dimensions of your active tile palette. This changes the tile dimensions of the parent **Grid** of the child tilemap to match the tile palette. This ensures that the tiles of the tile palette fits the newly created tilemap.  
**Rectangular Tilemap** | Select this to create a default rectangular tilemap.  
**Hexagonal Point Top Tilemap** | Select this to create [Hexagonal Point Top tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html).  
**Hexagonal Flat Top Tilemap** | Select this to create [Hexagonal Flat Top tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/hexagonal-tilemaps.html).  
**Isometric Tilemap** | Select this to create an [Isometric tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html).  
**Isometric Z As Y Tilemap** | Select this to create an [Isometric Z As Y tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html).  
### Tile Palette Clipboard overlay 
This overlay is a compact version of the **Tile Palette** editor’s [main editor window](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html#mainwindow) in the ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)** view. It mirrors the main editor window’s tile palette and toggles. Changing the active tile palette in one window also changes it in the other window. Use this overlay to keep a copy of the tile palette in the **Scene** view even when you minimize the **Tile Palette** editor. **Note:** Closing the **Tile Palette** editor also closes this overlay.
![The Tile Palette Clipboard overlay.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-clipboard-overlay.png) The Tile Palette Clipboard overlay.
## Main editor window 
This section of the window displays the active tile palette, and is where you edit the contents of the tile palette.
Control | Description  
---|---  
![The Active Palette.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-window-palette-dropdown.png)  
**Active Palette** | This displays the current active tile palette and lists the name of available tile palettes in this project. Select from the list of tile palettes to make that tile palette the **Active Palette**.  
**Create New Tile Palette** | Select this to create a new [tile palette](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/create-tile-palette.html). Unity names the created tile palette “New Palette” default and appends a number to it if there are duplicate tile palettes with the same name.  
![Edit Tile Palette toggle.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-window-edit-palette-toggle.png)  
**Edit Tile Palette toggle** | Select this to unlock or lock the **Active Palette** for editing with the [Tile Palette toolbar](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html#toolbar).  
![Grid visibility toggle.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-window-grid-toggle.png)  
**Grid visibility toggle** | Select this to reveal or hide the grid lines in the **Tile Palette** editor window. This toggle is switched on by default.  
![Gizmo visibility toggle.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/tile-palette-window-gizmo-toggle.png)  
**Gizmo visibility toggle** | Select this to reveal or hide gizmos in the **Tile Palette** editor window.  
## Brush Inspector window
You can find the **Brush Inspector** window at the bottom of the **Tile Palette** editor window, and you can use it to change the current [active brush](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/brushes/active-brush.html) and its properties. You can minimize or expand the **Brush Inspector** by clicking the **Brush Inspector** visibility toggle, or drag the bottom toolbar upwards to expand it the window.
Use the dropdown menu to change the active brush from the **Default Brush** to one of the [2D Tilemap Extras package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest)’s [Scriptable Brushes](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/Brushes.html).
Control | Description  
---|---  
**Default Brush** | The default brush with no additional properties.  
**[GameObject Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/GameObjectBrush.html)** | Select this brush to instance, place and manipulate **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) onto the **Scene** view.  
**[Group Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/GroupBrush.html)** | Select this brush to pick tiles which are grouped together according to their position and set properties.  
**[Random Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/RandomBrush.html)** | Select this brush to place random tiles onto a tilemap by selecting from defined **Tile Sets** while painting onto the tilemap.  
**[Line Brush](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/LineBrush.html)** | Select this brush to draw a line of tiles onto a tilemap.  
Refer to the [Scriptable Brushes](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest/index.html?subfolder=/manual/Brushes.html)’ respective documentation for more information on their specific properties and usage.
Property | Description  
---|---  
**Script** | Displays the assigned script Asset that provides a fixed set of APIs for painting on tilemaps. The default is the [GridBrush](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.html). Users may use or create their own [Scriptable Brushes](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/brushes/create-scriptable-brush.html) which become available from the dropdown menu. The **Script** property updates to reflect the current active brush.  
**Flood Fill Contiguous Only** | Enable this property to have the **Flood Fill** tool only affect tiles on a tilemap which are both the same as the targeted tile and are contiguous to each other from the targeted position. When disabled, **Flood Fill** will change all tiles which are the same as the targeted tile on a tilemap regardless of their position. This only affects the **Default Brush**.  
**Lock Z Position** | Enable this property to change the z-position of the active brush. Disable to prevent any changes to the current z-position of the active brush.  
**Z Position** | Only available when **Lock Z Position** is disabled. Enter the desired z-axis value (only whole numbers) for this brush when painting tiles, which also adjusts the relative heights of tiles on a [Z as Y Isometric Tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html) . Refer to [Adjusting the Tile height in the Palette](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-tile-palette-isometric-tilemap.html) for more information.  
**Reset** | Select to reset the z-position value back to zero.  
## Tilemap Focus overlay
The **Tilemap Focus** overlay appears in the **Scene** view while the **Tile Palette** editor window is opened. Use the **Tilemap Focus** overlay to focus on a specific tilemap or grid by fading out other GameObjects in the **Scene** view. This helps to identify specific tilemaps if you are working with many tilemaps to avoid confusion and clutter. The **Tilemap Focus** overlay only affects the **Tile Palette** editor’s [Active Target](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-editor-reference.html#activetarget) tilemap.
## Additional resources
  * [Create a Tile Palette](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/create-tile-palette.html)
  * [2D Tilemap Extras package](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tile-palettes/tile-palette-preferences-reference.html)
Tile palette preferences reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/grid-reference.html)
Grid component reference
