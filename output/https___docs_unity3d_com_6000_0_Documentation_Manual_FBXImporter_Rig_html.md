* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * Rig tab


[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html)
Model tab Import Settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html)
Avatar Mapping tab
# Rig tab
The settings on the **Rig** tab define how Unity maps the deformers to the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) in the imported model so that you can animate it. For humanoid characters, this means [assigning or creating an avatar](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html). For non-humanoid (generic) characters, this means [identifying a root bone in the skeleton](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html).
To open the Rig tab, select a mesh, and in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) select the **Rig** tab.
## Animation Type
The value you select for the **Animation Type** determines the layout for the **Rig** tab.
By default, when you select a model in the **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Project) view, Unity determines which **Animation Type** best matches the selected model and displays it in the **Rig** tab. If Unity has never imported the file, the Animation Type is set to **None**.
**Property** | **Description**  
---|---  
**None** | No animation present.  
**Legacy** | Use the [Legacy Animation System](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#LegacyRig). Import and use animations as with Unity version 3.x and earlier.  
**Generic** | Use the [Generic Animation System](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#GenericRig) if your rig is non-humanoid (quadruped or any entity to be animated). Unity picks a root node automatically but you can identify another bone to use as the **Root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rootnode) instead.  
**Humanoid** | Use the [Humanoid Animation System](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#HumanoidRig) if your rig is humanoid (it has two legs, two arms and a head). Unity usually detects the skeleton and maps it to the Avatar correctly. In some cases, you may need to set the **Avatar Definition** and configure the mapping manually.  
## Generic animation types
[Generic Animations](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html) do not use Avatars like **Humanoid animations** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation) do. Since the skeleton can be arbitrary, you must specify which bone is the **Root node**. The Root node allows Unity to establish consistency between **Animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) for a generic model, and blend properly between Animations that have not been authored “in place” (that is, where the whole model moves its world position while animating).
Specifying the root node helps Unity determine between movement of the bones relative to each other, and motion of the Root node in the world (controlled from [OnAnimatorMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorMove.html)).
**Property** | **Description**  
---|---  
**Avatar Definition** | Choose where to get the Avatar definition. The following options are available: 
  * **Create from this model** - Create an Avatar based on this model
  * **Copy from Other Avatar** - Point to an Avatar set up on another model.

  
**Root node** | Select the bone to use as a root node for this Avatar.   
  
This setting is only available if you set the **Avatar Definition** to **Create From This Model**.  
**Source** | Copy another Avatar with an identical rig to import its animation clips.   
  
This setting is only available if you set the **Avatar Definition** to **Copy from Other Avatar**.  
**Skin Weights** | Set the maximum number of bones that can influence a single vertex. The following options are available: 
  * **Standard (4 Bones)** - Use a maximum influence of four bones. This is the default, and is recommended for performance.
  * **Custom** - Set your own maximum number of bones. When you select this option, the **Max Bones/Vertex** and **Max Bone Weight** properties appear.

  
**Max Bones/Vertex** | Set the maximum number of bones per vertex to influence a given vertex. You can set between 1 and 32 bones per vertex, but the higher the number of bones you use to influence a vertex, the greater the performance cost.  
  
This setting is only available you set the **Skin Weights** property to **Custom**.  
**Max Bone Weight** | Set the bottom threshold for considering bone weights. The weighting calculation ignores anything smaller than this value, and Unity scales up the bone weights higher than this value to a total of 1.0.  
  
This setting is only available if the **Skin Weights** property is set to **Custom**.  
**Strip Bones** | Enable to only add bones to Skinned **Mesh Renderers** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) that have skin weights assigned to them.  
**Optimize Game Object** | Remove and store the GameObject Transform hierarchy of the imported character in the Avatar and Animator component. If enabled, the SkinnedMeshRenderers of the character use the Unity animation system’s internal skeleton, which improves the performance of the animated characters.   
  
