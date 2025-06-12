* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html

# ArticulationBody
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
### Description
A body that forms part of a Physics articulation.
An articulation is a set of bodies arranged in a logical tree. The parent-child link in this tree reflects that the bodies have their relative motion constrained. Articulations are solved by a Featherstone solver that works in reduced coordinates - that is each body has relative coordinates to its parent but only along the unlocked degrees of freedom. This guarantees there is no unwanted stretch.  
Like with regular Joints, there are two anchors for each pair of connected articulation bodies. One anchor is defined in the parent body's reference frame, whereas the other one is defined in the child's reference frame. Changing the constraints, you directly affect the allowed space for relative positions of the two anchors. For instance, [ArticulationDofLock.LockedMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDofLock.LockedMotion.html) will not allow any relative motion at all.
### Properties
Property | Description  
---|---  
[anchorPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-anchorPosition.html) | Position of the anchor relative to this body.  
[anchorRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-anchorRotation.html) | Rotation of the anchor relative to this body.  
[angularDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-angularDamping.html) | Damping factor that affects how this body resists rotations.  
[angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-angularVelocity.html) | The angular velocity of the body defined in world space.  
[automaticCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-automaticCenterOfMass.html) | Whether or not to calculate the center of mass automatically.  
[automaticInertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-automaticInertiaTensor.html) | Whether or not to calculate the inertia tensor automatically.  
[centerOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-centerOfMass.html) | The center of mass of the body defined in local space.  
[collisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-collisionDetectionMode.html) | The ArticulationBody's collision detection mode.  
[dofCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-dofCount.html) | The amount of degrees of freedom of a body.  
[driveForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-driveForce.html) | The drive force in reduced coordinates.  
[excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-excludeLayers.html) | The additional layers that all Colliders attached to this ArticulationBody should exclude when deciding if the Collider can come into contact with another Collider.  
[immovable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-immovable.html) | Allows you to specify that this body is not movable.  
[includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-includeLayers.html) | The additional layers that all Colliders attached to this ArticulationBody should include when deciding if a the Collider can come into contact with another Collider.  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-index.html) | The index of the body in the hierarchy of articulation bodies.  
[inertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-inertiaTensor.html) | The inertia tensor of this body.  
[inertiaTensorRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-inertiaTensorRotation.html) | The rotation of the inertia tensor.  
[isRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-isRoot.html) | Indicates whether this body is the root body of the articulation (Read Only).  
[jointAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointAcceleration.html) | The joint acceleration in reduced coordinates.  
[jointForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointForce.html) | The joint force in reduced coordinates.  
[jointFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointFriction.html) | Allows you to specify the amount of friction that is applied as a result of the parent body moving relative to this body.  
[jointPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointPosition.html) | The joint position in reduced coordinates.  
[jointType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointType.html) | The type of joint connecting this body to its parent body.  
[jointVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointVelocity.html) | The joint velocity in reduced coordinates.  
[linearDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-linearDamping.html) | Damping factor that affects how this body resists linear motion.  
[linearLockX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-linearLockX.html) | The type of lock along X axis of movement.  
[linearLockY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-linearLockY.html) | The type of lock along Y axis of movement.  
[linearLockZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-linearLockZ.html) | The type of lock along Z axis of movement.  
[linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-linearVelocity.html) | Linear velocity of the body defined in world space.  
[mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-mass.html) | The mass of this articulation body.  
[matchAnchors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-matchAnchors.html) | Whether the parent anchor should be computed automatically or not.  
[maxAngularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-maxAngularVelocity.html) | The maximum angular velocity of the articulation body measured in radians per second.  
[maxDepenetrationVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-maxDepenetrationVelocity.html) | The maximum velocity of an articulation body when moving out of penetrating state.  
[maxJointVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-maxJointVelocity.html) | The maximum joint velocity of the articulation body joint in reduced coordinates.  
[maxLinearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-maxLinearVelocity.html) | The maximum linear velocity of the articulation body measured in meters per second.  
[parentAnchorPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-parentAnchorPosition.html) | Position of the anchor relative to this body's parent.  
[parentAnchorRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-parentAnchorRotation.html) | Rotation of the anchor relative to this body's parent.  
[sleepThreshold](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-sleepThreshold.html) | The mass-normalized energy threshold, below which objects start going to sleep.  
[solverIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-solverIterations.html) | The solverIterations determines how accurately articulation body joints and collision contacts are resolved.  
[solverVelocityIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-solverVelocityIterations.html) | The solverVelocityIterations affects how accurately articulation body joints and collision contacts are resolved during bounce.  
[swingYLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-swingYLock.html) | The magnitude of the conical swing angle relative to Y axis.  
[swingZLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-swingZLock.html) | The magnitude of the conical swing angle relative to Z axis.  
[twistLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-twistLock.html) | The type of lock for twist movement.  
[useGravity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-useGravity.html) | Controls whether gravity affects this articulation body.  
[worldCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-worldCenterOfMass.html) | The center of mass of the body defined in world space (Read Only).  
[xDrive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-xDrive.html) | The properties of drive along or around X.  
[yDrive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-yDrive.html) | The properties of drive along or around Y.  
[zDrive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-zDrive.html) | The properties of drive along or around Z.  
### Public Methods
Method | Description  
---|---  
[AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForce.html) | Applies a force to the ArticulationBody.  
[AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddForceAtPosition.html) | Applies a force at a specific position, resulting in applying a torque and force on the object.  
[AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeForce.html) | Applies a force to the Articulation Body, relative to its local coordinate system.  
[AddRelativeTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddRelativeTorque.html) | Applies a torque to the articulation body, relative to its local coordinate system.  
[AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.AddTorque.html) | Add torque to the articulation body.  
[GetAccumulatedForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetAccumulatedForce.html) | Returns the force that the ArticulationBody has accumulated before the simulation step.  
[GetAccumulatedTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetAccumulatedTorque.html) | Returns the torque that the ArticulationBody has accumulated before the simulation step.  
[GetClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetClosestPoint.html) | Return the point on the articulation body that is closest to a given one.  
[GetDenseJacobian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDenseJacobian.html) | Calculates and writes dense Jacobian matrix of the articulation body hierarchy to the supplied struct.  
[GetDofStartIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDofStartIndices.html) | Calculates and reads back reduced coordinate data start indexes in reduced coordinate data buffer for every articulation body in the hierarchy.  
[GetDriveForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDriveForces.html) | Reads the entire hierarchy of Articulation Bodies and fills the supplied list of floats with Articulation Drive forces.  
[GetDriveTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDriveTargets.html) | Reads back articulation body joint drive targets of the entire hierarchy to the supplied list of floats.  
[GetDriveTargetVelocities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDriveTargetVelocities.html) | Reads back articulation body joint drive target velocities of the entire hierarchy to the supplied list of floats .  
[GetJointAccelerations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointAccelerations.html) | Reads back articulation body joint accelerations of the entire hierarchy to the supplied list of floats .  
[GetJointCoriolisCentrifugalForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointCoriolisCentrifugalForces.html) | Fills the supplied list of floats with the forces required to counteract the Coriolis and centrifugal forces for each Articulation Body in the articulation.  
[GetJointExternalForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointExternalForces.html) | Fills the supplied list of floats with forces required to counteract any existing external forces (applied using ArticulationBody.AddForce or ArticulationBody.AddTorque) for each Articulation Body in the articulation.  
[GetJointForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointForces.html) | Reads back articulation body joint forces of the entire hierarchy to the supplied list of floats .  
[GetJointForcesForAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointForcesForAcceleration.html) | Returns the forces required for the body to reach the provided acceleration in reduced space.  
[GetJointGravityForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointGravityForces.html) | Fills the supplied list of floats with forces required to counteract gravity for each Articulation Body in the articulation.  
[GetJointPositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointPositions.html) | Reads back articulation body joint positions of the entire hierarchy to the supplied list of floats .  
[GetJointVelocities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointVelocities.html) | Reads back articulation body joint velocities of the entire hierarchy to the supplied list of floats .  
[GetPointVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetPointVelocity.html) | Gets the velocity of the articulation body at the specified worldPoint in global space.  
[GetRelativePointVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetRelativePointVelocity.html) | The velocity relative to the articulation body at the point relativePoint.  
[IsSleeping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.IsSleeping.html) | Indicates whether the articulation body is sleeping.  
[PublishTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.PublishTransform.html) | Reads the position and rotation of the Articulation Body from the physics system and applies it to the corresponding Transform component.  
[ResetCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.ResetCenterOfMass.html) | Resets the center of mass of the articulation body.  
[ResetInertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.ResetInertiaTensor.html) | Resets the inertia tensor value and rotation.  
[SetDriveDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveDamping.html) | Sets the damping value of the specified drive.  
[SetDriveForceLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveForceLimit.html) | Sets the force limit of the specified drive.  
[SetDriveLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveLimits.html) | Sets the lower and upper limits of the drive.  
[SetDriveStiffness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveStiffness.html) | Sets the stiffness value of the specified drive.  
[SetDriveTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveTarget.html) | Sets the target value of the specified drive.  
[SetDriveTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveTargets.html) | Assigns articulation body joint drive targets for the entire hierarchy of bodies.  
[SetDriveTargetVelocities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveTargetVelocities.html) | Assigns articulation body joint drive target velocities for the entire hierarchy of bodies.  
[SetDriveTargetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetDriveTargetVelocity.html) | Sets the target velocity value of the specified drive.  
[SetJointForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetJointForces.html) | Assigns articulation body joint forces for the entire hierarchy of bodies.  
[SetJointPositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetJointPositions.html) | Assigns articulation body joint positions for the entire hierarchy of bodies.  
[SetJointVelocities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetJointVelocities.html) | Assigns articulation body joint velocities for the entire hierarchy of bodies.  
[Sleep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.Sleep.html) | Forces an articulation body to sleep.  
[SnapAnchorToClosestContact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SnapAnchorToClosestContact.html) | Snap the anchor to the closest contact between the connected bodies.  
[TeleportRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.TeleportRoot.html) | Teleport the root body of the articulation to a new pose.  
[WakeUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.WakeUp.html) | Forces an articulation body to wake up.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
