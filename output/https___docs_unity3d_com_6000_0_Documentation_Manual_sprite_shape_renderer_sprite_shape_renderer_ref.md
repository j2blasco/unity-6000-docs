* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite shape renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/shape-renderer-landing.html)
  * Sprite shape renderer reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/mask-interaction.html)
Mask interaction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
Tilemaps in Unity
# Sprite shape renderer reference
Property | Function  
---|---  
**Color** | Define the vertex color of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) Shape geometry, which tints or recolors the Sprite Shape. Use the color picker to set the vertex. See the [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/color.html) section below this table for examples.  
**Mask Interaction** | Set how the Sprite Renderer behaves when it interacts with a [Sprite Mask](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)A texture which defines which areas of an underlying image to reveal or hide. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteMask) . Refer to examples of the different options in the [Mask Interaction](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/mask-interaction.html) section below. 
  * **None** : The Sprite Shape Renderer does not interact with any Sprite Masks in the Scene. This is the default option.
  * **Visible Inside Mask** : The Sprite Shape is visible where the Sprite Mask overlays it, but not outside of it.
  * **Visible Outside Mask** : The Sprite Shape is visible outside of the Sprite Mask, but not inside it. The Sprite Mask hides the sections of the Sprite Shape it overlays.

  
**Sorting Layer** | Set the [Sorting Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html) of the Sprite Shape geometry, which controls its priority during rendering. Select an existing Sorting Layer from the drop-down box, or create a new Sorting Layer.  
**Order In Layer** | Set the render priority of the Sprite Shape within its [Sorting Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html). Lower numbered Sprite Shapes are rendered first, with higher numbered Sprite Shapes overlapping those below.  
SpriteShapeRenderer
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/mask-interaction.html)
Mask interaction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
Tilemaps in Unity
