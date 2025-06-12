* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RagdollStability.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Ragdoll physics](https://docs.unity3d.com/6000.0/Documentation/Manual/ragdoll-physics-section.html)
  * Joint and Ragdoll stability


[](https://docs.unity3d.com/6000.0/Documentation/Manual/wizard-RagdollWizard.html)
Create a ragdoll
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html)
Cloth
# Joint and Ragdoll stability
This page provides tips for improving [Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) and [Ragdoll](https://docs.unity3d.com/6000.0/Documentation/Manual/wizard-RagdollWizard.html) stability.
  * Avoid small Joint angles of **Angular Y Limit** and **Angular Z Limit**. Depending on your setup, the minimum angles should be around 5 to 15 degrees in order to be stable. Instead of using a small angle, try setting the angle to zero. This locks the axis and provide a stable simulation.
  * Uncheck the Joint’s **Enable Preprocessing** property. Disabling preprocessing can help prevent Joints from separating or moving erratically if they are forced into situations where there is no possible way to satisfy the Joint constraints. This can occur if [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) components connected by Joints are pulled apart by static **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) geometry (for example, spawning a Ragdoll partially inside a wall).
  * Under extreme circumstances (such as spawning partially inside a wall or pushed with a large force), the joint solver is unable to keep the Rigidbody components of a Ragdoll together. This can result in stretching. To handle this, enable projection on the Joints using either [ConfigurableJoint.projectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConfigurableJoint-projectionMode.html) or [CharacterJoint.enableProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-enableProjection.html).
  * If Rigidbody components connected with Joints are jittering, open the [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsManager.html) window (**Edit** > **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings), then select the **Physics** category) and try increasing the **Default Solver Iterations** value to between 10 and 20.
  * If Rigidbody components connected with Joints are not accurately responding to bounces, open the [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsManager.html) window (**Edit** > **Project Settings** , then select the **Physics__category) and try increasing the** Default Solver Velocity Iterations__ value to between 10 and 20.
  * Never use direct Transform access with Kinematic Rigidbody components connected by Joints to other Rigidbody components. Doing so skips the step where PhysX computes internal velocities of corresponding Rigidbody components, making the solver provide unwanted results. A common example of bad practice is using direct Transform access in 2D projects to flip characters, by altering [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html) on the root bone of the rig. This behaves much better if you use [Rigidbody2D.MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MovePosition.html) and [Rigidbody2D.MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html) instead.
  * Avoid large differences in the masses between Rigidbody components connected by Joints. It’s okay to have one Rigidbody with twice as much mass as another, but when one mass is ten times larger than the other, the simulation can become jittery.
  * Try to avoid scaling different from 1 in the Transform containing Rigidbody or the Joint. The scaling might not be robust in all cases.
  * If Rigidbody components are overlapping when inserted into the world, and you cannot avoid the overlap, try lowering the [Rigidbody.maxDepenetrationVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxDepenetrationVelocity.html) to make the Rigidbody components exit each other more smoothly.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wizard-RagdollWizard.html)
Create a ragdoll
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html)
Cloth
