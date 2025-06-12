* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html

# UnityEngine.AnimationModule
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
The Animation module implements Unity's animation system.
### Classes
Class | Description  
---|---  
[AimConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.html) | Constrains the orientation of an object relative to the position of one or more source objects, such that the object is facing the average position of the sources.  
[Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) | The animation component is used to play back animations.  
[AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) | Stores keyframe based animations.  
[AnimationEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationEvent.html) | AnimationEvent lets you call a script function similar to SendMessage as part of playing back an animation.  
[AnimationPlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableBinding.html) | A PlayableBinding that contains information representing an AnimationPlayableOutput.  
[AnimationPlayableOutputExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Animations.AnimationPlayableOutputExtensions.html) | Static class providing experimental extension methods for AnimationPlayableOutput .  
[AnimationPlayableUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.AnimationPlayableUtilities.html) | Implements high-level utility methods to simplify use of the Playable API with Animations.  
[AnimationSceneHandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationSceneHandleUtility.html) | Static class providing utility functions for animation scene handles.  
[AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) | The AnimationState gives full control over animation blending.  
[AnimationStreamHandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStreamHandleUtility.html) | Static class providing utility functions for animation stream handles.  
[Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) | Interface to control the Mecanim animation system.  
[AnimatorControllerParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorControllerParameter.html) | Used to communicate between scripting and the controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API.  
[AnimatorJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html) | Static class providing extension methods for Animator and the animation C# jobs.  
[AnimatorOverrideController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html) | Interface to control Animator Override Controller.  
[AnimatorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.html) | Various utilities for animator manipulation.  
[Avatar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Avatar.html) | Avatar definition.  
[AvatarBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.html) | Class to build avatars from user scripts.  
[AvatarMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.html) | AvatarMask is used to mask out humanoid body parts and transforms.  
[DiscreteEvaluationAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.DiscreteEvaluationAttribute.html) | Use this attribute to indicate that a property will be evaluated as a discrete value during animation playback.  
[GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html) | Animation utility functions for reading and writing values from Unity components.  
[HumanPoseHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.html) | Use this class to create, read, and write the HumanPose for a humanoid avatar skeleton hierarchy or an avatar pose.  
[HumanTrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.html) | Details of all the human bone and muscle types defined by Mecanim.  
[LookAtConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.LookAtConstraint.html) |  Constrains the orientation of an object relative to the position of one or more source objects, such that the object is facing the average position of the sources. The LookAtConstraint is a simplified AimConstraint typically used with a Camera.   
[Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html) | Base class for AnimationClips and BlendTrees.  
[NotKeyableAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.NotKeyableAttribute.html) | Use this attribute in a script to mark a property as non-animatable.  
[ParentConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.html) | Constrains the orientation and translation of an object to one or more source objects. The constrained object behaves as if it is in the hierarchy of the sources.  
[PositionConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PositionConstraint.html) | Constrains the position of an object relative to the position of one or more source objects.  
[RotationConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.RotationConstraint.html) | Constrains the rotation of an object relative to the rotation of one or more source objects.  
[RuntimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeAnimatorController.html) | The runtime representation of the AnimatorController. Use this representation to change the Animator Controller during runtime.  
[ScaleConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ScaleConstraint.html) | Constrains the scale of an object relative to the scale of one or more source objects.  
[SharedBetweenAnimatorsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SharedBetweenAnimatorsAttribute.html) | The SharedBetweenAnimatorsAttribute specifies that this StateMachineBehaviour is instantiated only once and shared by all Animator instances. This attribute reduces the memory footprint for each controller instance.  
[StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html) | StateMachineBehaviour is a component that can be added to a state machine state. It's the base class any script on a state must derive from.  
### Structs
Struct | Description  
---|---  
[AnimationClipPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.html) | A Playable that controls an AnimationClip.  
[AnimationHumanStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream.html) | The humanoid stream of animation data passed from one Playable to another.  
[AnimationLayerMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationLayerMixerPlayable.html) | An implementation of IPlayable that controls an animation layer mixer.  
[AnimationMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html) | An implementation of IPlayable that controls an animation mixer.  
[AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) | A IPlayableOutput implementation that connects the PlayableGraph to an Animator in the Scene.  
[AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) | A Playable that can run a custom, multi-threaded animation job.  
[AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) | The stream of animation data passed from one Playable to another.  
[AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) | Information about clip being played and blended by the Animator.  
[AnimatorControllerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerPlayable.html) | An implementation of IPlayable that controls an animation RuntimeAnimatorController.  
[AnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) | Information about the current or next state.  
[AnimatorTransitionInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorTransitionInfo.html) | Information about the current transition.  
[BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) | A BoundProperty is a safe handle to read and write value in a generic way from any Unity components.  
[ConstraintSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ConstraintSource.html) | Represents a source for the constraint.  
[GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html) | Defines an animatable property on a Unity Component.  
[HumanBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone.html) | The mapping between a bone in the model and the conceptual bone in the Mecanim human anatomy.  
[HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html) | Class that holds humanoid avatar parameters to pass to the AvatarBuilder.BuildHumanAvatar function.  
[HumanLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanLimit.html) | This class stores the rotation limits that define the muscle for a single human bone.  
[HumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPose.html) | Retargetable humanoid pose.  
[MatchTargetWeightMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MatchTargetWeightMask.html) | Use this struct to specify the position and rotation weight mask for Animator.MatchTarget.  
[MuscleHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.html) | Handle for a muscle in the AnimationHumanStream.  
[PropertySceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html) | Handle to read a Component property on an object in the Scene.  
[PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html) | Handle for a Component property on an object in the AnimationStream.  
[SkeletonBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone.html) | Details of the Transform name mapped to the skeleton bone of a model and its default position and rotation in the T-pose.  
[TransformSceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html) | Handle to read position, rotation and scale of an object in the Scene.  
[TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html) | Position, rotation and scale of an object in the AnimationStream.  
### Enumerations
Enumeration | Description  
---|---  
[AnimationBlendMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationBlendMode.html) | Used by Animation.Play function.  
[AnimationCullingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCullingType.html) | This enum controlls culling of Animation component.  
[AnimationStreamSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Animations.AnimationStreamSource.html) | Describes how an AnimationStream is initialized  
[AnimationUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUpdateMode.html) | The update mode of the Animation component.  
[AnimatorControllerParameterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorControllerParameterType.html) | The type of the parameter.  
[AnimatorCullingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorCullingMode.html) | Culling mode for the Animator.  
[AnimatorRecorderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorRecorderMode.html) | The mode of the Animator's recorder.  
[AnimatorUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUpdateMode.html) | The update mode of the Animator.  
[ArmDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.html) | Enumeration of all the muscles in an arm.  
[AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) | IK Goal.  
[AvatarIKHint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKHint.html) | IK Hint.  
[AvatarMaskBodyPart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMaskBodyPart.html) | Avatar body part.  
[AvatarTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarTarget.html) | Target.  
[Axis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.Axis.html) | Represents the axes used in 3D space.  
[BodyDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BodyDof.html) | Enumeration of all the muscles in the body.  
[CustomStreamPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CustomStreamPropertyType.html) | The type of custom stream property to create using BindCustomStreamProperty  
[DurationUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DurationUnit.html) | Describe the unit of a duration.  
[FingerDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FingerDof.html) | Enumeration of all the muscles in a finger.  
[HeadDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HeadDof.html) | Enumeration of all the muscles in the head.  
[HumanBodyBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBodyBones.html) | Human Body Bones.  
[HumanPartDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPartDof.html) | Enumeration of all the parts in a human.  
[LegDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LegDof.html) | Enumeration of all the muscles in a leg.  
[PlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) | Used by Animation.Play function.  
[QueueMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueueMode.html) | Used by Animation.Play function.  
* * *
