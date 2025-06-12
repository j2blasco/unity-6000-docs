* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom physics shape](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html)
  * Work with multiple outlines


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/move-edges.html)
Move edges
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/update-shape-collider-2d-meshes.html)
Update the shape of the collider 2D meshes
# Work with multiple outlines
A **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite)’s physics shape can contain multiple separate outlines. This is useful if only specific areas of a Sprite need a **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2D **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) for **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision). For example, you might want a character to only respond to collisions on specific areas of its Sprite as part of your game’s damage mechanic.
To create a new rectangular outline with four control points:
  1. Click and drag over any empty space in the Sprite Editor window.  
![A detail of the sprite editor with the mouse cursor drawing a rectangle area for a first outline.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2D-CustomPS-generatedoutline-multi1.png)
  2. Repeat this step to create additional outlines.  
![A detail of the sprite editor with a first rectangle outline already drawn and the mouse cursor drawing another one.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2D-CustomPS-generatedoutline-multi3.png)


You can refine each outline in the same way you would for a single Physics Shape outline.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/move-edges.html)
Move edges
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/update-shape-collider-2d-meshes.html)
Update the shape of the collider 2D meshes
