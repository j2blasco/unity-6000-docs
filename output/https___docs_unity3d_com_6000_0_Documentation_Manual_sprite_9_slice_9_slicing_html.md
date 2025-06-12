* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/9-slice/9-slicing.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Various image sizes without multiple assets](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/9-slice/9-slice-landing.html)
  * 9-slicing


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/9-slice/9-slice-landing.html)
Various image sizes without multiple assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/9-slice/set-sprite-9slicing.html)
Set up your sprite for 9-slicing
# 9-slicing
9-slicing is a 2D technique which allows you to reuse an image at various sizes without needing to prepare multiple [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset). It involves splitting the image into nine portions, so that when you re-size the [Sprite](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite), the different portions scale or tile (that is, repeat in a grid formation) in different ways to keep the Sprite in proportion. This is useful when creating patterns or [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture), such as walls or floors in a 2D environment.
This is an example of a 9-sliced Sprite, split into nine sections. Each section is labelled with a letter from A to I.
![Example of a 9-sliced sprite.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/9-slice-0.png) Example of a 9-sliced sprite.
The following points describe what happens when you change the dimensions of the image:
  * The four corners (A, C, G and I) do not change in size.
  * The B and H sections stretch or tile horizontally.
  * The D and F sections stretch or tile vertically.
  * The E section stretches or tiles both horizontally and vertically.


This section describes how to set 9-slicing up, and which settings to apply depending on whether you want to stretch or tile the areas shown above.
### Limitations and known issues
  * The only two Collider2Ds that support 9-slicing are BoxCollider2D and PolygonCollider2D.
  * You cannot edit BoxCollider2D or PolygonCollider2D when the **Sprite Renderer** A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteRenderer)’s **Draw Mode** is set to **Sliced** or **Tiled**. Editing in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window is disabled, and a warning appears to notify you that the Collider2D cannot be edited because it is driven by the Sprite Renderer component’s tiling properties.
  * When the shape is regenerated in **Auto Tiling** , additional edges might appear within the Collider2D’s shape. This may have an effect on **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/9-slice/9-slice-landing.html)
Various image sizes without multiple assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/9-slice/set-sprite-9slicing.html)
Set up your sprite for 9-slicing
