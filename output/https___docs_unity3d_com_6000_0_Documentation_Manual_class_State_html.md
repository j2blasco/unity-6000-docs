* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  * Animation States


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)
State Machine Basics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html)
Animation Parameters
# Animation States
**Animation States** are the basic building blocks of an **Animation**State Machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine)**. Each state contains an animation sequence (or [blend tree](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html)) that plays when the character is in that state. Select the state in the ****Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController)**, to view the properties for the state in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
![Animation State properties in the Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/anim-insp-state-properties.png) Animation State properties in the Inspector window. **_Property:_** | **_Description:_**  
---|---  
**Motion** | The **animation clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) or blend tree assigned to this state.  
**Speed** | The default speed of the motion for this state. Enable Parameter to modify the speed with a custom value from a script. For example, you can multiply the speed with a custom value to decelerate or accelerate the play speed.  
**Motion Time** | The time used to play the motion for this state. Enable Parameter to control the motion time with a custom value from a script.  
**Mirror** | This property only applies to states with **humanoid animation** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation). Enable to mirror the animation for this state. Enable Parameter to enable or disable mirroring from a script.  
**Cycle Offset** | The offset added to the state time of the motion. This offset does not affect the Motion Time. Enable Parameter to specify the Cycle Offset from a script.  
**Foot IK** | This property only applies to states with humanoid animation. Enable to respect Foot IK for this state.  
**Write Defaults** | Whether the AnimatorStates writes the default values for properties that are not animated by its motion.  
**Transitions** | The list of transitions originating from this state.  
The default state, displayed in brown, is the state that the machine will be in when it is first activated. You can change the default state, if necessary, by right-clicking on another state and selecting **Set As Default** from the context menu. The **Solo** and **Mute** checkboxes on each transition are used to control the behaviour of **animation previews**. Refer to [this page](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSoloMute.html) for further details.
A new state can be added by right-clicking on an empty space in the **Animator Controller Window** and selecting **Create State- >Empty** from the context menu. Alternatively, you can drag an animation into the Animator Controller Window to create a state containing that animation. (Note that you can only drag Mecanim animations into the Controller. Non-Mecanim animations will be rejected.) States can also contain [Blend Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html).
## Any State
**Any State** is a special state which is always present. It exists for the situation where you want to go to a specific state regardless of which state you are currently in. This is a shorthand way of adding the same outward transition to all states in your machine. Note that the special meaning of **Any State** implies that it cannot be the end point of a transition (for example, jumping to **Any State** cannot be used as a way to pick a random state to enter next).
![The Any State in the Animator Controller window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnyState.png) The Any State in the Animator Controller window.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)
State Machine Basics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html)
Animation Parameters
