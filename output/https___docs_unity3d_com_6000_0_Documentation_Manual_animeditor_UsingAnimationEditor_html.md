* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-UsingAnimationEditor.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
  * Use the Animation view


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
Animation window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html)
Create a new Animation Clip
# Use the Animation view
Use the **Animation view** to preview and edit **Animation Clips** for animated **GameObjects** in Unity. To open the Animation view in Unity, go to **Window** > **Animation**.
## Viewing Animations on a GameObject
The **Animation window** is linked to the Hierarchy window, the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view, and the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. Like the Inspector, the Animation window shows the timeline and **keyframes** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) of the Animation for the currently selected **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) or **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) Asset. You can select a GameObject using the Hierarchy window or the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView), or select an Animation Clip Asset using the Project Window.
## The Animated Properties list
In the image below, the Animation view (left) shows the Animation used by the currently selected GameObject, and its child GameObjects if they are also controlled by this Animation. The Scene view and Hierarchy view are on the right, demonstrating that the Animation view shows the Animations attached to the currently selected GameObject.
![Animation view displays the animated properties of the selected GameObject.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorShowsSelected.jpg) Animation view displays the animated properties of the selected GameObject.
In the left side of the Animation view is a list of the animated properties. In a newly created clip where no animation has yet been recorded, this list is empty.
![The Animation view displays no properties when the selected GameObject has no animation.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationWindowEmptyClip.png) The Animation view displays no properties when the selected GameObject has no animation.
When you begin to animate various properties within this clip, the animated properties will appear here. If the animation controls multiple child objects, the list will also include hierarchical sub-lists of each child object’s animated properties. In the example above, various parts of the Robot Arm’s GameObject hierarchy are all animated within the same animation clip.
When animating a hierarchy of GameObjects within a single clip like this, make sure you create the Animation on the root GameObject in the hierarchy.
Each property can be folded and unfolded to reveal the exact values recorded at each keyframe. The value fields show the interpolated value if the playback head (the white line) is between keyframes. You can edit these fields directly. If changes are made when the playback head is over a keyframe, the keyframe’s values are modified. If changes are made when the playback head is between keyframes (and therefore the value shown is an interpolated value), a new keyframe is created at that point with the new value that you entered.
## The Animation Timeline
On the right side of the Animation View is the timeline for the current clip. The keyframes for each animated property appear in this timeline. The timeline view has two modes, **Dopesheet** and **Curves**. To toggle between these modes, click **Dopesheet** or **Curves** at the bottom of the animated property list. These modes offer two views of the Animation timeline and keyframe data.
### Dopesheet mode
**Dopesheet** mode offers a more compact view, allowing you to view each property’s keyframe sequence in an individual horizontal track. This allows you to view a simple overview of the keyframe timing for multiple properties or GameObjects.
![Dopesheet mode displays the keyframe positions of all animated properties within the Animation clip.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorDopeSheetView.png) Dopesheet mode displays the keyframe positions of all animated properties within the Animation clip.
Consult [Key manipulation in Dopesheet mode](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AdvancedKeySelectionAndManipulation.html) for more information.
### Curves mode
**Curves** mode displays a resizable graph containing a view of how the values for each animated property changes over time. All selected properties appear overlaid within the same graph view. This mode allows you to have great control over viewing and editing the values, and how they are interpolated between.
![The Animation Window displays an animation clip with the rotation data for four selected GameObjects.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorCurvesViewMultipleSelected.png) The Animation Window displays an animation clip with the rotation data for four selected GameObjects.
### Fitting your selection to the window
When using **Curves** mode to view your Animation, it’s important to understand that sometimes the various ranges for each property can differ greatly. For example, consider a simple Animation clip for a spinning bouncing cube. The bouncing Y position value may vary between the range 0 to 2 (meaning the cube bounces 2 units high during the animation); however, the rotation value goes from 0 to 360 (representing its degrees of rotation). When viewing these two curves at the same time, the **animation curves** Allows you to add data to an imported clip so you can animate the timings of other items based on the state of an animator. For example, for a game set in icy conditions, you could use an extra animation curve to control the emission rate of a particle system to show the player’s condensing breath in the cold air. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationCurvesOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationCurves) for the position values will be very difficult to make out because the view will be zoomed out to fit the 0–360 range of the rotation values within the window:
![The position and rotation curves of a bouncing spinning cube are both selected. Because the view is zoomed out to fit the 0-360 range of the rotation curve, the bouncing Y position curve is not easily discernible.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorTwoCurvesBigRangeDifference.png) The position and rotation curves of a bouncing spinning cube are both selected. Because the view is zoomed out to fit the 0–360 range of the rotation curve, the bouncing Y position curve is not easily discernible.
Press **F** on the keyboard to zoom the view to the currently selected keyframes. This is useful as a quick way to focus and re-scale the window on a portion of your Animation timeline for easier editing.
![Animation window zoomed in on a few selected keyframes of an animation.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorSelectedKeyframesFitView.png) Animation window zoomed in on a few selected keyframes of an animation.
Click on individual properties in the list and press **F** on the keyboard to automatically re-scale the view to fit the range for that value. You can also manually adjust the zoom of the **Curves** window by using the drag handles at each end of the view’s scrollbar sliders.
Press **A** on the keyboard to fit and re-scale the window to show all the keyframes in the clip, regardless of which ones are selected. This is useful if you want to view the whole timeline while preserving your current selection:
![Animation window zoomed out to display all the keyframes of an animation.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorSelectedKeyframesAllView.png) Animation window zoomed out to display all the keyframes of an animation.
### Playback and frame navigation controls
To control playback of the **Animation Clip** , use the **Playback Controls** at the top left of Animation view.
![Frame navigation](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorFrameNavigation.png) Frame navigation
From left-to-right, these controls are:
  * Preview mode (toggle on/off).
  * Record mode (toggle on/off). Note: Preview mode is on when record mode is on.
  * Move the playback head to the beginning of the clip.
  * Move the playback head to the previous keyframe.
  * Play the Animation Clip starting from the location of the playback head.
  * Move the playback head to the next keyframe.
  * Move the playback head to the end of the clip.
  * The location of the playback head in frames or seconds. Edit this field to move the playhead to a specific location.


You can also control the playback head with the following keyboard shortcuts:
  * Press Comma (,) to go to the previous frame or second.
  * Press Period (.) to go to the next frame or second.
  * Hold Alt (macOS: Option) and press Comma (,) to go to the previous keyframe.
  * Hold Alt (macOS: Option) and press Period (.) to go to the next keyframe.


### Locking the window
You can lock the Animation editor window so that it does not automatically switch to reflect the currently selected GameObject in the Hierarchy or Scene. Locking the window is useful if you want to focus on the Animation for one particular GameObject, and still be able to select and manipulate other GameObjects in the Scene.
![The Lock button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorWindowLockIcon.png) The Lock button
To learn more about navigating the Curve view, consult [Using Animation Curves](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimationCurves.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
Animation window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html)
Create a new Animation Clip
