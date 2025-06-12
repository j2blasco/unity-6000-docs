* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimatingAGameObject.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
  * Animate a GameObject


[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html)
Create a new Animation Clip
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimationCurves.html)
Use Animation curves
# Animate a GameObject
There are two methods you can use to animate **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the Animation window: **Record mode** and **Preview mode**.
**Record mode** (Also referred to as auto-key mode)
![The Animation Window in Record mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorControlsRecordMode.png) The Animation Window in Record mode
In record mode, Unity automatically adds **keyframes** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) at the location of the playback head when you move, rotate, or modify an animatable property on your animated GameObject. Press the button with the red circle to enable record mode. The Animation window time line is tinted red when in record mode.
**Preview mode:**
![The Animation Window in Preview mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorControlsPreviewMode.png) The Animation Window in Preview mode
In preview mode, modifying your animated GameObject does not automatically add keyframes. You must manually add keyframes each time you modify your GameObject to a desired new state (for example, moving or rotating it). Press the **Preview** button to enable preview mode. The Animation window time line is tinted blue when in preview mode.
In record mode, the **Preview** button is also active, because you are previewing the existing animation and recording new keyframes at the same time.
## Record keyframes
To record keyframes for the selected GameObject, click the **Record** button. This activates Animation Record Mode. During this mode, changes to the GameObject are recorded into the **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip).
![Record button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorAnimationModeButton.png) Record button
Once in **Record mode** you can add keyframes by setting the white Playback head to the desired time in the Animation time line, and then modify your GameObject to the state you want it to be at that point in time.
The changes you make to the GameObject are recorded as keyframes at the current time shown by the white line (the playback head) in the Animation Window.
Any change to an animatable property (such as its position or rotation) will cause a keyframe for that property to appear in the Animation window.
Clicking or dragging in the time line bar moves the playback head and shows the state of the animation at the playback head’s current time.
In the screenshot below you can see the Animation window in record mode. The time line bar is tinted red, indicating record mode, and the animated properties show up with a red background in the inspector.
![Current frame](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorPreviewFrame.jpg) Current frame
You can stop the **Record Mode** at any time by clicking the **Record button** again. When you stop Record mode, the Animation window switches to **Preview mode** , so that you can still see the GameObject in its current position according to the animation time line.
You can animate any property of the GameObject by manipulating it while in Animation Record Mode. Moving, Rotating or Scaling the GameObject adds corresponding keyframes for those properties in the animation clip. Adjusting values directly in the GameObject’s inspector also adds keyframes while in Record mode. This applies to any animatable property in the inspector, including numeric values, checkboxes, colors, and most other values.
Any properties of the GameObject that are currently animated are shown listed in the left-hand side of the Animation Window. Properties which are not animated are not shown in this window. Any new properties that you animate, including properties on child objects, are added to the property list area as soon as you start animating them.
**Transform** properties are special in that the **.x** , **.y** , and **.z** properties are linked, so curves for all three are added at the same time.
You can also add animatable properties to the current GameObject (and its children) by clicking the **Add Property** button. Clicking this button shows a pop up list of the GameObject’s animatable properties. These correspond with the properties you can see listed in the inspector.
![The animatable properties of a GameObject are revealed when you click the Add Property button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorMatchesInspector.png) The animatable properties of a GameObject are revealed when you click the **Add Property** button
When in **Preview mode** or **Record mode** , the white vertical line shows which frame of the **Animation Clip** is currently previewed. The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) and **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) shows the GameObject at that frame of the Animation Clip. The values of the animated properties at that frame are also shown in a column to the right of the property names.
In Animation Mode a white vertical line shows the currently previewed frame.
### Time line
You can click anywhere on the **Animation window time line** to move the playback head to that frame, and preview or modify that frame in the Animation Clip. The numbers in the **time line** are shown as seconds and frames, so 1:30 means 1 second and 30 frames.
![Time Line](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorTimeLine.png) Time Line
Note: The time line is tinted blue in Preview mode and tinted red in Record mode.
## Add keyframes in preview mode
As well as using **Record mode** to automatically add keyframes when you modify a GameObject, you can add keyframes in **Preview mode** by modifying a property on the GameObject, then explicitly choosing to add a keyframe for that property.
In preview mode, animated properties are tinted blue in the Inspector window. When you see this blue tint, it means these values are being driven by the keyframes of the animation clip currently being previewed in the animation window.
![In preview mode, animated fields are tinted blue in the inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorPreviewModifiedInspectorFields.png) In preview mode, animated fields are tinted blue in the inspector
If you modify any of these blue-tinted properties while previewing (such as rotating a GameObject that has its rotation property animated, as in the above screenshot) the GameObject is now in a modified animation state. This is indicated by a change of color in the tint of the inspector field to a pink color. Because you are not in record mode, your modification is not yet saved as a keyframe.
For example, in the screenshot below, the rotation property has been modified to have a Y value of –90. This modification has not yet been saved as a keyframe in the animation clip.
![A modified animated property in preview mode. This change has not yet been saved as a keyframe](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorPreviewModifiedValue.png) A modified animated property in preview mode. This change has not yet been saved as a keyframe
In this modified state, you must manually create a keyframe to “save” this modification. If you move the playback head, or switch your selection away from the animated GameObject, you will lose the modification.
## Add keyframes manually
There are three different ways to manually create a keyframe when you have modified a GameObject in preview mode.
You can add a keyframe by right-clicking the **property label** of the property you have modified, which allows you to either add a keyframe for just that property, or for all animated properties:
![The property label context menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorPropertyContextMenuAddKey.png) The property label context menu
When you have added a keyframe, the new keyframe will be visible in the **animator window** The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow) as a diamond symbol (called out in red in the screenshot below), and the property field will return to a blue tint, indicating that your modification is saved as a keyframe, and that you are now previewing a value that is driven by the animation keyframes.
![With the new keyframe added \(marked in red\), the values in the inspector return to a blue tint.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorPreviewKeyAdded.png) With the new keyframe added (marked in red), the values in the inspector return to a blue tint.
You can also add a keyframe by clicking the **Add Keyframe** button in the Animation window: ![The Add Keyframe Button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEditorAddKeyframeButton.png)
Or, you can add a keyframe (or keyframes) by using the hotkeys K or Shift-K as described below:
## Hotkeys
  * **K** : Key all animated. Adds a keyframe for all animated properties at the current position of the playback head in the animation window.
  * **Shift-K** : Key all modified. Adds a keyframe for only those animated properties which have been modified at the current position of the playback head in the animation window.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html)
Create a new Animation Clip
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimationCurves.html)
Use Animation curves
