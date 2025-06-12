* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Rigidbody 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * [Kinematic Body Type](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-landing.html)
  * Kinematic Body Type reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
Kinematic Body Type fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/static/static-body-type-landing.html)
Static Body Type
# Kinematic Body Type reference
A Kinematic **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) 2D behaves like an immovable object (as if it has infinite mass) during **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision), and mass-related properties are not available with this **Body Type** Defines a fixed behavior for a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is affected by forces like gravity), Kinematic (the body moves under simulation, but and isn’t affected by forces like gravity) or Static (the body doesn’t move under simulation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BodyType).
## Kinematic Rigidbody 2D properties
**Property** | **Function**  
---|---  
**Body Type** | Select to set the movement behavior and **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2D interaction of this Rigidbody 2D’s component settings.  
**Dynamic** | Select to set this Rigidbody 2D to the [Dynamic](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/dynamic/dynamic-body-type-reference.html) Body Type, which is designed to move under simulation and has all Rigidbody 2D properties available. This is the default Body Type for a Rigidbody 2D.  
**Kinematic** | Select to set this Rigidbody 2D to the Kinematic Body Type, which is designed to move under simulation but only under very explicit user control.  
**Static** | Select to set this Rigidbody 2D to the [Static](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html) Body Type, which is designed to not move under simulation at all and behaves like an immovable object with infinite mass. Refer to [Body Type: Static](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/static/static-body-type-reference.html) for more information.  
**Material** | Set a common [physics material](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-material-2d-reference.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsMaterial) for all Collider 2Ds attached to this Rigidbody 2D. **Note:** A Collider 2D uses its own Material property if it has one set. If there is no Material specified here or in the Collider 2D, the default option is **None (Physics Material 2D)**. This uses a default Material which you can set in the [Physics 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Physics2DManager) window.  
**Simulated** | Enable **Simulated** to have the Rigidbody 2D and any attached Collider 2Ds and **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) 2Ds to interact with the physics simulation during runtime. If this is disabled, these components do not interact with the simulation. Refer to [Rigidbody 2D properties: Simulated](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-simulated-property.html), below for more information. This property is enabled by default.  
**Full Kinematic Contact** | Enable this property if you want the Rigidbody 2D to be able to collide with all other Rigidbody 2D **Body Types**. **Note** : When this property is disabled, the Kinematic Rigidbody 2D only collides with Dynamic Rigidbody 2Ds. See [Using Full Kinematic Contacts](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-reference.html#kinematiccontact) for more details.  
****Collision Detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CollisionDetection)** | Define how collisions between Collider 2Ds are detected.  
**Discrete** | Select this option to allow **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with Rigidbody 2Ds and Collider 2Ds to overlap or pass through each other during a physics update, if they are moving fast enough. Collision contacts are only generated at the new position.  
**Continuous** | Select this option to ensure GameObjects with Rigidbody 2Ds and Collider 2Ds do not pass through each other during a physics update. Instead, Unity calculates the first impact point of any of the Collider 2Ds, and moves the GameObject there. **Note:** This option takes more CPU time than **Discrete**.  
**Sleeping Mode** | Define how the GameObject “sleeps” to save processor time when it is at rest.  
**Never Sleep** | Select this option to have sleeping disabled. **Important:** This should be avoided where possible, as it can impact system resources.  
**Start Awake** | Select this to have the GameObject initially awake.  
**Start Asleep** | Select this to have the GameObject initially asleep but can be awaken by collisions.  
**Interpolate** | Define how the GameObject’s movement is interpolated between physics updates. **Note** : This is useful when motion tends to be jerky.  
**None** | Select this to not apply movement smoothing.  
**Interpolate** | Select this to smoothen movement based on the GameObject’s positions in previous frames.  
**Extrapolate** | Select this to smoothen movement is smoothed based on an estimate of its position in the next frame.  
**Constraints** | Define any restrictions on the Rigidbody 2D’s motion.  
**Freeze Position** | Stops the Rigidbody 2D moving in the X and Y world axes selectively.  
**Freeze Rotation** | Stops the Rigidbody 2D rotating around the Z world axis selectively.  
**Layer Overrides** | Expand for the Layer override settings.  
**Include Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should include, when deciding if a collision with another Collider2D should occur or not. Refer to [Rigidbody2D-includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-includeLayers.html) for more information.  
**Exclude Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should exclude, when deciding if a collision with another Collider 2D should occur or not. Refer to [Rigidbody2D-excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-excludeLayers.html) for more information.  
## Full Kinematic Contacts 
Enabling **Full Kinematic Contacts** enables a Kinematic Rigidbody 2D to collide with all Rigidbody 2D **Body Types**. This is similar to the behavior of a Dynamic Rigidbody 2D, except the Kinematic Rigidbody 2D is not moved by the physics system when contacting another Rigidbody 2D. Instead, it behaves like an immovable object with infinite mass.
When this property is disabled, a Kinematic Rigidbody 2D will only collide with Dynamic Rigidbody 2Ds and not the other **Body Types**. **Note** : Trigger Colliders are an exception to this rule. This means that no collision scripting callbacks ([OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionEnter2D.html), [OnCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionStay2D.html), [OnCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionExit2D.html)) will occur.
This can be inconvenient when you are using physics queries (such as [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)) to detect where and how a Rigidbody 2D should move, and when you require multiple Kinematic Rigidbody 2Ds to interact with each other. Enable **Use Full Kinematic Contacts** to make Kinematic Rigidbody 2D components interact in this way.
**Note** : **Use Full Kinematic Contacts** allows explicit position and rotation control of a Kinematic Rigidbody 2D, but still allows full collision callbacks. In a setup where you need explicit control of all Rigidbody 2Ds, use Kinematic Rigidbody 2Ds in place of Dynamic Rigidbody 2Ds to still have full collision callback support.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
Kinematic Body Type fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/static/static-body-type-landing.html)
Static Body Type
