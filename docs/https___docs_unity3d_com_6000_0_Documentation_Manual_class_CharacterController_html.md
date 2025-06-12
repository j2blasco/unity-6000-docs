* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Character control](https://docs.unity3d.com/6000.0/Documentation/Manual/character-control-section.html)
  * Character Controller component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CharacterControllers.html)
Introduction to character control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)
Rigidbody physics
# Character Controller component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html "Go to CharacterController page in the Scripting Reference")
The **Character Controller** is mainly used for third-person or first-person player control that does not make use of **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) physics.
![The Character Controller inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Inspector-CharacterController.png) The Character Controller inspector
## Properties
**Property** | **Description**  
---|---  
**Slope Limit** | Limits the collider to only climb slopes that are less steep (in degrees) than the indicated value.  
**Step Offset** | The character will step up a stair only if it is closer to the ground than the indicated value. This should not be greater than the Character Controller’s height or it will generate an error.  
**Skin width** | Two colliders can penetrate each other as deep as their Skin Width. Larger Skin Widths reduce jitter. Low Skin Width can cause the character to get stuck. A good setting is to make this value 10% of the Radius.  
**Min Move Distance** | If the character tries to move below the indicated value, it will not move at all. This can be used to reduce jitter. In most situations this value should be left at 0.  
**Center** | This will offset the Capsule Collider in world space, and won’t affect how the Character pivots.  
**Radius** | Length of the Capsule Collider’s radius. This is essentially the width of the collider.  
**Height** | The Character’s **Capsule Collider** A capsule-shaped collider component that handles collisions for GameObjects like barrels and character limbs. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#capsulecollider) height. Changing this will scale the collider along the Y axis in both positive and negative directions.  
![The Character Controller](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CharacterControllerWindow.jpg) The Character Controller
## Details
The traditional Doom-style first person controls are not physically realistic. The character runs 90 miles per hour, comes to a halt immediately and turns on a dime. Because it is so unrealistic, use of Rigidbodies and physics to create this behavior is impractical and will feel wrong. The solution is the specialized Character Controller. It is simply a capsule shaped **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) which can be told to move in some direction from a script. The Controller will then carry out the movement but be constrained by **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision). It will slide along walls, walk up stairs (if they are lower than the **Step Offset**) and walk on slopes within the **Slope Limit**.
The Controller does not react to forces on its own and it does not automatically push Rigidbodies away.
If you want to push Rigidbodies or objects with the Character Controller, you can apply forces to any object that it collides with via the **OnControllerColliderHit()** function through scripting.
On the other hand, if you want your player character to be affected by physics then you might be better off using a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html) instead of the Character Controller.
### Fine-tuning your character
You can modify the **Height** and **Radius** to fit your Character’s **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). It is recommended to always use around 2 meters for a human-like character. You can also modify the **Center** of the capsule in case your pivot point is not at the exact center of the Character.
**Step Offset** can affect this too, make sure that this value is between 0.1 and 0.4 for a 2 meter sized human.
**Slope Limit** should not be too small. Often using a value of 90 degrees works best. The Character Controller will not be able to climb up walls due to the capsule shape.
### Don’t get stuck
The **Skin Width** is one of the most critical properties to get right when tuning your Character Controller. If your character gets stuck it is most likely because your **Skin Width** is too small. The **Skin Width** will let objects slightly penetrate the Controller but it removes jitter and prevents it from getting stuck.
It’s good practice to keep your **Skin Width** at least greater than 0.01 and more than 10% of the **Radius**.
We recommend keeping **Min Move Distance** at 0.
See the Character Controller script reference [here](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)
## Hints
  * Try adjusting your **Skin Width** if you find your character getting stuck frequently.
  * The Character Controller can affect objects using physics if you write your own **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
  * The Character Controller can not be affected by objects through physics.
  * Note that changing Character Controller properties in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) will recreate the controller in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), so any existing Trigger contacts will get lost, and you will not get any OnTriggerEntered messages until the controller is moved again.
  * The Character Controller’s capsule used in queries such as raycast might shrink by a small factor. Queries therefore could miss in some corner cases, even when they appear to hit the Character Controller’s **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CharacterControllers.html)
Introduction to character control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)
Rigidbody physics
