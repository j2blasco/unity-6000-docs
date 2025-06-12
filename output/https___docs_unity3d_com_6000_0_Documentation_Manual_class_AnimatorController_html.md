* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Animator Controller


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html)
Animator component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorControllerCreation.html)
Create an Animator Controller
# Animator Controller
Use an **Animator Controller** to arrange and maintain a set of **Animation Clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) and associated **Animation Transitions** Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineTransitions.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationTransition) for a character or an animated **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). 
In most situations, it’s normal to have multiple animations and transition between them when certain game conditions occur. For example, you could transition from a walk animation to a jump whenever the spacebar is pressed. However, even if you just have a single animation clip, you still need to place it into an Animator Controller to use it on a Game Object.
The Animator Controller has references to the Animation clips it uses. The Animator Controller manages the various Animation Clips and the Transitions between them using a ****State Machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine)**, which could be thought of as a flow-chart of Animation Clips and Transitions. you can find more information about state machines [here](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html).
![A simple Animator Controller](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimAnimatorControllerWindow.png) A simple Animator Controller
Unity automatically creates an Animator Controller when you begin animating a GameObject using the Animation Window, or when you attach an Animation Clip to a GameObject.
To manually create an Animator Controller, right-click within either column of the Project window and select **Create** > **Animator Controller**.
The following topics provide more details on the Animator Controller Asset and state machines:
  * [Create an Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorControllerCreation.html)
  * [Animator Controller Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/Animator.html)
  * [Animator Window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationStateMachine)


## Navigation
Use the scroll wheel to zoom in and zoom out of the Animator Controller window.
To focus on an item in the Animator Controller window, select one or multiple states (click or drag a selection box around the states you wish to select), then press the F key to zoom in on the selection.
![Focus on selected states](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/classAnimatorController-Focus.jpg) Focus on selected states
Press the A key to fit all of the animation states into the Animator Controller view.
Unity preserves your selection. Press the A and F keys to switch between your selected animation states and the entire Animator Controller.
![Unity automatically fits all states in the Animator Controller view when the A key is pressed](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/classAnimatorController-Autofit.jpg) Unity automatically fits all states in the Animator Controller view when the A key is pressed
During Play Mode, the Animator pans the view so that the current state being played is always visible. The Animator Controller respects the independent zoom factors of the Base Layer and Sub-State Machine, and the window pans automatically to ensure visibility of the active state or states.
To modify the zoom during Play Mode, follow these steps:
  1. Enable **Auto Live Link** in the Animator Controller window.
  2. Click the Play button to enter Play Mode.
  3. Click Pause.
  4. In the Animator Controller, select the state or states you want to zoom into.
  5. Press the F key to zoom into the selection.
  6. Click the Play button again to resume Play Mode.


Note that the Animator Controller pans to each state when it activates.
![The Animator pans to the active state](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/classAnimatorController-Pans.png) The Animator pans to the active state
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html)
Animator component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorControllerCreation.html)
Create an Animator Controller
