* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Effectors 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/effectors-2d-landing.html)
  * Buoyancy Effector 2D reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/area-effector-2d-reference.html)
Area Effector 2D reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/point-effector-2d-reference.html)
Point Effector 2D reference
# Buoyancy Effector 2D reference
The Buoyancy Effector 2D defines simple fluid behaviour such as floating and the drag and flow of fluid. You can also control a fluid surface, with the fluid behaviour taking place below.
## Properties
**Property** | **Function**  
---|---  
**Use**Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) Mask** | Check this box to enable the ‘Collider Mask’ property. If this is not enabled, the Global **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) Matrix will be used as the default for all Collider 2Ds.  
**Collider Mask** | The mask used to select specific Layers allowed to interact with the effector. Note that this option only displays if you have selected **Use Collider Mask**.  
**Surface Level** | Defines the surface location of the buoyancy fluid. When a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) is above this line, no buoyancy forces are applied. When a GameObject is intersecting or completely below this line, buoyancy forces are applied. This is a location specified as a world-space offset along the world y-axis, but is also scaled by the GameObject’s **Transform** component.  
**Density** | The density of the fluid. Colliders with a higher density sink, those with a lower density float, and those with the same density appear suspended in the fluid.  
**Linear Drag** | The drag coefficient affecting positional movement of a GameObject. This only applies when inside the fluid.  
**Angular Drag** | The drag coefficient affecting rotational movement of a GameObject. This only applies when inside the fluid.  
**Flow Angle** | The world-space angle (in degrees) for the direction of fluid flow. Fluid flow applies buoyancy forces in the specified direction.  
**Flow Magnitude** | The “power” of the fluid flow force. Combined with **Fluid Angle** , this specifies the level of buoyancy force applied to GameObjects inside the fluid. The magnitude can also be negative, in which case the buoyancy forces are applied at 180 degrees to the **Flow Angle.**  
**Flow Variation** | Enter a value here to randomly vary the fluid forces. Specify a positive or negative variation to randomly add or subtract from the **Fluid Magnitude**.  
BuoyancyEffector2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/area-effector-2d-reference.html)
Area Effector 2D reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/point-effector-2d-reference.html)
Point Effector 2D reference
