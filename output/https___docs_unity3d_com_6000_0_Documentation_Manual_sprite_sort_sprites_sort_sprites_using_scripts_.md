* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprites sorting order](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites-landing.html)
  * Sort sprites using scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites.html)
Sort sprites
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sprites-sorting-reference.html)
Sprites sorting reference
# Sort sprites using scripts
You can sort **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) per **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) through **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), by modifying the following properties in Camera:
  * [TransparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortMode.html) (corresponds with **Transparency Sort Mode**)
  * [TransparencySortAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortAxis.html) (corresponds with **Transparency Sort Axis**)


For example:
```
var camera = GetComponent<Camera>();

camera.transparencySortMode = TransparencySortMode.CustomAxis;

camera.transparencySortAxis = new Vector3(0.0f, 1.0f, 0.0f);

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sort-sprites.html)
Sort sprites
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sort-sprites/sprites-sorting-reference.html)
Sprites sorting reference
