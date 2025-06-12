* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Retargeting.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Humanoid Avatar](https://docs.unity3d.com/6000.0/Documentation/Manual/AvatarCreationandSetup.html)
  * Retarget Humanoid animations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AvatarCreationandSetup.html)
Humanoid Avatar
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InverseKinematics.html)
Inverse Kinematics
# Retarget Humanoid animations
One of the most powerful features of Mecanim is the ability to retarget **humanoid animations** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation). This means that you can apply the same set of animations to different character models. **Retargeting** is only possible for humanoid models with a configured **Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar). A configured avatar provides the ability to correspondence between the models’ bone structure.
## Recommended Hierarchy structure
When working with Mecanim animations, you can expect your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to contain the following elements:
  * The Imported character model, which has an Avatar on it.
  * The **Animator Component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent), referencing an **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) asset.
  * A set of **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip), referenced from the Animator Controller.
  * **Scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) for the character.
  * Character-related components, such as the **Character Controller** A simple, capsule-shaped collider component with specialized features for behaving as a character in a game. Unlike true collider components, a Rigidbody is not needed and the momentum effects are not realistic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CharacterController).


Your project should also contain another character model with a valid Avatar.
To retarget between character models, follow these steps:
  1. Create a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the Hierarchy that contains Character-related components.
![The MainChar GameObject with its Character Controller component.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimRetargetingTopLevel.png) The MainChar GameObject with its Character Controller component.
  2. Put the model as a child of the GameObject, together with the Animator component.
![The child Kyle_Robot GameObject with its Animator Controller component.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimRetargetingModel.png) The child Kyle_Robot GameObject with its Animator Controller component.
  3. Make sure scripts referencing the Animator are looking for the animator in the children instead of the root. To do this, use `GetComponentInChildren<Animator>()` instead of `GetComponent<Animator>()`.
![The Kyle_Robot character.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimRetargetingKyle.jpg) The Kyle_Robot character.


Then, to reuse the same animations on another model, do the following:
  1. Disable the original model.
  2. Drop in the desired model as another child of GameObject.
![The child Teddy GameObject with its Animator Controller component set to no controller.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimRetargetingOtherModel.png) The child Teddy GameObject with its Animator Controller component set to no controller.
  3. Make sure the Animator Controller property for the new model is referencing the same controller asset.
![The Teddy GameObject with its Animator Controller set to the same controller as the Kyle GameObject.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimRetargetingOtherModelCorrectController.png) The Teddy GameObject with its Animator Controller set to the same controller as the Kyle GameObject.
  4. Tweak the character controller, the transform, and other properties on the top-level GameObject to make sure that the animations work smoothly with the new model.
![The Teddy character.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimRetargetingTed.jpg) The Teddy character.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AvatarCreationandSetup.html)
Humanoid Avatar
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InverseKinematics.html)
Inverse Kinematics
