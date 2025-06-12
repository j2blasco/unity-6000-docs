* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * Animation State Machine


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)
Animator Window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)
State Machine Basics
# Animation State Machine
It is common for a character or a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to have several different animations for the different actions it performs in a game. For example, a character breathes and sways slightly when idle, walks when commanded, and raises their arms when they fall from a platform. A door has animations for when it opens, closes, jams, and when it gets broken open.
Mecanim uses a visual layout system, similar to a flowchart, to represent a **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine). You use this visual layout system to control and arrange when to play the **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) for your character or GameObject.
The following topics provide more details on Mecanim’s state machine:
  * [State Machine Basics](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)
  * [Animation States](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html)
  * [Animation Parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html)Used to communicate between scripting and the Animator Controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationParameters)
  * [State Machine Transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineTransitions.html)
  * [Animation Transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html)Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineTransitions.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationTransition)
  * [Animation Blend Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html)Used for continuous blending between similar Animation Clips based on float Animation Parameters. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationBlendTree)
  * [State Machine Behaviours](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html)A script that attaches to a state within a state machine to control what happens when the state machine enters, exits or remains within a state, such as play sounds as states are entered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachineBehaviour)
  * [Sub-State Machines](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedStateMachines.html)
  * [Animation Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationLayer)
  * [State Machine Solo and Mute](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSoloMute.html)
  * [Target Matching](https://docs.unity3d.com/6000.0/Documentation/Manual/TargetMatching.html)A scripting function that allows you to move characters in such a way that a hand or foot lands in a certain place at a certain time. For example, the character may need to jump across stepping stones or jump and grab an overhead beam. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/TargetMatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Targetmatching)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)
Animator Window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)
State Machine Basics
