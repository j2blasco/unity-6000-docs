* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
  * Character Joint component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)
Introduction to joints
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FixedJoint.html)
Fixed Joint component reference
# Character Joint component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint.html "Go to CharacterJoint page in the Scripting Reference")
A Character **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) is an extended ball-socket joint that allows you to limit the joint on each axis. 
Character Joints are useful for ragdoll effects. For information about setting up a ragdoll, refer to [Ragdoll Wizard](https://docs.unity3d.com/6000.0/Documentation/Manual/wizard-RagdollWizard.html). 
Note: For **Character Joints** made with the Ragdoll wizard, the twist axis corresponds with the limb’s largest **swing axis** , the Swing 1 axis corresponds with the limb’s smaller swing axis, and the Swing 2 axis is for twisting the limb.
## Properties
**Property:** | **Function:**  
---|---  
**Edit Angular Limits** | Adds a visual **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) to the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view that helps you edit joint angular limits. To use this gizmo, set the **Angular X, Y, Z Motion** to **Limited** and then handles appear for you to drag and adjust the joint’s rotational space.  
**Connected Body** | Optional reference to the **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) that the joint is dependent upon. If you do not assign a **Connected Body** or **Connected Articulation Body** , the joint connects to the world.  
**Connected Articulation Body** | Optional reference to the ArticulationBody that the joint is dependent upon. If not set, the joint connects to the world.  
**Anchor** | The point in the ****GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s** local space where the joint rotates around.  
**Axis** | Define the twist axis (visualized with the orange gizmo cone).  
**Auto Configure Connected Anchor** | If this is enabled, then Unity calculates the Connected Anchor position automatically to match the global position of the anchor property. This is the default behavior. If this is disabled, you can configure the position of the connected anchor manually.  
**Connected Anchor** | Manually configure the connected anchor position.  
**Swing Axis** | The swing axis. Visualized with the green gizmo cone.  
**Twist Limit Spring** | The elasticity of the limit along the Twist axis. Set this value to zero to make the limit impassable. A value other than zero makes the limit elastic. Refer to the [Limit Spring properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html#limit-springs) section for information on the properties available.  
****Low Twist Limit**** | Specify a lower limit to the twist axis in degrees, relative to the starting position. Refer to the [Limit properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html#limits) section for information on the properties available.  
****High Twist Limit**** | Specify an upper limit to the twist axis in degrees, relative to the starting position. Refer to the [Limit properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html#limits) section for information on the properties available.  
****Swing Limit** Spring** | The elasticity of the limit along the Swing axis. Set this value to zero to make the limit impassable. A value other than zero makes the limit elastic. Refer to the [Limit Spring properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html#limit-springs) section for information on the properties available.  
**Swing 1 Limit** | Limits the rotation around the swing axis (visualized with the green axis on the gizmo). Refer to the [Limit properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html#limits) section for information on the properties available.  
**Swing 2 Limit** | Limits the rotation around the swing 2 axis. The **Swing 2 Limit** axis isn’t visualized on the gizmo, but the axis is orthogonal to the two other axes (that is, the twist axis visualized in orange on the gizmo, and the **Swing 1 Limit** visualized in green on the gizmo). Refer to the [Limit properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html#limits) section for information on the properties available..  
**Enable Projection** | This defines how the joint snaps back to its constraints when it unexpectedly moves beyond them, because the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) is unable to reconcile the current combination of forces within the simulation. The options are **None** and **Position and Rotation**.  
**Projection Distance** | The distance the joint must move beyond its constraints before the physics engine attempts to snap it back to an acceptable position.  
**Projection Angle** | The angle the joint must rotate beyond its constraints before the physics engine attempts to snap it back to an acceptable position.  
**Break Force** | The force that needs to be applied for this joint to break.  
**Break Torque** | The torque that needs to be applied for this joint to break.  
**Enable**Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision)** | When checked, this enables collisions between bodies connected with a joint.  
**Enable Preprocessing** | Disabling preprocessing helps to stabilize configurations that are otherwise not possible.  
**Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the Rigidbody, ranging from 0.00001 to infinity. This is useful when the joint connects two Rigidbodies of largely varying mass. The physics solver produces better results when the connected Rigidbodies have a similar mass. When your connected Rigidbodies vary in mass, use this property with the **Connect Mass Scale** property to apply fake masses to make them roughly equal to each other. This produces a high-quality and stable simulation, but reduces the physical behavior of the Rigidbodies.  
**Connected Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the connected Rigidbody, ranging from 0.00001 to infinity.  
## Limit Spring properties
The following limit spring properties are available for **Twist Limit Spring** and **Swing Limit Spring**.
Values apply to force for linear motion, and torque for rotational motion.
**Property** | **Function**  
---|---  
**Spring** | The elasticity of the limit. Set this value to zero to make the limit impassable. A value other than zero makes the limit elastic.  
**Damper** | The reduction of the spring in proportion to the speed of the joint’s movement. Set a value above zero to allow the joint to “dampen” oscillations which would otherwise carry on indefinitely.  
## Limit properties
The following limit properties are available for **Low Twist Limit** , **High Twist Limit** , **Swing 1 Limit** , and **Swing 2 Limit**.
Values apply to force for linear motion, and torque for rotational motion.
**Property** | **Function**  
---|---  
**Limit** | Set a value to define the limits of the movement for the swing or twist axes, relative to the starting position.   
  
- For the **swing axis** , the limit angle is symmetric; for example, a value of `30` sets a range between –30 and 30.  
- For the **twist axis** , the Limit for **Low Twist Limit** indicates the lower limit, and the Limit for the **High Twist Limit** indicates the higher limit. For example, a Limit of `-30` in **Low Twist Limit** and `60` in **High Twist Limit** limits the rotation around the twist axis (orange gizmo) between –30 and 60 degrees.  
**Bounciness** | Define how much bounce occurs when the objects reach the defined limits. A value of 0 does not bounce. A value of 1 bounces without any loss of energy.  
****Contact Distance**** | Define the distance within which the contacts persist. Use this property to avoid jitter.  
CharacterJoint
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)
Introduction to joints
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FixedJoint.html)
Fixed Joint component reference
