* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
  * Motion


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationMaskOnImportedClips.html)
Mask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html)
Materials tab
# Motion
Unity uses **root motion** Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootMotion) to displace and orient the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) at the root of the Animator hierarchy for all **Animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip). Sometimes, it is necessary to select a different node to act as the root motion source rather than the designated node.
To select a different Root Motion Node for all animation clips:
  1. Expand the Motion section.
  2. Select the new root motion source from the Root Motion Node menu. This menu list all the objects and nodes under the root of the imported file’s hierarchy. This includes _None_ (designated node) and _**Root Transform** The Transform at the top of a hierarchy of Transforms. In a Prefab, the Root Transform is the topmost Transform in the Prefab. In an animated humanoid character, the Root Transform is a projection on the Y plane of the Body Transform and is computed at run time. At every frame, a change in the Root Transform is computed, and then this is applied to the GameObject to make it move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootTransform)_, your character’s **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) objects, the root bone name, and a submenu for each item with child objects. Each submenu also contains the child object(s) themself and further sub-menus if those objects have child objects.
  3. Select Apply.

![Traverse the hierarchy of objects to select a root motion node](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationInspectorRootNodeSelectionMenu.png) Traverse the hierarchy of objects to select a root motion node
When you select a different Root Motion Node, the newly selected root motion source overrides the manual root motion settings for each imported animation clip. This hides and overriddes the Root Transform Rotation, Root Transform Position (Y), and Root Transform Position (XZ) settings.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationMaskOnImportedClips.html)
Mask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html)
Materials tab
