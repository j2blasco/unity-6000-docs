* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-other-events.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider interactions](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions.html)
  * Use collisions to trigger other events


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions.html)
Collider interactions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-interaction.html)
Interaction between collider types
# Use collisions to trigger other events
When two **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) make contact, they call functions that you can use to trigger other events in your project. You can place any code you like in these functions to respond to the **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) event.
Collider events require configuration via C# script; you cannot configure them using only the user interface. 
There are two collider event types: 
  * Collision events: Collision events occur when two colliders make contact, and neither collider has **Is Trigger** enabled. The most common collision functions are [`Collider.OnCollisionEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html), [`Collider.OnCollisionStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionStay.html), and [`Collider.OnCollisionExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionExit.html).
  * Trigger events: Trigger events occur when two colliders make contact, at least one collider has **Is Trigger** enabled, and at least one collider has a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) or ArticulationBody. The most common trigger functions are [`Collider.OnTriggerEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html), [`Collider.OnTriggerStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerStay.html), and [`Collider.OnTriggerExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html).


A collider that has **Is Trigger** enabled is called a **trigger collider**. Trigger colliders do not physically collide with other colliders; instead, they create a space that sends an event when other colliders pass through it.
Note: The 2D physics system has equivalent functions with **2D** appended to the name (for example, `OnCollisionEnter2D`). For details of these 2D functions, refer to the [`MonoBehaviour`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) API class documentation.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions.html)
Collider interactions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-interaction.html)
Interaction between collider types
