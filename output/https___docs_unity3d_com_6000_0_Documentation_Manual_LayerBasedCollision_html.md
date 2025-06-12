* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LayerBasedCollision.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)
  * Layer-based collision detection


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-layers.html)
Create functional layers in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
Layers and layerMasks
# Layer-based collision detection
Layer-based **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection is a way to make a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) collide with another GameObject that’s set up on a specific layer or layers.
![Layer Collision Matrix selected in the Project Settings window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/layer-collision-matrix.png) Layer Collision Matrix selected in the Project Settings window.
The Layer Collision Matrix defines which GameObjects can collide with which Layers. To open the Layer Collision Matrix go to **Edit > Project Settings > Physics**.
In the image, the Layer Collision Matrix is set up so that only GameObjects that belong to the same layer can collide: 
  * Layer 1 is checked for Layer 1 only
  * Layer 2 is checked for Layer 2 only
  * Layer 3 is checked for Layer 3 only


If, for example, you want Layer 1 to collide with Layer 2 and 3, but not with Layer 1, find the row for **Layer 1** , then check the boxes for the **Layer 2** and **Layer 3** columns, and leave the **Layer 1** column checkbox blank.
## Set up layer-based collision detection
  1. Select the GameObject you want to assign a layer to.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), select the **Layer** dropdown at the top, and either choose a Layer or add a new Layer. Repeat for each GameObject until you have finished assigning your GameObjects to Layers.
![Cube selected in the Inspector, with Layer 1 assigned to it.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/layer-collision-selection.png) Cube selected in the Inspector, with Layer 1 assigned to it.
  3. In the Unity menu bar, go to **Edit** > **Project Settings** , then select the **Physics** category to open the [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsManager.html) window.
  4. Select the layers on the Collision Matrix that you want to interact with the other layers.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-layers.html)
Create functional layers in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layers-and-layermasks.html)
Layers and layerMasks
