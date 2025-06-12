* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationsImport.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * Animation from external sources


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
Animation clips
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
Animation window
# Animation from external sources
Animation from external sources are imported into Unity in the same way as regular 3D files. These files, whether they’re generic FBX files or recognized 3D software formats such as Autodesk® Maya®, Cinema 4D, Autodesk® 3ds Max®, or Blender™, can contain animation data in the form of a linear recording of the movements of objects within the file.
![An imported FBX 3D Asset containing an animation titled Run](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationSelectingImportedClip.png) An imported FBX 3D Asset containing an animation titled `Run`
Sometimes, the object you want to animate (for example, a character) and its animations are in the same file. In other cases, the animations might exist in a separate file from the object you want to animate.
It may be that animations are specific to a particular model, and cannot be re-used on other models. For example, a giant octopus end-boss in your game might have a unique arrangement of limbs and bones, and its own set of animations.
In other situations, it may be that you have a library of animations which are to be used on various different models in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). For example, a number of different humanoid characters might all use the same walk and run animations. In these situations, it’s common to have a simple placeholder model in your animation files for the purposes of previewing them. Alternatively, it is possible to use animation files even if they have no geometry at all, just the animation data.
When importing multiple animations, the animations can each exist as separate files within your project folder, or you can extract multiple **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) from a single FBX file if exported as takes from MotionBuilder or with a **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) or script for Autodesk® Maya®, Autodesk® 3ds Max® or other 3D packages. You might want to do this if your file contains multiple separate animations arranged on a single timeline. For example, a long motion captured timeline might contain the animation for a few different jump motions, and you may want to cut out certain sections of this to use as individual clips and discard the rest. Unity provides animation cutting tools to achieve this when you import all animations in one timeline by allowing you to select the frame range for each clip.
## Import animation files
Before you can use any animation in Unity, you must first import it into your project. Unity can import Autodesk® Maya® (.mb or .ma), Autodesk® 3ds Max® (.max), and Blender™ (.blend), and also generic FBX files which [you can export from most animation software](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html). Note that importing from .blend files requires a local installation of Blender™.
For more information, consult [Importing](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html).
## View and copy data from imported animation files
You can view the **keyframes** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) and curves of imported animation clips in the Animation window. If these imported clips have many bones with many keyframes, the amount of animation data can be overwhelming. For example, the following image shows bones and keyframes for a run animation:
![Imported animation clips contain many keyframes and curves.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationViewingImportedCurves.jpg) Imported animation clips contain many keyframes and curves.
To limit the animation data being displayed, select only the bones you are interested in examining. The Animation window displays only the keyframes or curves for the selected bones.
![Limit the view to only the selected bones or properties.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationViewingImportedCurvesSelected.png) Limit the view to only the selected bones or properties.
When viewing imported Animation keyframes, the Animation window provides a read-only view of the animation data. You cannot edit this data, but you can edit a copy of the Animation data by copying and pasting keyframes into a new Animation clip. To create a copy of Animation data from a read only FBX file, follow these steps:
  1. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), select the FBX file with the animation data that you want to copy.
  2. In the Animation window, select the properties to limit the amount of animation data being displayed.
  3. Select the keyframes that you want to copy.
  4. Press **Ctrl+C** (macOS: **Cmd+C**) to copy the selected keyframes.
  5. Create a new empty Animation Clip for the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) where you want to paste the copied keyframes. Consult [Creating a new Animation Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html).
  6. Press **Ctrl-V** (macOS: **Cmd+V**) to paste the copied keyframes.


For best results, the GameObject where you are pasting should have the same hierarchy and properties as the animation data you are copying. For example, if you are copying properties for chest and head movement from an FBX file, the GameObject should have chest and head properties.
![Selected keyframes from an imported clip.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationSelectingKeysOnImportedClip.png) Selected keyframes from an imported clip.
If the GameObject does not have the same properties, the animation data is copied, but the properties are drawn in yellow. Hovering over the name of the property displays the message `The GameObject or Component are missing`.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
Animation clips
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
Animation window
