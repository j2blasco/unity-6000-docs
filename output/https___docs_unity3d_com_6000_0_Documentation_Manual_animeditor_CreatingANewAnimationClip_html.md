* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
  * Create a new Animation Clip


[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-UsingAnimationEditor.html)
Use the Animation view
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimatingAGameObject.html)
Animate a GameObject
# Create a new Animation Clip
To create a new **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip), do the following:
  1. Select a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. Go to **Window** > **Animation** > **Animation** to open the **Animation Window** ,


If the GameObject is not assigned an animation clip, the Create button displays in the centre of the Animation Window.
![Use the Create button to create a new Animation Clip and assign it to the selected GameObject](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorNewClip.png) Use the Create button to create a new Animation Clip and assign it to the selected GameObject
Click the **Create** button. Unity prompts you to save your new empty Animation Clip in your **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) folder. When you save this new empty Animation Clip, Unity does the following:
  * Creates a new Animator Controller Asset.
  * Adds the new clip into the Animator Controller as the default state.
  * Adds an **Animator Component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent) to the selected GameObject.
  * Assigns the new Animator Controller to the Animator Component.


The required elements of the animation system are set up. You can begin animating the GameObject.
## Create another Animation Clip
If the selected GameObject already has one or more Animation Clips assigned and you open the Animation window, the Create button is not displayed. Instead, one of the animation clips assigned to the selected GameObject is displayed.
To switch between Animation Clips, use the menu in the top-left of the Animation window, under the playback controls.
To create a new Animation Clip on a GameObject that has existing animations, select **Create New Clip** from this menu. Unity prompts you to save your new empty Animation Clip.
![Option to create a new animation clip](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorNewClipMenu.png) Option to create a new animation clip
## How it fits together
The above steps automatically set up the components and assets needed to animate a GameObject. It is useful to understand how these components, clips, and assets connect together:
  * A GameObject must have an **Animator** component
  * The Animator component must have an **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) Asset assigned
  * The Animator Controller asset must have one or more Animation Clips assigned


The diagram below shows how Unity assigns these components and assets, starting from a new Animation Clip.
![How animation clips, components, and assets are linked together](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationNewClipAutoSetup.png) How animation clips, components, and assets are linked together
After you create a new Animation Clip, the follow happens:
  * The Animation Window displays a timeline with a white playback line. The `Cube Animation Clip` clip is selected in the clip menu.
  * In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, the Cube GameObject has an Animator Component. The **Controller** field is assigned the `Cube` Animator Controller Asset.
  * The **Project Window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) has two new Assets: the `Cube` Animator Controller asset and the `Cube Animation Clip` animation clip asset.
  * The **Animator Window** The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow) displays the contents of the `Cube` Animator Controller asset. The `Cube Animation Clip` is set as the default state, as indicated by the orange color.

![New Animation Clip in the Project Window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorNewAnimationAdded.png) New Animation Clip in the Project Window
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-UsingAnimationEditor.html)
Use the Animation view
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimatingAGameObject.html)
Animate a GameObject
