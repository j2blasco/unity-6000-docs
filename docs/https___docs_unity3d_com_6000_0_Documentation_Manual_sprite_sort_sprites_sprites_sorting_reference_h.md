* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sprites-sorting-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprites sorting order](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites-landing.html)
  * Sprites sorting reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
Sort sprites using scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)
Sprite Renderer
# Sprites sorting reference
There are four **Transparency Sort Mode** options available:
**Sort Mode** | **Description**  
---|---  
**Default** | Sorts based on whether the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s **Projection** mode is set to **Perspective** or **Orthographic**.  
**Perspective** | Sorts based on perspective view. Perspective view sorts sprites based on the distance from the Camera’s position to the **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite)’s center.  
**Orthographic** | Sorts based on orthographic view. Orthographic view sorts sprites based on the distance along the view direction.  
**Custom Axis** | Sorts based on the given axis set in **Transparency Sort Axis**.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
Sort sprites using scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)
Sprite Renderer
