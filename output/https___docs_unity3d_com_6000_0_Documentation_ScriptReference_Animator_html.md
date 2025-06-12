* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html

# Animator
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
### Description
Interface to control the Mecanim animation system.
### Properties
Property | Description  
---|---  
[angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-angularVelocity.html) | Gets the avatar angular velocity for the last evaluated frame.  
[animatePhysics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-animatePhysics.html) | When enabled, the physics system uses animated transforms from GameObjects with kinematic Rigidbody components to influence other GameObjects.  
[applyRootMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-applyRootMotion.html) | Should root motion be applied?  
[avatar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-avatar.html) | Gets/Sets the current Avatar.  
[avatarRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-avatarRoot.html) | Returns the Avatar root Transform.  
[bodyPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-bodyPosition.html) | The position of the body center of mass.  
[bodyRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-bodyRotation.html) | The rotation of the body center of mass.  
[cullingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-cullingMode.html) | Controls culling of this Animator component.  
[deltaPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-deltaPosition.html) | Gets the avatar delta position for the last evaluated frame.  
[deltaRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-deltaRotation.html) | Gets the avatar delta rotation for the last evaluated frame.  
[feetPivotActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-feetPivotActive.html) | Blends pivot point between body center of mass and feet pivot.  
[fireEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-fireEvents.html) | Sets whether the Animator sends events of type AnimationEvent.  
[gravityWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-gravityWeight.html) | The current gravity weight based on current animations that are played.  
[hasBoundPlayables](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-hasBoundPlayables.html) | Returns true if Animator has any playables assigned to it.  
[hasRootMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-hasRootMotion.html) | Returns true if the current rig has root motion.  
[hasTransformHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-hasTransformHierarchy.html) | Returns true if the object has a transform hierarchy.  
[humanScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-humanScale.html) | Returns the scale of the current Avatar for a humanoid rig, (1 by default if the rig is generic).  
[isHuman](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-isHuman.html) | Returns true if the current rig is humanoid, false if it is generic.  
[isInitialized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-isInitialized.html) | Returns whether the animator is initialized successfully.  
[isMatchingTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-isMatchingTarget.html) | If automatic matching is active.  
[isOptimizable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-isOptimizable.html) | Returns true if the current rig is optimizable with AnimatorUtility.OptimizeTransformHierarchy.  
[keepAnimatorStateOnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-keepAnimatorStateOnDisable.html) | Controls the behaviour of the Animator component when a GameObject is inactive.  
[layerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-layerCount.html) | Returns the number of layers in the controller.  
[layersAffectMassCenter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-layersAffectMassCenter.html) | Additional layers affects the center of mass.  
[leftFeetBottomHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-leftFeetBottomHeight.html) | Get left foot bottom height.  
[parameterCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-parameterCount.html) | Returns the number of parameters in the controller.  
[parameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-parameters.html) | The AnimatorControllerParameter list used by the animator. (Read Only)  
[pivotPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-pivotPosition.html) | Get the current position of the pivot.  
[pivotWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-pivotWeight.html) | Gets the pivot weight.  
[playableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-playableGraph.html) | The PlayableGraph created by the Animator.  
[playbackTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-playbackTime.html) | Sets the playback position in the recording buffer.  
[recorderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-recorderMode.html) | Gets the mode of the Animator recorder.  
[recorderStartTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-recorderStartTime.html) | Start time of the first frame of the buffer relative to the frame at which StartRecording was called.  
[recorderStopTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-recorderStopTime.html) | End time of the recorded clip relative to when StartRecording was called.  
[rightFeetBottomHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-rightFeetBottomHeight.html) | Get right foot bottom height.  
[rootPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-rootPosition.html) | The root position, the position of the game object.  
[rootRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-rootRotation.html) | The root rotation, the rotation of the game object.  
[runtimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-runtimeAnimatorController.html) | The runtime representation of AnimatorController that controls the Animator.  
[speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-speed.html) | The playback speed of the Animator. 1 is normal playback speed.  
[stabilizeFeet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-stabilizeFeet.html) | Automatic stabilization of feet during transition and blending.  
[targetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-targetPosition.html) | Returns the position of the target specified by SetTarget.  
[targetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-targetRotation.html) | Returns the rotation of the target specified by SetTarget.  
[updateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-updateMode.html) | Specifies the update mode of the Animator.  
[velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-velocity.html) | Gets the avatar velocity for the last evaluated frame.  
[writeDefaultValuesOnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-writeDefaultValuesOnDisable.html) | Specifies whether playable graph values are reset or preserved when the Animator is disabled.  
### Public Methods
Method | Description  
---|---  
[ApplyBuiltinRootMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.ApplyBuiltinRootMotion.html) | Apply the default Root Motion.  
[CrossFade](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.CrossFade.html) | Creates a crossfade from the current state to any other state using normalized times.  
[CrossFadeInFixedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.CrossFadeInFixedTime.html) | Creates a crossfade from the current state to any other state using times in seconds.  
[GetAnimatorTransitionInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetAnimatorTransitionInfo.html) | Returns an AnimatorTransitionInfo with the informations on the current transition.  
[GetBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBehaviour.html) | Returns the first StateMachineBehaviour that matches type T or is derived from T. Returns null if none are found.  
[GetBehaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBehaviours.html) | Returns all StateMachineBehaviour that match type T or are derived from T. Returns null if none are found.  
[GetBoneTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBoneTransform.html) | Retrieves the Transform mapped to a human bone based on its id.  
[GetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBool.html) | Returns the value of the given boolean parameter.  
[GetCurrentAnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorClipInfo.html) | Returns an array of all the AnimatorClipInfo in the current state of the given layer.  
[GetCurrentAnimatorClipInfoCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorClipInfoCount.html) | Returns the number of AnimatorClipInfo in the current state.  
[GetCurrentAnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorStateInfo.html) | Returns an AnimatorStateInfo with the information on the current state.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetFloat.html) | Returns the value of the given float parameter.  
[GetIKHintPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKHintPosition.html) | Gets the position of an IK hint.  
[GetIKHintPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKHintPositionWeight.html) | Gets the translative weight of an IK Hint (0 = at the original animation before IK, 1 = at the hint).  
[GetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKPosition.html) | Gets the position of an IK goal.  
[GetIKPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKPositionWeight.html) | Gets the translative weight of an IK goal (0 = at the original animation before IK, 1 = at the goal).  
[GetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKRotation.html) | Gets the rotation of an IK goal.  
[GetIKRotationWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKRotationWeight.html) | Gets the rotational weight of an IK goal (0 = rotation before IK, 1 = rotation at the IK goal).  
[GetInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetInteger.html) | Returns the value of the given integer parameter.  
[GetLayerIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetLayerIndex.html) | Returns the index of the layer with the given name.  
[GetLayerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetLayerName.html) | Returns the layer name.  
[GetLayerWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetLayerWeight.html) | Returns the weight of the layer at the specified index.  
[GetNextAnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetNextAnimatorClipInfo.html) | Returns an array of all the AnimatorClipInfo in the next state of the given layer.  
[GetNextAnimatorClipInfoCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetNextAnimatorClipInfoCount.html) | Returns the number of AnimatorClipInfo in the next state.  
[GetNextAnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetNextAnimatorStateInfo.html) | Returns an AnimatorStateInfo with the information on the next state.  
[GetParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetParameter.html) | See AnimatorController.parameters.  
[HasState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.HasState.html) | Returns true if the state exists in this layer, false otherwise.  
[InterruptMatchTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.InterruptMatchTarget.html) | Interrupts the automatic target matching.  
[IsInTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.IsInTransition.html) | Returns true if there is a transition on the given layer, false otherwise.  
[IsParameterControlledByCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.IsParameterControlledByCurve.html) | Returns true if the parameter is controlled by a curve, false otherwise.  
[MatchTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.MatchTarget.html) | Automatically adjust the GameObject position and rotation.  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.Play.html) | Plays a state.  
[PlayInFixedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.PlayInFixedTime.html) | Plays a state.  
[Rebind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.Rebind.html) | Rebind all the animated properties and mesh data with the Animator.  
[ResetTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.ResetTrigger.html) | Resets the value of the given trigger parameter.  
[SetBoneLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetBoneLocalRotation.html) | Sets local rotation of a human bone during a IK pass.  
[SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetBool.html) | Sets the value of the given boolean parameter.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetFloat.html) | Send float values to the Animator to affect transitions.  
[SetIKHintPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKHintPosition.html) | Sets the position of an IK hint.  
[SetIKHintPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKHintPositionWeight.html) | Sets the translative weight of an IK hint (0 = at the original animation before IK, 1 = at the hint).  
[SetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html) | Sets the position of an IK goal.  
[SetIKPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPositionWeight.html) | Sets the translative weight of an IK goal (0 = at the original animation before IK, 1 = at the goal).  
[SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html) | Sets the rotation of an IK goal.  
[SetIKRotationWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotationWeight.html) | Sets the rotational weight of an IK goal (0 = rotation before IK, 1 = rotation at the IK goal).  
[SetInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetInteger.html) | Sets the value of the given integer parameter.  
[SetLayerWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetLayerWeight.html) | Sets the weight of the layer at the given index.  
[SetLookAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetLookAtPosition.html) | Sets the look at position.  
[SetLookAtWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetLookAtWeight.html) | Set look at weights.  
[SetTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTarget.html) | Sets an AvatarTarget and a targetNormalizedTime for the current state.  
[SetTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTrigger.html) | Sets the value of the given trigger parameter.  
[StartPlayback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StartPlayback.html) | Sets the animator in playback mode.  
[StartRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StartRecording.html) | Sets the animator in recording mode, and allocates a circular buffer of size frameCount.  
[StopPlayback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StopPlayback.html) | Stops the animator playback mode. When playback stops, the avatar resumes getting control from game logic.  
[StopRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StopRecording.html) | Stops animator record mode.  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.Update.html) | Evaluates the animator based on deltaTime.  
[WriteDefaultValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.WriteDefaultValues.html) | Forces a write of the default values stored in the animator.  
### Static Methods
Method | Description  
---|---  
[StringToHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StringToHash.html) | Generates a parameter id from a string.  
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
