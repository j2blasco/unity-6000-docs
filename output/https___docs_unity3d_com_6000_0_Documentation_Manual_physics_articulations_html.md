* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/physics-articulations.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Articulations](https://docs.unity3d.com/6000.0/Documentation/Manual/articulations-section.html)
  * Introduction to physics articulations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/articulations-section.html)
Articulations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html)
Articulation Body component reference
# Introduction to physics articulations
A physics articulation is a set of [Articulation Bodies](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html) organized in a logical tree, in which each parent-child relationship reflects mutually constrained relative motion.
The main purpose of physics articulations is to provide a realistic physics behavior for commercial and industrial non-gaming applications that involve **joints** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint). For example, they make it a lot easier than the [regular Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html) to simulate robotic arms and kinematic chains.
## Articulation setup vs. regular joints
In the most basic scenario to get two physical bodies linked with a single joint, you can either build an articulation or use regular joints, as described in the following table.
**Unity component** | **Articulation setup** | **Setup with regular joint**  
---|---|---  
**Hierarchy** | 
  * GameObject + Articulation Body
    * GameObject + Articulation Body

| 
  * GameObject + Rigid Body
  * GameObject + Rigid Body + Joint

  
**Relationship** | The GameObjects have a hierarchical relationship (parent-child).  
**Note:** The physics engine uses the Unity transform hierarchy to express the parent-child relationship. | The GameObjects don’t necessarily have a hierarchical relationship.  
**Note:** In more advanced scenarios, you can freely simulate kinematic loops.  
**Physical bodies** | Both **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) have an Articulation Body component, which defines physical body properties (among others). | Both GameObjects have a **RigidBody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) component, which defines physical body properties (among others).  
**Joint** | The Articulation Body of the child GameObject holds the joint properties, where you can select the joint type. | One of the GameObjects also has a Joint component. The joint properties depend on the type of Joint component that you add.  
However, the overall resulting behavior is not the same in both cases, especially if you extend this principle to multiple physical bodies and joints.
If you try to use regular joints to model kinematic chains such as in a rag doll, robotic arm, or mechanism with several concurrent hinges, the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) might encounter unsolvable scenarios and leave certain constraints unsatisfied. This might result in stuttery and unrealistic motion. Not only would the joints look peculiar, but it would also be impossible to use them for simulating a real device, impeding efforts to model or prototype industrial designs.
## Building an Articulation in Unity
To build a physics articulation in Unity, you must add an Articulation Body component to each GameObject that the articulation consists of. Each Articulation Body component allows you to configure in one single place:
  * The physical body properties of the corresponding GameObject. Basically, its mass and the way it responds to the physics environment.
  * The type and properties of the joint that links the GameObject to its parent GameObject (except for the root of the articulation).


The following example shows a simple physics articulation that involves 3 physical bodies and 2 joints:
![Physics articulation with three physical bodies and two joints.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/physics-articulation-concept.png) Physics articulation with three physical bodies and two joints.
To build such an articulation in Unity:
  1. Create a linear hierarchy of 3 GameObjects.
  2. Add an Articulation Body component to each of these 3 GameObjects.
  3. Configure each Articulation Body component (according to the above graphic):

**GameObject** | **Articulation Body component configuration**  
---|---  
**A** (root) | You can only define physical body properties for GameObject A.  
**B** | You can define:  

  * Physical body properties for GameObject B.
  * The type and properties of the joint with GameObject A.

  
**C** | You can define:  

  * Physical body properties for GameObject C.
  * The type and properties of the joint with GameObject B.

  
**Note:** By definition, an articulation can only have one root and is not allowed to have kinematic loops. If you need kinematic loops, use [regular joints](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html).
**Limitation:** If you want to build very long articulation chains, you must still be aware that Unity supports a maximum hierarchy depth of 64 GameObjects.
## Articulation Joint types and degrees of freedom
There are four types of articulation joints that you can select and configure through an Articulation Body:
  * ****Fixed joint** A joint type that is completely constrained, allowing two objects to be held together. Implemented as a spring so some motion may still occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FixedJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FixedJoint)**: sets a rigid, unbreakable and unstretchable link between bodies.
  * **Prismatic joint** : prevents all motion except sliding along a particular axis.
  * **Revolute joint** : allows rotation around a particular axis (like a hinge).
  * **Spherical joint** : anatomical joint, which allows two swings and one twist.


All locked degrees of freedom in an articulation are unbreakable and unstretchable by design. To achieve this, the physics engine uses the reduced coordinate space, where bodies only have coordinates about unlocked axes of motion.
In contrast, for the regular iterative joints, the physics engine enforces the maximal coordinate space, which only guarantees the satisfaction of constraints if the solver is able to converge after a set of iterations.
## Physics articulation demo
Check out Unity’s [robotics demo project](https://github.com/Unity-Technologies/articulations-robot-demo) to experiment with a serial link robot arm with articulation joints.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/articulations-section.html)
Articulations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html)
Articulation Body component reference
