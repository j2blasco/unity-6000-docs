* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/set-sort-point-sprite.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)
  * Set the sort point of a sprite


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/change-color-sprite.html)
Change the color of a sprite
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/sprite-renderer-reference.html)
Sprite Renderer reference
# Set the sort point of a sprite
This property is only available when the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) Renderer’s **Draw Mode** is set to **Simple**.
In a 2D project, the Main **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is set to [Orthographic Projection mode](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html) by default. In this mode, Unity renders sprites in the order of their distance to the camera, along the direction of the Camera’s view.
![Orthographic Camera: Side view \(top\) and Game view \(bottom\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2DSpriteRenderer_SortPoint.png) **Orthographic Camera:** Side view (top) and Game view (bottom)
By default, a Sprite’s **Sort Point** is set to its **Center** , and Unity measures the distance between the camera’s Transform position and the Center of the Sprite to determine their render order. 
To set to a different **Sort Point** from the Center, select the **Pivot** option. Edit the Sprite’s Pivot position in the [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html).
* * *
SpriteRenderer
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/change-color-sprite.html)
Change the color of a sprite
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/sprite-renderer-reference.html)
Sprite Renderer reference
