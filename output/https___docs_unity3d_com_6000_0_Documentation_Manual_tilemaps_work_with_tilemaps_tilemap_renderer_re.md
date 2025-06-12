* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Tilemap Renderer component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
Tilemap component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
Tilemap Collider 2D component reference
# Tilemap Renderer component reference
When you create a [tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/create-tilemap.html)A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap), Unity automatically attaches the **Tilemap Renderer** component to the tilemap **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) you created. You can determine how Unity renders tiles set on the tilemap by adjusting the following property settings of the Tilemap Renderer component.
## Properties
Property | Description  
---|---  
**Sort Order** | Select the direction that Unity sorts the tiles on the selected tilemap from.  
**Mode** | Select the rendering mode of the renderer.  
**Chunk** | Select this mode to have the renderer group tiles by their location and the textures used by their sprites, and then batch them together for rendering. Groups with the same textures can be dynamically batched together even if they’re out of locational sequence of each other (based on the direction selected for the renderer’s **Sort Order**).   
  
Select this mode for the best rendering performance with tilemaps.   
  
**Note:** This mode isn’t compatible with the [Scriptable Render Pipeline Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html).  
**Individual** | Select this mode to have the renderer render each tile individually, taking into account their location and position in the **Sort Order**. This mode enables the **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) on the tiles to interact with other renderers in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) or with a [Custom Sorting Axis](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/renderer/tilemap-renderer-isometric-modes.html).  
**SRP Batch** | Select this mode to make the Tilemap Renderer component compatible with the [Scriptable Render Pipeline Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html), once the compatibility requirements are also met. **Note:** This mode is only supported in the [Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html) version 15 onwards.   
  
This rendering mode groups tiles by their location and the textures used by their sprites, and then batch them together for rendering. Groups with the same textures will be dynamically batched together only if they’re in locational sequence of each other (based on the direction selected for the renderer’s **Sort Order**).  
**Detect Chunk Culling Bounds** | Select the way the renderer detects the [bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TilemapRenderer-chunkCullingBounds.html) used for the culling of [tilemap chunks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TilemapRenderer-chunkSize.html). These bounds expand the boundary of tilemap chunks to ensure that oversize sprites aren’t clipped during culling.  
**Auto** | The Renderer automatically inspects the Sprites used by the Tiles to determine the expanded culling bounds to use.  
**Manual** | The values used to extend the bounds for culling of the tilemap chunks are manually set instead of with the Editor’s automatic detection.  
**Chunk Culling Bounds** | This property is visible only when **Detect Chunk Culling Bounds** is set to **Manual**  
**XYZ** | Enter the values (in Unity units) to extend the culling bounds by.  
**Mask Interaction** | Set how the Tilemap Renderer behaves when it interacts with a [Sprite Mask](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)A texture which defines which areas of an underlying image to reveal or hide. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteMask).  
**None** | Select this option to have the Tilemap Renderer not interact with any Sprite Mask in the scene. This is the default option.  
**Visible Inside Mask** | Select this option to have the Tilemap Renderer only render areas of the tilemap that the Sprite Mask overlays.  
**Visible Outside Mask** | Select this option to have the Tilemap Renderer render the entire tilemap but subtract the areas that the Sprite Mask overlays.  
**Material** | Select the material used to render the sprite textures.  
### Additional Settings
Properties in the **Additional Settings** section of the tilemap renderer component.
Property | Description  
---|---  
**Sorting Layer** | Select an existing [Sorting Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html) from the **Sorting Layer** dropdown or create a new Sorting Layer for this tilemap.  
**Order in Layer** | Set the render priority of the tilemap within its Sorting Layer. Unity renders lower numbered layers first, and higher numbered layers overlap those below.  
## Additional resources
  * [TilemapRenderer class](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TilemapRenderer.html) (Scripting API)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)
Tilemap component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
Tilemap Collider 2D component reference
