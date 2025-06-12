* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * Wheel colliders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)
Mesh collider component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-introduction.html)
Introduction to Wheel colliders
# Wheel colliders
The **Wheel**collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider)** is a collider for grounded vehicles. It has built-in **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels.
Unity’s PhysX integration uses the PhysX 4.1 Vehicles SDK to simulate the wheel assembly of ground vehicles (that is, the wheels, suspension, and braking). This documentation covers how to interact with this SDK in Unity; for details of the SDK itself, see the [PhysX 4.1 Vehicles SDK documentation](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Index.html).
You don’t need to understand how a real-world vehicle works to build a simple simulation. However, an understanding of the main elements such as suspension and wheel behavior can help you work more precisely with the different vehicle simulation properties available in Unity.
**Topic** | **Description**  
---|---  
[Introduction to wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-introduction.html) | Overview of the concepts and fundamental behaviors of the **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) class and component. This section includes information on how Unity implements **Wheel colliders** A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WheelCollider) to simulate ground wheel movement, and how to work with Wheel colliders in the Editor. |   
[Wheel collider friction](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-friction.html) | How Unity simulates friction between the Wheel collider and the surface it travels across.  
[Wheel collider suspension](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-suspension.html) | How Unity simulates a suspension system via the Wheel collider’s position and behavior.  
[Create a vehicle with Wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/WheelColliderTutorial.html) | Build a ground vehicle with Wheel colliders. This step-by-step walkthrough provides demonstration assets and code samples.  
[Wheel collider component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html) | Reference page for the Wheel collider component.  
## Additional resources
  * [Nvidia PhysX 4.1 Vehicles SDK documentation](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Index.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)
Mesh collider component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-introduction.html)
Introduction to Wheel colliders
