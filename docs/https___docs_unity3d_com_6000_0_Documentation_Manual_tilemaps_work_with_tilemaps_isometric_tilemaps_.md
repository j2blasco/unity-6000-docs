* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-isometric-sprites-sprite-atlas.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * [Isometric tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)
  * [Tilemap Renderer for Isometric Tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-landing.html)
  * Sort isometric Sprites with the Sprite Atlas


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
Tilemap Renderer isometric modes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-sprites-custom-sorting-axis.html)
Sort Sprites with a Custom Sorting Axis
# Sort isometric Sprites with the Sprite Atlas
In **Chunk Mode** , the **Tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap) Renderer isn’t able to sort Tiles from multiple textures individually and doesn’t render the tile **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) consistently.
![The Scene view with an example of isometric tile rendering issues.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2D_IsoTilemap_10.png) The Scene view with an example of isometric tile rendering issues.
Pack all the individual Sprites that make up the Tilemap into a single [Sprite Atlas](https://docs.unity3d.com/Manual/SpriteAtlas.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas) to solve this issue. To do this:
  1. Create a **Sprite Atlas** from the Assets menu (go to: **Atlas > Create > Sprite Atlas**).
  2. Add the Sprites to the Sprite Atlas by dragging them to the **Objects for Packing** list in the Atlas’ **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
![Objects for packing list](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2D_IsoTilemap_11.png) **Objects for packing** list
  3. Click **Pack Preview**. Unity packs the Sprites into the Sprite Atlas during Play mode, and correctly sorts and renders them. This is only visible in the Editor during Play mode.
![Isometric tilemap](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2D_IsoTilemap_12.png) Isometric tilemap


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html)
Tilemap Renderer isometric modes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/sort-sprites-custom-sorting-axis.html)
Sort Sprites with a Custom Sorting Axis
