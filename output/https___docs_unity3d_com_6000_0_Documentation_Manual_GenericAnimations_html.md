* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * Importing a model with non-humanoid (generic) animations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)
Importing a model with humanoid animations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
Model Import Settings reference
# Importing a model with non-humanoid (generic) animations
This page contains guidance on importing a model for use with Unity’s [Animation System](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html). For information on creating a model for use with the Animation System, see [Creating models for animation](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html).
The Animation System works with two types of models:
  * A **Humanoid** model is a specific structure, containing at least 15 bones organized in a way that loosely conforms to an actual human skeleton. For information on importing this type of model, see [Importing a model with humanoid animations](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html).
  * A **Generic** model is everything else. This might be anything from a teakettle to a dragon. This page contains guidance on importing this type of model.


For general importing guidance that is applicable to all types of models, see [Importing a model](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html).
## Overview
When Unity imports a **Generic** model, you must tell it which bone is the **Root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rootnode). This effectively defines the model’s **center of mass** Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CenterofMass).
Since there is only one bone to map, Generic setups do not use the [Humanoid Avatar window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html). As a result, preparing to import your non-Humanoid **model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile) into Unity requires fewer steps than for Humanoid models.
  1. [Set up your Rig](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html#RigSetup) as **Generic**.
  2. You can optionally limit the animation that gets imported on certain bones by [defining an Avatar Mask](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html#AvatarMask).
  3. From the **Animation** tab, enable the **Import Animation** option and then set the other Asset-specific properties, .
  4. If the file consists of multiple animations or actions, you can [define specific frame ranges as Animation Clips](https://docs.unity3d.com/6000.0/Documentation/Manual/Splittinganimations.html).
  5. For each **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) defined in the file, you can: 
     * [Set the pose and root transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#ClipProperties)
     * [Optimize looping](https://docs.unity3d.com/6000.0/Documentation/Manual/LoopingAnimationClips.html)
     * [Add curves to the clip](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationCurvesOnImportedClips.html) in order to animate the timings of other items
     * [Add events to the clip](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEventsOnImportedClips.html) in order to trigger certain actions in time with the animation
     * [Discard part of the animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationMaskOnImportedClips.html) similar to using a runtime [Avatar Mask](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html) but applied at import time
     * [Select a different Root Motion Node](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html) to drive the action from
     * [Read any messages from Unity about importing the clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#ImportMessages)
     * [Watch a preview of the animation clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AnimationPreview)
  6. To save your changes, click the **Apply** button at the bottom of the **Import Settings** window or **Revert** to discard your changes.


## Setting up the Rig
From the [Rig tab of the Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html), set the **Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) (animation) type to **Generic**. By default, the **Avatar Definition** property is set to **Create From This Model** and the **Root node** option is set to **None**.
In some cases, you can change the **Avatar Definition** option to **Copy From Other Avatar** to use an Avatar you already defined for another Model file. For example, if you create a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) (skin) in your 3D modeling application with several distinct animations, you can export the Mesh to one FBX file, and each animation to its own FBX file. When you import these files into Unity, you only need to create a single Avatar for the first file you import (usually the Mesh). As long as all the files use the same bone structure, you can re-use that Avatar for the rest of the files (for example, all the animations).
![Generic Rig](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Rig-1.png) Generic Rig
If you keep the **Create From This Model** option, you must then choose a bone from the **Root node** property.
If you decide to change the **Avatar Definition** option to **Copy From Other Avatar** , you need to specify which Avatar you want to use by setting the **Source** property.
You can also change the maximum number of bones that can influence a given vertex with the **Skin Weights** property. By default, this property limits influence to four bones, but you can specify more or fewer.
When you click the **Apply** button, Unity creates a **Generic Avatar** and adds an Avatar sub-Asset under the Model Asset, which you can find in the Project view.
![Avatar appears as a sub-Asset of the imported Model](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimFBXNoAvatar2.png) Avatar appears as a sub-Asset of the imported Model
**Note:** The Generic Avatar is not the same thing as the Humanoid Avatar, but it does appear in the Project view, and it does hold the Root node mapping. However, if you click on the Avatar icon in the Project view to display its properties in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), only its name appears and there is no **Configure Avatar** button.
## Creating an Avatar Mask
You can apply masking to animation clips either during import time, or at runtime. Masking during import time is preferable, because it allows the discarded animation data to be omitted from your build, making the files smaller and therefore using less memory. It also makes for faster processing because there is less animation data to be blended at runtime. In some cases, import masking may not be suitable for your purposes. In that case, you can apply a mask at runtime by creating an **Avatar Mask** A specification for which body parts to include or exclude for an animation rig. Used in Animation Layers and in the importer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AvatarMask) Asset, and [using it in the layer settings](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html) of your **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController).
To create an empty Avatar Mask Asset, you can either:
  * Choose **Create** > **Avatar Mask** from the **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) menu.
  * Click the Model object you want to define the mask on in the **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Project) view, and then right-click and choose **Create** > **Avatar Mask**.


The new Asset appears in the **Project** view:
![The Avatar Mask window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ConfiguringtheAvatar-Mask.png) The Avatar Mask window
You can now choose which bones to include or exclude from a [Transform hierarchy](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html#Transform) and then add the mask to either an [Animation Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationLayer) or add a reference to it under the [Mask](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationMaskOnImportedClips.html)Can refer to a Sprite Mask, a UI Mask, or a Layer Mask [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Mask.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mask) section of the [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)
Importing a model with humanoid animations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
Model Import Settings reference
