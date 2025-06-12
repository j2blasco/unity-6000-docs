* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Tilemap Collider 2D


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-brush-shortcut-reference.html)
Isometric brush shortcut Reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
Tilemap component reference
# Tilemap Collider 2D
The **Tilemap**Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2D** component generates collider shapes for [tiles](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)A simple class that allows a sprite to be rendered on a Tilemap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tile) on a [Tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap) component on the same **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). When you add or remove tiles on the Tilemap component, the Tilemap Collider 2D updates the collider shapes during `LateUpdate`. It batches multiple tile changes together to minimize the impact on performance.
## Collider Type’s effect on collider generation
The collider shapes generated for each tile in the tilemap depend on the **Collider Type** set in the tile’s properties. For more information on how this component’s shape generation behavior corresponds to the **Collider Types** , refer to [Tile asset reference](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html).
## Tilemap and Composite Colliders
You can use the Tilemap Collider 2D component together with the [Composite Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/composite-collider/composite-collider-2d-reference.html) component. When you add both components to the same tilemap, Unity composites the collider shapes of neighboring tiles together. This smoothens the corners and edges between collider shapes in neighboring tiles.
Using both components together reduces the number of individual collider shapes involved in a physics update, which reduces the amount of calculations required, and minimizes the impact on performance.
## Tilemap collider 2D API
If you require immediate changes to happen to the collider, use [Tilemaps.TilemapCollider2D.ProcessTilemapChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TilemapCollider2D.ProcessTilemapChanges.html) to process them immediately. You can use [Tilemaps.TilemapCollider2D-hasTilemapChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TilemapCollider2D-hasTilemapChanges.html) to check if any processing is required.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-brush-shortcut-reference.html)
Isometric brush shortcut Reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
Tilemap component reference
