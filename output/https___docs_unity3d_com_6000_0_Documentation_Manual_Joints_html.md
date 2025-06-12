* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
  * Introduction to joints


[](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
Joints
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html)
Character Joint component reference
# Introduction to joints
A **joint** connects a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) to another Rigidbody or to a fixed point in space. Joints apply forces that move rigid bodies, and joint limits restrict that movement. Joints give Rigidbody components the following degrees of freedom:
![A diagram of the degrees of freedom for Rigidbody components. The y-axis controls linear up and down movement, the x-axis controls linear back and forward movement, and the z-axis controls linear left and right movement.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/DegreesOfFreedom.png) A diagram of the degrees of freedom for Rigidbody components. The y-axis controls linear up and down movement, the x-axis controls linear back and forward movement, and the z-axis controls linear left and right movement.
For details on joints in the PhysX system, including how twist and swing axes work, refer to [NVidia PhysX documentation: Joints](https://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/Manual/Joints.html).
Unity provides the following joint components that apply different forces and limits to Rigidbody components, and give those bodies different motion:
**Property** | **Function**  
---|---  
[Character Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html)An extended ball-socket joint which allows a joint to be limited on each axis. Mainly used for Ragdoll effects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CharacterJoint) | Emulates a ball and socket joint, like a hip or shoulder. Constrains rigid body movement along all linear degrees of freedom, and enables all angular freedoms. Rigidbody components attached to a Character Joint orient around each axis and pivot from a shared origin.  
[Configurable Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)An extremely customizable joint that other joint types are derived from. It can be used to create anything from adapted versions of existing joints to custom designed and highly specialized joints. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ConfigurableJoint) | Emulates any skeletal joint, like those in a ragdoll. You can configure this joint to force and restrict rigid body movement in any degree of freedom.  
[Fixed Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FixedJoint.html)A joint type that is completely constrained, allowing two objects to be held together. Implemented as a spring so some motion may still occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FixedJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FixedJoint) | Restricts the movement of a rigid body to follow the movement of the rigid body it is attached to. This is useful when you need rigid bodies that easily break apart from each other, or you want to connect the movement of two rigid bodies without parenting in a [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) hierarchy.  
[Hinge Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HingeJoint.html)A joint that groups together two Rigidbody components, constraining them to move like they are connected by a hinge. It is perfect for doors, but can also be used to model chains, pendulums and so on. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HingeJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HingeJoint) | Attaches a rigid body to another rigid body or a point in space at a shared origin and allows the rigid bodies to rotate around a specific axis from that origin. Useful for emulating doors and finger joints.  
[Spring Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpringJoint.html)A joint type that connects two Rigidbody components together but allows the distance between them to change as though they were connected by a spring. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpringJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpringJoint) | Keeps rigid bodies apart from each other but lets the distance between them stretch slightly. The spring acts like a piece of elastic that tries to pull the two anchor points together to the exact same position.  
2D joints have **2D** at the end of the name (for example, [Hinge Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-reference.html)). For a summary of the 2D joints , see [Joints 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html) documentation.
Joints also have other options that you can enable for specific effects. For example, you can set a joint to break when a Rigidbody applies a force to it that exceeds a certain threshold. Some joints allow a **drive force** to occur between the connected Rigidbody components to set them in motion automatically.
**Note:** If you want to build kinematic chains in the context of an industrial application, for example to simulate a robotic arm with realistic physics behavior, you should use [physics articulations](https://docs.unity3d.com/6000.0/Documentation/Manual/physics-articulations.html) instead of the regular joints hereby described.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
Joints
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html)
Character Joint component reference
