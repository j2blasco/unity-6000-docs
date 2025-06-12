* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  * State Machine Behaviours


[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-AdditionalOptions.html)
Common Blend Tree Options
[](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedStateMachines.html)
Sub-State Machines
# State Machine Behaviours
A **State Machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine) Behaviour is a special class of script. In a similar way to attaching regular Unity **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) (MonoBehaviours) to individual **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), you can attach a StateMachineBehaviour script to an individual state within a state machine. This allows you to write code that will execute when the state machine enters, exits or remains within a particular state. This means you do not have to write your own logic to test for and detect changes in state.
A few examples for the use of this feature might be to:
  * Play sounds as states are entered or exited
  * Perform certain tests (eg, ground detection) only when in appropriate states
  * Activate and control special effects associated with specific states


State Machine Behaviours can be created and added to states in a very similar way to the way you would create and add scripts to GameObjects. Select a state in your state machine, and then in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) use the “Add Behaviour” button to select an existing StateMachineBehaviour or create a new one.
![A state machine with a behaviour attached to the Grounded state](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StateMachineBehaviourAttached.png) A state machine with a behaviour attached to the “Grounded” state
State Machine Behaviour scripts have access to a number of events that are called when the Animator enters, updates and exits different states (or sub-state machines). There are also events which allow you to handle the **Root motion** Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootMotion) and Inverse **Kinematics** The geometry that describes the position and orientation of a character’s joints and bodies. Used by inverse kinematics to control character movement.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#kinematics) calls.
For more information see the [State Machine Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html) script reference.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-AdditionalOptions.html)
Common Blend Tree Options
[](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedStateMachines.html)
Sub-State Machines
