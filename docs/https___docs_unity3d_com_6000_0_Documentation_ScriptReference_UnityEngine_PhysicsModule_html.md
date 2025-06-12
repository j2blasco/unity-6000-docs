* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html

# UnityEngine.PhysicsModule
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
The Physics module implements 3D physics in Unity.
### Classes
Class | Description  
---|---  
[ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) | A body that forms part of a Physics articulation.  
[BoxCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) | A box-shaped primitive collider.  
[CapsuleCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider.html) | A capsule-shaped primitive collider.  
[CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) | A CharacterController allows you to easily do movement constrained by collisions without having to deal with a rigidbody.  
[CharacterJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint.html) | Character Joints are mainly used for Ragdoll effects.  
[Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) | A base class of all colliders.  
[Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) | Describes a collision.  
[ConfigurableJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConfigurableJoint.html) | The configurable joint is an extremely flexible joint giving you complete control over rotation and linear motion.  
[ConstantForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConstantForce.html) | A force applied constantly.  
[ControllerColliderHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ControllerColliderHit.html) | ControllerColliderHit is used by CharacterController.OnControllerColliderHit to give detailed information about the collision and how to deal with it.  
[FixedJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FixedJoint.html) | The Fixed joint groups together 2 rigidbodies, making them stick together in their bound position.  
[HingeJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) | The HingeJoint groups together 2 rigid bodies, constraining them to move like connected by a hinge.  
[ImmediatePhysics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.ImmediatePhysics.html) | This class contains methods to run the immediate simulation steps.  
[Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html) | Joint is the base class for all joints.  
[MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) | A mesh collider allows you to do collision detection between meshes and primitives.  
[Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html) | Global physics properties and helper methods.  
[PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html) | Physics material describes how to handle colliding objects (friction, bounciness).  
[PhysicsSceneExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsSceneExtensions.html) | Scene extensions to access the underlying physics scene.  
[Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) | Control of an object's position through physics simulation.  
[SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) | A sphere-shaped primitive collider.  
[SpringJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint.html) | The spring joint ties together 2 rigid bodies, spring forces will be automatically applied to keep the object at the given distance.  
### Structs
Struct | Description  
---|---  
[ArticulationDrive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive.html) | Drive applies forces and torques to the connected bodies.  
[ArticulationJacobian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian.html) | The floating point dense Jacobian matrix of the articulation body hierarchy.  
[ArticulationReducedSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationReducedSpace.html) | Coordinates in reduced space.  
[BoxcastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.html) | Use this struct to set up a box cast command to be performed asynchronously during a job.  
[BoxGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.BoxGeometry.html) | Contains the basic geometric shape of a box.  
[CapsulecastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsulecastCommand.html) | Use this struct to set up a capsule cast command that is performed asynchronously during a job.  
[CapsuleGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry.html) | Contains the basic geometric shape of a capsule.  
[ClosestPointCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.html) | Struct used to set up a closest point command to be performed asynchronously during a job.When you use this struct to schedule a batch of closest commands, they are performed asynchronously and in parallel to each other. The results of the closest points are written to the results buffer. Because the results are written asynchronously, the results buffer cannot be accessed until the job has been completed.The result for a command at index N in the command buffer is stored at index N in the results buffer.  
[ColliderHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderHit.html) | Struct used to retrieve information from an Overlap batch query.  
[ContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.html) | A pair of Colliders that belong to the bodies in the parent ContactPairHeader struct.  
[ContactPairHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html) | A header struct which contains colliding bodies.  
[ContactPairPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairPoint.html) | A readonly struct describing a contact point between two Colliders.  
[ContactPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) | Describes a contact point where the collision occurs.  
[ConvexMeshGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.ConvexMeshGeometry.html) | Contains the basic geometric shape of a convex mesh.  
[GeometryHolder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.GeometryHolder.html) | Holds the basic information of a geometric shape and its type.  
[ImmediateContact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.ImmediateContact.html) | Describes a contact where two shapes collide.  
[ImmediateTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.ImmediateTransform.html) | A transform, containing a position and rotation.  
[JointDrive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointDrive.html) | How the joint's movement will behave along its local X axis.  
[JointLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointLimits.html) | JointLimits is used by the HingeJoint to limit the joints angle.  
[JointMotor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointMotor.html) | The JointMotor is used to motorize a joint.  
[JointSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html) | JointSpring is used add a spring force to HingeJoint and PhysicsMaterial.  
[ModifiableContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.html) | A light-weight proxy that allows to access the contact buffers directly.  
[ModifiableMassProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableMassProperties.html) | Mass-related modifiable properties of a contact pair.  
[OverlapBoxCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand.html) | Struct used to set up an overlap box command to be performed asynchronously during a job.  
[OverlapCapsuleCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapCapsuleCommand.html) | Struct used to set up an overlap capsule command to be performed asynchronously during a job.  
[OverlapSphereCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand.html) | Struct used to setup an overlap sphere command to be performed asynchronously during a job.  
[PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) | Represents a single instance of a 3D physics Scene.  
[QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html) | Creates a struct to set up parameters for batch queries: RaycastCommand, BoxcastCommand, CapsulecastCommand, SpherecastCommand.  
[RaycastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html) | Struct used to set up a raycast command to be performed asynchronously during a job.  
[RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) | Structure used to get information back from a raycast.  
[SoftJointLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SoftJointLimit.html) | The limits defined by the CharacterJoint.  
[SoftJointLimitSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SoftJointLimitSpring.html) | The configuration of the spring attached to the joint's limits: linear and angular. Used by CharacterJoint and ConfigurableJoint.  
[SpherecastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.html) | Use this struct to set up a sphere cast command that is performed asynchronously during a job.  
[SphereGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.SphereGeometry.html) | Contains the basic geometric shape of a sphere.  
[TerrainGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.TerrainGeometry.html) | Contains the geometric shape of a Terrain collider.  
[TriangleMeshGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.TriangleMeshGeometry.html) | Contains the basic geometric shape of a non-convex mesh (sometimes known as a triangle mesh).  
[WheelFrictionCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html) | WheelFrictionCurve is used by the WheelCollider to describe friction properties of the wheel tire.  
### Enumerations
Enumeration | Description  
---|---  
[ArticulationDofLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDofLock.html) | The lock type applied to a particular degree of freedom of an articulation body.  
[ArticulationDriveAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDriveAxis.html) | An axis of a drive of an ArticulationBody.  
[ArticulationDriveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDriveType.html) | The drive type applied to a particular drive of an ArticulationBody.  
[ArticulationJointType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJointType.html) | The type of the joint that restricts movement of the two connected articulation bodies.  
[CollisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html) | The collision detection mode constants used for Rigidbody.collisionDetectionMode.  
[CollisionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.html) | CollisionFlags is a bitmask returned by CharacterController.Move.  
[ConfigurableJointMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConfigurableJointMotion.html) | Constrains movement for a ConfigurableJoint along the 6 axes.  
[ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) | Use ForceMode to specify how to apply a force using Rigidbody.AddForce or ArticulationBody.AddForce.  
[GeometryType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.GeometryType.html) | The set of basic geometry shape types that can exist.  
[JointProjectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointProjectionMode.html) | Determines how to snap physics joints back to its constrained position when it drifts off too much.  
[MeshColliderCookingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.html) | Cooking options that are available with MeshCollider.  
[PhysicsMaterialCombine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine.html) | Describes how physics materials of the colliding objects are combined.The friction force as well as the residual bounce impulse are applied symmetrically to both of the colliders in contact, so each pair of overlapping colliders must have a single set of friction and bouciness settings. However, one can set arbitrary physics materials to any colliders. For that particular reason, there is a mechanism that allows the combination of two different sets of properties that correspond to each of the colliders in contact into one set to be used in the solver.Specifying Average, Maximum, Minimum or Multiply as the physics material combine mode, you directly set the function that is used to combine the settings corresponding to the two overlapping colliders into one set of settings that can be used to apply the material effect.Note that there is a special case when the two overlapping colliders have physics materials with different combine modes set. In this particular case, the function that has the highest priority is used. The priority order is as follows: Average < Minimum < Multiply < Maximum. For example, if one material has Average set but the other one has Maximum, then the combine function to be used is Maximum, since it has higher priority.  
[QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) | Overrides the global Physics.queriesHitTriggers.  
[RigidbodyConstraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.html) | Use these flags to constrain motion of Rigidbodies.  
[RigidbodyInterpolation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation.html) |  Rigidbody interpolation mode.  
[RotationDriveMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RotationDriveMode.html) | Control ConfigurableJoint's rotation with either X & YZ or Slerp Drive.  
[SimulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.html) | A selection of modes that control when Unity executes the physics simulation.  
[SimulationOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationOption.html) | An enumerator that specifies physics simulation options.  
[SimulationStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationStage.html) | A flag enum to determine which simulation stages to run.  
* * *
