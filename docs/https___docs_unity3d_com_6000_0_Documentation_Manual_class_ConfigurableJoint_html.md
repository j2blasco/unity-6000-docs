* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
  * [Create a configurable joint](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configurable-joint.html)
  * Configurable Joint component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html)
Configure driving forces on a Configurable Joint
[](https://docs.unity3d.com/6000.0/Documentation/Manual/articulations-section.html)
Articulations
# Configurable Joint component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConfigurableJoint.html "Go to ConfigurableJoint page in the Scripting Reference")
**Configurable**Joints** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint)** incorporate all the functionality of the other [joint types](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html) and provide greater control of character movement. They are particularly useful when you want to customize the movement of a ragdoll and enforce certain poses on your characters. You can also use them to adapt joints into highly specialized joints of your own design.
## Properties
**Property** | **Description**  
---|---  
**Edit Angular Limits** | Adds a visual **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) to the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view that helps you edit joint angular limits. To use this gizmo, set the **Angular X, Y, Z Motion** to **Limited** and then handles appear for you to drag and adjust the joint’s rotational space.  
**Connected Body** | The **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) object which the joint connects to. You can set this to **None** to indicate that the joint attaches to a fixed position in space rather than another Rigidbody.  
**Connected Articulation Body** | Optional reference to the ArticulationBody that the joint is dependent upon. If not set, the joint connects to the world.  
**Anchor** | The point which defines the center of the joint. All physics-based simulations use this point as the center in calculations.  
**Axis** | The local axis that defines the object’s natural rotation based on physics simulation.  
**Auto Configure Connected Anchor** | Enable this setting to automatically calculate the **Connected Anchor** position to match the global position of the anchor property. This is the default setting. Disable it to configure the position of the connected anchor manually.  
**Connected Anchor** | Manually configure the connected anchor position.  
**Secondary Axis** | The **Axis** and **Secondary Axis** define the local coordinate system of the joint. The third axis is orthogonal to the other two.  
**X, Y, Z Motion** | Set the movement along the X, Y or Z axes to be **Free** , completely **Locked** , or **Limited** according to the limit properties described below.  
**Angular X, Y, Z Motion** | Set the rotation around the X, Y or Z axes to be **Free** , completely **Locked** , or **Limited** according to the limit properties described below.  
**Linear Limit Spring** | Apply a spring force to pull the object back when it goes past the limit position:  

  * **Spring** : The spring force. Set this value to zero to make the limit impassable. A value other than zero makes the limit elastic.
  * **Damper** : The reduction of the spring force in proportion to the speed of the joint’s movement. Set a value above zero to allow the joint to “dampen” oscillations which would otherwise carry on indefinitely.

  
**Linear Limit** | Set a limit on the joint’s linear movement (that is, movement over distance rather than rotation), specified as a distance from the joint’s origin:  

  * **Limit** : The distance in world units from the origin to the limit.
  * **Bounciness** : Set a bounce force to apply to the object to push it back when it reaches the limit distance.
  * **Contact Distance** : The minimum distance tolerance between the joint position and the limit to enforce the limit. A high tolerance means the object is less likely to break past the limit when moving fast. However, this requires the physics simulation to consider the limit more often, which reduces performance slightly.

  
**Angular X Limit Spring** | Apply a spring torque to rotate the object back when it goes past the limit angle of the joint:  

  * **Spring** : The spring torque. Set this value to zero to make the limit impassable. Set a value other than zero to make the limit elastic.
  * **Damper** : The reduction of the spring torque in proportion to the speed of the joint’s rotation. Set a value above zero to allow the joint to “dampen” oscillations which would otherwise carry on indefinitely.

  
**Low Angular X Limit** | Lower limit on the joint’s rotation around the x-axis, specified as an angle from the joint’s original rotation:  

  * **Limit** : The limit angle.
  * **Bounciness** : Set a bounce torque to apply to the object when its rotation reaches the limit angle.
  * **Contact Distance** : The minimum angular tolerance (between the joint angle and the limit) at which the limit is enforced. A high tolerance violates the limit less often when the object is moving fast. However, this requires the physics simulation to consider the limit more often and reduces performance slightly.

  
**High Angular XLimit** | This is similar to the **Low Angular X Limit** property described above but it determines the upper angular limit of the joint’s rotation rather than the lower limit.  
**Angular YZ Limit Spring** | This is similar to the **Angular X Limit Spring** described above but applies to rotation around both the Y and Z axes.  
**Angular Y Limit** | This is similar to the **Angular X Limit** property described above but applies the limit to the y-axis and regards both the upper and lower angular limits as the same.  
**Angular Z Limit** | This is similar to the **Angular X Limit** property described above but applies the limit to the z-axis and regards both the upper and lower angular limits as the same.  
****Target Position**** | The target position that the joint’s drive force moves to.  
****Target Velocity**** | The desired velocity that the joint moves to the **Target Position** under the drive force.  
**X Drive** | Set the force that Unity uses to rotate the joint around its local x-axis by the **Position Spring** and **Position Damper** drive torques. The **Maximum Force** parameter limits the force. This property is only available if the **Rotation Drive Mode** property is set to **X & YZ**. For more information, refer to [Driving forces with Configurable Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html).  

  * **Position Spring** : The spring torque that Unity uses to rotate the joint from its current position towards its target position.
  * **Position Damper** : Reduces the amount of spring torque in proportion to the difference between the joint’s current velocity and its target velocity. This reduces the speed of the joint’s movement. Set a value above zero to allow the joint to dampen oscillations which would otherwise carry on indefinitely.
  * **Maximum Force** : Limits the amount of force that the drive can apply. To make the drive apply the force that it’s calculated, set this to a high value that the drive is unlikely to calculate.
  * **Use Acceleration** : Activate to make the drive an acceleration drive rather than a force drive.

  
