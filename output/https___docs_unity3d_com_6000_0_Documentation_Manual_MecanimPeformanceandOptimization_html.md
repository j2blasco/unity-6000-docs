* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimPeformanceandOptimization.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Performance and optimization


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-Examples.html)
Playables Examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimFAQ.html)
Mecanim FAQ
# Performance and optimization
This page contains some tips to help you obtain the best performance in Unity, covering the [animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimPeformanceandOptimization.html#anim) and [run-time optimizations](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimPeformanceandOptimization.html#runtime).
**Note:** For tips on modeling your character in a 3d application for best performance in Unity, see [Modeling characters for optimal performance](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html).
## Animation system
### Controllers
The [Animator](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html) doesn’t spend time processing when a [Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html) is not set to it.
### Simple animation
Playing a single [Animation Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) with no blending can make Unity slower than the [legacy animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html). The old system is very direct, sampling the curve and directly writing into the transform. Unity’s current animation system has temporary buffers it uses for blending, and there is additional copying of the sampled curve and other data. The current system layout is optimized for animation blending and more complex setups.
### Scale curves
Animating scale curves is more expensive than animating translation and rotation curves. To improve performance, avoid scale animations. 
**Note:** This does not apply to constant curves (curves that have the same value for the length of the [animation clip](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)). Constant curves are optimized, and are less expensive than normal curves. Constant curves that have the same values as the default **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) values do not write to the scene every frame.
### Layers
Most of the time Unity is evaluating animations, and keeps the overhead for [animation layers](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationLayer) and [Animation State Machines](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationStateMachine) to the minimum. The cost of adding another layer to the animator, synchronized or not, depends on what animations and blend trees are played by the layer. When the weight of the layer is zero, Unity skips the layer update.
### Humanoid vs. Generic animation types
These are tips to help you decide between these types:
  * When importing **Humanoid animation** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation) use an **Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) Mask (class-AvatarMask) to remove IK Goals or finger animation if you don’t need them.
  * When you use Generic, using **root motion** Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootMotion) is more expensive than not using it. If your animations don’t use root motion, make sure that you have not specified a root bone.


### Scene-level optimization
There are many optimizations that can be made, some useful tips include:
  * Use hashes instead of strings to query the Animator.
  * Implement a small AI Layer to control the Animator. You can make it provide simple callbacks for OnStateChange, OnTransitionBegin, and other events.
  * Use State Tags to easily match your AI **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine) to the Unity state machine.
  * Use additional curves to simulate events.
  * Use additional curves to mark up your animations; for example, in conjunction with [target matching](https://docs.unity3d.com/6000.0/Documentation/Manual/TargetMatching.html)A scripting function that allows you to move characters in such a way that a hand or foot lands in a certain place at a certain time. For example, the character may need to jump across stepping stones or jump and grab an overhead beam. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/TargetMatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Targetmatching).


## Runtime Optimizations
### Visibility and updates
Always optimize animations by setting the animator [Culling Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html) to **Cull Completely** , and disable the [skinned mesh renderer’s](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html) **Update When Offscreen** property. This saves Unity from updating animations when the character is not visible.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-Examples.html)
Playables Examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimFAQ.html)
Mecanim FAQ
