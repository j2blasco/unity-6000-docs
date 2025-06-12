* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Physics2DModule.html

# UnityEngine.Physics2DModule
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
The Physics2d module implements 2D physics in Unity.
### Classes
Class | Description  
---|---  
[AnchoredJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnchoredJoint2D.html) | Parent class for all joints that have anchor points.  
[AreaEffector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D.html) | Applies forces within an area.  
[BoxCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) | Collider for 2D physics representing an axis-aligned rectangle.  
[BuoyancyEffector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuoyancyEffector2D.html) | Applies forces to simulate buoyancy, fluid-flow and fluid drag.  
[CapsuleCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider2D.html) | A capsule-shaped primitive collider.  
[CircleCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CircleCollider2D.html) | Collider for 2D physics representing an circle.  
[Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) | Parent class for collider types used with 2D gameplay.  
[Collision2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) | Collision details returned by 2D physics callback functions.  
[CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html) | A Collider that can merge other Colliders together.  
[ConstantForce2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConstantForce2D.html) | Applies both linear and angular (torque) forces continuously to the rigidbody each physics update.  
[CustomCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomCollider2D.html) | Represents a Collider2D that is configured by assigning PhysicsShape2D geometry to it via a PhysicsShapeGroup2D.  
[DistanceJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DistanceJoint2D.html) | Joint that keeps two Rigidbody2D objects a fixed distance apart.  
[EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html) | Collider for 2D physics representing an arbitrary set of connected edges (lines) defined by its vertices.  
[Effector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Effector2D.html) | A base class for all 2D effectors.  
[FixedJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FixedJoint2D.html) | Connects two Rigidbody2D together at their anchor points using a configurable spring.  
[FrictionJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrictionJoint2D.html) | Applies both force and torque to reduce both the linear and angular velocities to zero.  
[HingeJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint2D.html) | Joint that allows a Rigidbody2D object to rotate around a point in space or a point on another object.  
[Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html) | Parent class for joints to connect Rigidbody2D objects.  
[Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html) | Global settings and helpers for 2D physics.  
[PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) | Asset type that defines the surface properties of a Collider2D.  
[PhysicsSceneExtensions2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsSceneExtensions2D.html) | Scene extensions to access the underlying physics scene.  
[PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html) | Represents a group of PhysicsShape2D and their geometry.  
[PhysicsUpdateBehaviour2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsUpdateBehaviour2D.html) | A base type for 2D physics components that required a callback during FixedUpdate.  
[PlatformEffector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformEffector2D.html) | Applies "platform" behaviour such as one-way collisions etc.  
[PointEffector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PointEffector2D.html) | Applies forces to attract/repulse against a point.  
[PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html) | Collider for 2D physics representing an arbitrary polygon defined by its vertices.  
[RelativeJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RelativeJoint2D.html) | Keeps two Rigidbody2D at their relative orientations.  
[Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) | Provides physics movement and other dynamics, and the ability to attach Collider2D to it.  
[SliderJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SliderJoint2D.html) | Joint that restricts the motion of a Rigidbody2D object to a single line.  
[SpringJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint2D.html) | Joint that attempts to keep two Rigidbody2D objects a set distance apart by applying a force between them.  
[SurfaceEffector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SurfaceEffector2D.html) | Applies tangent forces along the surfaces of colliders.  
[TargetJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TargetJoint2D.html) | The joint attempts to move a Rigidbody2D to a specific target position.  
[WheelJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelJoint2D.html) | The wheel joint allows the simulation of wheels by providing a constraining suspension motion with an optional motor.  
### Structs
Struct | Description  
---|---  
[ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) | Represents the separation or overlap of two Collider2D.  
[ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) | A set of parameters for filtering contact results. Define the angle by referring to their position in world space, where 0 degrees is parallel to the positive x-axis, 90 degrees is parallel to the positive y-axis, 180 degrees is parallel to the negative x-axis, and 270 degrees is parallel to the negative y-axis.  
[ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) | Details about a specific point of contact involved in a 2D physics collision.  
[JointAngleLimits2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointAngleLimits2D.html) | Angular limits on the rotation of a Rigidbody2D object around a HingeJoint2D.  
[JointMotor2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor2D.html) | Parameters for the optional motor force applied to a Joint2D.  
[JointSuspension2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSuspension2D.html) | Joint suspension is used to define how suspension works on a WheelJoint2D.  
[JointTranslationLimits2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointTranslationLimits2D.html) | Motion limits of a Rigidbody2D object along a SliderJoint2D.  
[PhysicsJobOptions2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsJobOptions2D.html) | A set of options that control how physics operates when using the job system to multithread the physics simulation.  
[PhysicsScene2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.html) | Represents a single instance of a 2D physics Scene.  
[PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) | Represents an efficient low-level physics shape used by the physics engine.  
[RaycastHit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html) | Returns information about 2D Colliders detected by a 2D physics query in the scene.  
### Enumerations
Enumeration | Description  
---|---  
[CapsuleDirection2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleDirection2D.html) | The direction that the capsule sides can extend.  
[ColliderErrorState2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.html) | Indicates what (if any) error was encountered when creating a 2D Collider.  
[CollisionDetectionMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode2D.html) | Controls how collisions are detected when a Rigidbody2D moves.  
[EffectorForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EffectorForceMode2D.html) | The mode used to apply Effector2D forces.  
[EffectorSelection2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EffectorSelection2D.html) | Selects the source and/or target to be used by an Effector2D.  
[ForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html) | Option for how to apply a force using Rigidbody2D.AddForce.  
[JointBreakAction2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.html) | Options for selecting which action to take when a Joint2D breaks.  
[JointLimitState2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimitState2D.html) | Represents the state of a joint limit.  
[PhysicsMaterialCombine2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.html) | Describes how PhysicsMaterial2D friction and bounciness are combined when two Collider2D come into contact.  
[PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) | Options for indicate which primitive shape type is used to interpret geometry contained within a PhysicsShape2D object.  
[RigidbodyConstraints2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints2D.html) | Use these flags to constrain motion of the Rigidbody2D.  
[RigidbodyInterpolation2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation2D.html) | Interpolation mode for Rigidbody2D objects.  
[RigidbodySleepMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodySleepMode2D.html) | Settings for a Rigidbody2D's initial sleep state.  
[RigidbodyType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.html) | The physical behaviour type of the Rigidbody2D.  
[SimulationMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode2D.html) | A selection of modes that control when Unity executes the 2D physics simulation.  
* * *
