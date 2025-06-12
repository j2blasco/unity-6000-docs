* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Animation clips


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
Mecanim Animation system
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationsImport.html)
Animation from external sources
# Animation clips
Animation clips are one of the core elements of Unity’s animation system. Unity supports importing animation from external sources. You can create **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) with the Animation window.
## Animation from external sources
You can import the following types of Animation clips from external sources:
  * **Humanoid animations** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation) captured at a motion capture studio.
  * Animations created from scratch by an artist in an external 3D application (such as Autodesk® 3ds Max® or Autodesk® Maya®).
  * Animation sets from third party libraries from Unity’s **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore).
  * Multiple animation clips cut from a single imported motion file.

![An example of an imported animation clip, viewed in Unitys Inspector window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationClipInspector.jpg) An example of an imported animation clip, viewed in Unity’s Inspector window
## Create and edit animation clips within Unity
You can also create and edit animation clips in Unity’s Animation window. These clips can animate:
  * The position, rotation, and scale of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
  * Component properties such as material color, the intensity of a light, and the volume of a sound.
  * Properties within your own **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) including float, integer, enum, vector, and Boolean variables.
  * The timing of calling functions within your own scripts.

![Unitys Animation window used to animate the intensity and range of a point light](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationViewSimpleParameters.png) Unity’s Animation window used to animate the intensity and range of a point light
## Additional resources
  * [Animation From External Sources](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationsImport.html)
  * [Animation Window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)


* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
Mecanim Animation system
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationsImport.html)
Animation from external sources