Only available if the **Avatar Definition** is set to **Create From This Model**.  
**Extra Transforms to Expose** | Specify which Transform paths you want Unity to ignore when **Optimize Game Object** is enabled. For more information, see [Including extra Transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#ExtraTransforms).  
  
This section only appears when **Optimize Game Object** is enabled.  
## Humanoid animation types
![Your rig is humanoid \(it has two legs, two arms and a head\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Rig-2.png) Your rig is _humanoid_ (it has two legs, two arms and a head)
With rare exceptions, humanoid models have the same basic structure. This structure represents the major articulated parts of the body: the head and limbs. The first step to using Unity’s [Humanoid animation features](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html) is to [set up and configure](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html) an **Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar). Unity uses the Avatar to map the simplified humanoid bone structure to the actual bones present in the Model’s skeleton. 
**Property** | **Description**  
---|---  
**Avatar Definition** | Choose where to get the Avatar definition. The following options are available: 
  * **Create from this model** - Create an Avatar based on this model
  * **Copy from Other Avatar** - Point to an Avatar set up on another model.

  
**Source** | Copy another Avatar with an identical rig to import its animation clips.   
  
Only available if the **Avatar Definition** is set to **Copy from Other Avatar**.  
**Configure** | Open the [Avatar configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html).   
  
Only available if the **Avatar Definition** is set to **Create From This Model**.  
**Skin Weights** | This property is identical for both Humanoid and Generic Models. Refer to the **Skin Weights** property for [Generic](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#GenericRig) models above for more information.  
**Strip Bones** | Enable to only add bones to Skinned Mesh Renderers that have skin weights assigned to them.  
**Optimize Game Object** | Remove and store the GameObject Transform hierarchy of the imported character in the Avatar and Animator component. If enabled, the SkinnedMeshRenderers of the character use the Unity animation system’s internal skeleton, which improves the performance of the animated characters.   
  
Only available if the **Avatar Definition** is set to **Create From This Model**.  
**Extra Transforms to Expose** | Specify which Transform paths you want Unity to ignore when **Optimize Game Object** is enabled. For more information, see [Including extra Transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#ExtraTransforms).  
  
This section only appears when **Optimize Game Object** is enabled.  
## Including extra Transforms
When you enable the **Optimize Game Object** property, Unity ignores any Transform which is part of the hierarchy but is not mapped in the Avatar, in order to improve CPU performance. However, you can mark specific nodes in the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) hierarchy to include in calculations using the **Extra Transforms to Expose** section:
![The Extra Transforms to Expose property appears when Optimize Game Objects is enabled](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ExtraTransforms.png) The Extra Transforms to Expose property appears when Optimize Game Objects is enabled
**(A)** Enter the full or partial name in the search box to filter the list of Transforms. This makes it easier to navigate through characters with a large number of bones.
**(B)** Enable each Transform (bones of a skeleton) you want Unity to include in calculations.
**(C)** Use the buttons to help select specific Transforms. For example, the **Toggle All** button selects or deselects everything at once (regardless of the current selection, including filtered items).
**(D)** Use the **Revert** button to undo your selections or the **Apply** button to apply the exceptions to the Model.
**Note** : In optimized mode, skinned Mesh matrix extraction is multi-threaded.
## Legacy animation types
**Property** | **Description**  
---|---  
**Generation** | Select the animation import method. The following options are available: 
  * **Don’t Import** - Do not import animation
  * **Store in Original Roots (Deprecated)** - Deprecated. Do not use.
  * **Store in Nodes (Deprecated)** - Deprecated. Do not use.
  * **Store in Root (Deprecated)** - Deprecated. Do not use.
  * **Store in Root (New)** - Import the animation and store it in the Model’s root node. This is the default setting.

  
**Skin Weights** | This property is the same for Legacy as for Humanoid and Generic Models. Refer to the **Skin Weights** property for [Generic](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html#GenericRig) models above for more information.  
**Strip Bones** | Enable to only add bones to Skinned Mesh Renderers that have skin weights assigned to them.  
For more information about legacy animation, refer to the documentation for [Legacy Animation System](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html)
Model tab Import Settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html)
Avatar Mapping tab
