* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Playables.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Playables API


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorOverrideController.html)
Animator Override Controller
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-Graph.html)
The PlayableGraph
# Playables API
The **Playables** API provides a way to create tools, effects or other gameplay mechanisms by organizing and evaluating data sources in a tree-like structure known as the PlayableGraph. The PlayableGraph allows you to mix, blend, and modify multiple data sources, and play them through a single output.
The Playables API supports animation, audio and **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). The Playables API also provides the capacity to interact with the [animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html) and audio system through scripting.
The following topics provide more details on Playables and the Playables API:
  * [The Playable Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-Graph.html)
  * [ScriptPlayable and PlayableBehaviour](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-ScriptPlayable.html)
  * [Playables Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-Examples.html)


## Playable vs Animation
The animation system already has a graph editing tool, it’s a **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine) system that is restricted to playing animation. The Playables API is designed to be more flexible and to support other systems. The Playables API also allows for the creation of graphs not possible with the state machine. These graphs represent a flow of data, indicating what each node produces and consumes. In addition, a single graph is not limited to a single system. A single graph may contain nodes for animation, audio, and scripts.
## Advantages of using the Playables API
  * The Playables API allows for dynamic animation blending. This means that objects in the **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) could provide their own animations. For example, animations for weapons, chests, and traps could be dynamically added to the PlayableGraph and used for a certain duration.
  * The Playables API allows you to easily play a single animation without the overhead involved in creating and managing an AnimatorController asset.
  * The Playables API allows users to dynamically create blending graphs and control the blending weights directly frame by frame.
  * A PlayableGraph can be created at runtime, adding playable node as needed, based on conditions. Instead of having a huge “one-size-fit-all” graph where nodes are enabled and disabled, the PlayableGraph can be tailored to fit the requirements of the current situation.


* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorOverrideController.html)
Animator Override Controller
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables-Graph.html)
The PlayableGraph
