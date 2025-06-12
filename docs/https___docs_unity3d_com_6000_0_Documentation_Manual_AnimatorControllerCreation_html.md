* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorControllerCreation.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * Create an Animator Controller


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
Animator Controller
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Animator.html)
Animator Controller Asset
# Create an Animator Controller
You can view and set up character behavior from the **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) view (Menu: **Window** > **Animation** > **Animator**).
To create an Animator Controller, do one of the following:
  * Select **Create** > **Animator Controller** from the Project window.
  * Right-click in the Project window and select **Create** > **Animator Controller**.
  * From the Assets menu, select **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) > **Create** > **Animator Controller**.


This creates a `.controller` asset. In the **Project Browser** window.
After the **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine) setup has been made, you can drop the controller onto the **Animator component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent) of any character with an **Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) in the **Hierarchy View**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
Animator Controller
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Animator.html)
Animator Controller Asset
