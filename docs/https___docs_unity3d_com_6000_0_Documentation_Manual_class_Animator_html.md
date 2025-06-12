* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Animator component


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingRootMotion.html)
Scripting Root Motion
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
Animator Controller
# Animator component
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html "Go to Animator page in the Scripting Reference")
Use an **Animator component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent) to assign animation to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The Animator component requires a reference to an [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) which defines which **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) to use, and controls when and how to blend and transition between them.
If the GameObject is a humanoid character with an [Avatar](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html) definition, the Avatar should also be assigned in the Animator component.
![The Animator component with a controller and avatar assigned](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimAnimatorComponent.png) The Animator component with a controller and avatar assigned
## Properties
**Property** | **Function**  
---|---  
**Controller** | The animator controller attached to this character.  
**Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) | The [Avatar](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html) for this character. (If the Animator is being used to animate a humanoid character)  
**Apply Root Motion** | Select whether to control the character’s position and rotation from the animation itself or from script.  
**Update Mode** | This allows you to select when the Animator updates, and which timescale it should use.
  * **Normal** The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normal): The Animator is updated in-sync with the Update call, and the animator’s speed matches the current timescale. If the timescale is slowed, animations will slow down to match.
  * **Animate Physics** : The animator is updated in-sync with the FixedUpdate call (i.e. in lock-step with the physics system). You should use this mode if you are animating the motion of objects with physics interactions, such as characters which can push rigidbody objects around.
  * **Unscaled Time** : The animator is updated in-sync with the Update call, but the animator’s speed ignores the current timescale and animates at 100% speed regardless. This is useful for animating a GUI system at normal speed while using modified timescales for special effects or to pause gameplay.

  
**Culling Mode** | The culling mode you can choose for animations.
  * **Always Animate** : Always animate, don’t do culling even when offscreen.
  * **Cull Update Transforms** : Retarget, IK and write of Transforms are disabled when renderers are not visible.
  * **Cull Completely** : Animation is completely disabled when renderers are not visible.

  
## Animation curve information
The information box at the bottom of the Animator component provides you with a breakdown of the data being used in all the clips used by the Animator Controller.
An animation clip contains data in **animation curves** Allows you to add data to an imported clip so you can animate the timings of other items based on the state of an animator. For example, for a game set in icy conditions, you could use an extra animation curve to control the emission rate of a particle system to show the player’s condensing breath in the cold air. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationCurvesOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationCurves), which represent how a value changes over time. These curves may describe the position or rotation of an object, the flex of a muscle in the **humanoid animation** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation) system, or other animated values within the clip such as a changing material color.
This table explains what each item of data represents:
**Label** | **Description**  
---|---  
**Clip Count** | The total number of animation clips used by the animator controller assigned to this Animator.  
**Curves (Pos, Rot & Scale)** | The total number of curves Unity uses to animate the position, rotation or scale of GameObjects. These are for animated GameObjects that are not part of a standard humanoid rig. When animating a humanoid avatar, these curves would show up a count for extra non-muscle bones such as a tail, flowing cloth or a dangling pendant. If you have a humanoid animation and you notice unexpected non-muscle animation curves, you might have unnecessary animation curves in your animation files.  
**Muscles** | The number of muscle animation curves used for humanoid animation by this Animator. These are the curves used to animate the standard humanoid avatar muscles. As well as the standard muscle movements for all the humanoid bones in Unity’s standard avatar, this also includes two “muscle curves” which store the **root motion** Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootMotion) position and rotation animation.  
**Generic** | The number of numeric (float) curves used by the animator to animate other properties such as material color.  
**PPtr** | The total count of **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) animation curves (used by Unity’s 2d system)  
**Curves Count** | The total combined number of animation curves  
**Constant** | The number of animation curves that are optimized as constant (unchanging) values. Unity selects this automatically if your animation files contain curves with unchanging values.  
**Dense** | The number of animation curves that are optimized using the dense method of storing data (discrete values which are interpolated between linearly). This method uses significantly less memory than the stream method.  
**Stream** | The number of animation curves using the stream method of storing data (values with time and tangent data for curved interpolation). This data occupies significantly more memory than the dense method.  
If your animation clips are imported with **Anim.**Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression)** set to **Optimal** in the [Animation import reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html), Unity will use a heuristic algorithm to determine whether it is best to use the dense or stream method to store the data for each curve.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingRootMotion.html)
Scripting Root Motion
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
Animator Controller
