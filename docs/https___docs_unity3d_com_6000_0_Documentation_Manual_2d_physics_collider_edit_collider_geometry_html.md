* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/edit-collider-geometry.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/collider-2d-landing.html)
  * Edit the collider's geometry


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
Use a Custom Collider 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/edit-collider-mode-reference.html)
Edit Collider mode reference
# Edit the collider’s geometry
You can edit a **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider)’s geometry manually or have Unity generate its shape automatically.
Unity automatically generates a collider’s geometry when you drag a **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) into the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and add a Collider 2D component to it. The generated collider shape matches the outline of the sprite as close as possible.
To edit the collider’s shape:
  1. Select **Edit Collider** ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/edit-collider-inspector-icon.png) in the Inspector window to edit the collider’s geometry. You can also access the collider’s editing mode from the Tools overlay in the Scene view window.  
![The Edit Collider icon located at the bottom of the Tools overlay.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/edit-collider-overlay.png)
  2. To move an existing vertex, select and hold it, then move it to a new location.
  3. To create a new vertex, hover your cursor over the outline of the collider’s shape. A dot shows the position of the cursor on the collider’s geometry. Click on the dot to create a new vertex at that position.
  4. To remove a vertex, hold Ctrl (macOS:Cmd) while hovering your cursor over the edges of the collider’s geometry, which turn red. Click the red edges to remove the vertex that connects them.
  5. Exit the collider editing mode by selecting **Edit Collider** in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window or Tools overlay again.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/custom-collider/use-custom-collider-2d.html)
Use a Custom Collider 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/edit-collider-mode-reference.html)
Edit Collider mode reference
