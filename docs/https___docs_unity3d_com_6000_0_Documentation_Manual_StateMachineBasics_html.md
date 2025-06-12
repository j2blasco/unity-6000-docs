* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  * State Machine Basics


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
Animation State Machine
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html)
Animation States
# State Machine Basics
The basic idea is that a character is engaged in some particular kind of action at any given time. The actions available will depend on the type of gameplay but typical actions include things like idling, walking, running, jumping, etc. These actions are referred to as **states** , in the sense that the character is in a state where it is walking, idling or whatever. In general, the character will have restrictions on the next state it can go to rather than being able to switch immediately from any state to any other. For example, a running jump can only be taken when the character is already running and not when it is at a standstill, so it should never switch straight from the idle state to the running jump state. The options for the next state that a character can enter from its current state are referred to as **[state transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html)**. Taken together, the set of states, the set of transitions and the variable to remember the current state form a **state machine**.
The states and transitions of a state machine can be represented using a graph diagram, where the nodes represent the states and the arcs (arrows between nodes) represent the transitions. You can think of the current state as being a marker or highlight that is placed on one of the nodes and can then only jump to another node along one of the arrows.
![A graph diagram that represents a state machine with six different states, the transitions between states, and the flow of each transition.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StateMachineDiagram.png) A graph diagram that represents a state machine with six different states, the transitions between states, and the flow of each transition.
The importance of state machines for animation is that they can be designed and updated quite easily with relatively little coding. Each state has an animation associated with it that will play whenever the machine is in that state. This enables an animator or designer to define the possible sequences of character actions and animations without being concerned about how the code will work.
## State Machines
Unity’s **Animation State Machines** A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationStateMachine) provide a way to overview all of the **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) related to a particular character and allow various events in the game (for example user input) to trigger different animations. 
Animation State Machines can be set up from the [Animator Controller Window](https://docs.unity3d.com/6000.0/Documentation/Manual/Animator.html), and they look something like this:
![Animator Controller window with a state machine.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimStateMachine.png) Animator Controller window with a state machine.
State Machines consist of **States** , **Transitions** The blend from one state to another in a state machine, such as transitioning a character from a walk to a jog animation. Transitions define how long the blend between states should take, and the conditions that activate the blend. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Transition) and **Events** and smaller Sub-State Machines can be used as components in larger machines. Refer to [Animation States](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html) and [Animation Transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html)Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineTransitions.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationTransition) for more information.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
Animation State Machine
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html)
Animation States
