* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorOverrideController.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Animator Override Controller


[](https://docs.unity3d.com/6000.0/Documentation/Manual/TargetMatching.html)
Target Matching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables.html)
Playables API
# Animator Override Controller
Use an **Animator Override Controller** asset to override the **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) in an **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) while retaining the structure, parameters, and logic of its **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine). You can use this technique to create many variations of the same Animator Controller.
For example, your game has different characters such as a goblin, ogre, and an elf. Each character uses different animation clips for idling, turning, and jogging but the structure, parameters, and logic of each state machine is the same. In this case, you can create a base Animator Controller for all characters and create an Animator Override Controller asset for each character.
The advantage of creating a base Animator Controller is that you only have to modify one Animator Controller to change the gameplay logic, structure, or parameters for all the characters in your game. Also, if you want to add a new character to your game, you only need to create an additional Animator Override Controller asset.
## Set up an Animator Override Controller asset
Before you can use an Animator Override Controller asset, you must first create and define an Animator Controller asset. These steps begin with an already created and defined Animator Controller named `NPC Animator`.
![The Blend Tree for the NPC Animator Controller](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorOverrideControllerOriginalAnimator.png) The Blend Tree for the NPC Animator Controller
To extend an Animator Controller with an Animator Override Controller, follow these steps:
  1. Go to **Assets** > **Create** > **Animation** > **Animator Override Controller** to create a new Animator Override Controller asset in the Project window. You can also use the **Create** button in the Project window.
  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), select the new Animator Override Controller asset to display its settings in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
![An Animator Override Controller with no Animator Controller assigned](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorOverrideControllerUnassigned.png) An Animator Override Controller with no Animator Controller assigned
  3. Rename the Animator Override Controller asset as `Ogre Animator`.
  4. Use the **Controller** field to choose the Animator Controller asset that you want to override. To do this, perform one of the following actions:
  5. Select and drag an Animator Controller asset from the Project window into the Controller field.
  6. Select the Animator Controller picker (⊙) and choose the `NPC Animator Controller` from the window that displays.
![Drag an Animator Controller asset from the Project window to the Controller field](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorOverrideControllerInspector.png) Drag an Animator Controller asset from the Project window to the Controller field
The Inspector window displays the Animator Override Controller with a two column table. The first column displays the animation clips from the original Animator Controller. The second column displays the overriding clips. By default, each override animation clip is the same as the original animation clip. 
  7. Use the fields in the Override column to choose an override animation clip for each original animation clip. For example, the original animation clips in the `NPC Animator` controller are overridden with Ogre versions.
![The Animator Override Controller with Ogre versions of the original animation clips](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorOverrideControllerNewClips.png) The Animator Override Controller with Ogre versions of the original animation clips
In your state machine, you can use seconds or normalized time to set the transition exit time. When you use an Animator Override Controller, make sure the transition exit time is in normalized time.
When in seconds, the exit time might be ignored if you specify an override clip shorter than the transition exit time. When the exit time uses normalized time, the clip exits according to the ratio defined by your state machine. 


## Assign an Animator Override Controller asset
To assign an Animator Override Controller asset to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), follow these steps:
  1. In the Hierarchy window, select the GameObject that will use the Animator Override Controller.
  2. In the Inspector window, locate the Animator Controller component associated with the selected GameObject.
  3. In the Animator Controller component, select `Ogre Animator` as its Animator Controller.


In this example, the Animator Override Controller asset named `Ogre Animator` uses the same logic, transitions, and blends as the original Animator Controller named `NPC Animator`. but plays the animation clips specified in the `Ogre Animator` Override Controller asset.
![The Ogre character uses an Animator Override Controller asset as its Controller in the Animator Component](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorOverrideControllerInUseOnGameObject.png) The Ogre character uses an Animator Override Controller asset as its Controller in the Animator Component
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TargetMatching.html)
Target Matching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables.html)
Playables API