**Y Drive** | This is similar to the **X Drive** described above but applies to the joint’s y-axis.  
**Z Drive** | This is similar to the **X Drive** described above but applies to the joint’s z-axis.  
**Target Rotation** | The orientation that the joint’s rotational drive rotates towards, specified as a [quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)Unity’s standard way of representing rotations as data. When writing code that deals with rotations, you should usually use the Quaternion class and its methods. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quaternion). The target rotation is relative to the body that the Joint is attached to, unless the Swap Bodies parameter is set, in which case it’s relative to the connected body’s anchor.  
**Target Angular Velocity** | The angular velocity that the joint’s rotational drive aims to achieve. The property is specified as a vector. The vector’s length specifies the rotational speed and whose direction defines the axis of rotation.  
**Rotation Drive Mode** | Set how Unity applies drive force to the object to rotate it to the target orientation. Set the mode to **X and YZ** , to apply the torque around the axes as specified by the **Angular X/YZ Drive** properties described below. If you use **Slerp** mode then the **Slerp Drive** properties determine the drive torque.  
**Angular X Drive** | This specifies how the drive torque rotates the joint around its local x-axis. This property is only available if the **Rotation Drive Mode** property described above is set to **X & YZ**. For more information, refer to [Driving forces with Configurable Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html).  

  * **Position Spring** : The spring torque that Unity uses to rotate the joint from its current position towards its target position.
  * **Position Damper** : Reduces the amount of spring torque in proportion to the difference between the joint’s current velocity and its target velocity. This reduces the speed of the joint’s movement. Set a value above zero to allow the joint to dampen oscillations which would otherwise carry on indefinitely.
  * **Maximum Force** : Limits the amount of force that the drive can apply. To make the drive apply the force that it’s calculated, set this to a high value that the drive is unlikely to calculate.
  * **Use Acceleration** : Activate to make the drive an acceleration drive rather than a force drive.

  
**Angular YZ Drive** | This is similar to the **Angular X Drive** described above but applies to both the joint’s Y and Z axes.  
**Slerp Drive** | This specifies how the drive torque rotates the joint around all local axes. The property is only available if the **Rotation Drive Mode** property described above is set to **Slerp**. For more information, refer to [Configure driving forces on a Configurable Joint](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html).   

  * **Position Spring** : The spring torque that Unity uses to rotate the joint from its current position towards its target position.
  * **Position Damper** : Reduces the amount of spring torque in proportion to the difference between the joint’s current velocity and its target velocity. This reduces the speed of the joint’s movement. Set a value above zero to allow the joint to dampen oscillations which would otherwise carry on indefinitely.
  * **Maximum Force** : Limits the amount of force that the drive can apply. To make the drive apply the force that it’s calculated, set this to a high value that the drive is unlikely to calculate.
  * **Use Acceleration** : Activate to make the drive an acceleration drive rather than a force drive.

  
**Projection Mode** | This defines how the joint snaps back to its constraints when it unexpectedly moves beyond them, because the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) is unable to reconcile the current combination of forces within the simulation. The options are **None** and **Position and Rotation**.  
**Projection Distance** | The distance the joint must move beyond its constraints before the physics engine attempts to snap it back to an acceptable position.  
**Projection Angle** | The angle the joint must rotate beyond its constraints before the physics engine attempts to snap it back to an acceptable position.  
**Configured in World Space** | Enable this property to calculate the values set by the various target and drive properties in world space instead of the object’s local space.  
**Swap Bodies** | Enable this property to swap the order in which the physics engine processes the Rigidbodies involved in the joint. This results in different joint motion but has no impact on Rigidbodies and anchors.  
**Break Force** | If a force larger than this value pushes the joint beyond its constraints then the joint is permanently “broken” and deleted. Break Force only breaks a joint when its axes are **Limited** or **Locked**. For more information, refer to [Customize movement constraint with Configurable Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-movement-constraint.html).  
**Break Torque** | If a torque larger than this value rotates the joint beyond its constraints then the joint is permanently “broken” and deleted. Break Torque can break a joint regardless of whether its axes are **Free** , **Limited** or **Locked**. For more information, refer to [Customize movement constraint with Configurable Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-movement-constraint.html).  
**Enable**Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision)** | Enable this property to let the object with the joint collide with the object it is connected to. If this is disabled, the joint and object pass through each other.  
**Enable Preprocessing** | If preprocessing is disabled then certain “impossible” configurations of the joint are kept more stable rather than drifting wildly out of control.  
**Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the Rigidbody, ranging from 0.00001 to infinity. This is useful when the joint connects two Rigidbodies of largely varying mass. The physics solver produces better results when the connected Rigidbodies have a similar mass. When your connected Rigidbodies vary in mass, use this property with the **Connect Mass Scale** property to apply fake masses to make them roughly equal to each other. This produces a high-quality and stable simulation, but reduces the physical behaviour of the Rigidbodies.  
**Connected Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the connected Rigidbody, ranging from 0.00001 to infinity.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html)
Configure driving forces on a Configurable Joint
[](https://docs.unity3d.com/6000.0/Documentation/Manual/articulations-section.html)
Articulations
