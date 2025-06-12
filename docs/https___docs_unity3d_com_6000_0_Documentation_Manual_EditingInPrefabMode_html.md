* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * Edit prefabs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html)
Create prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html)
Instance overrides
# Edit prefabs
To edit a **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) Asset, open it in **Prefab Mode**. Prefab Mode allows you to view and edit the contents of the Prefab Asset separately from any other **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Changes that you make in Prefab Mode affect all instances of that Prefab.
## Entering and exiting Prefab Mode
You can edit a Prefab Asset **in isolation** , or **in context**.
![Left: editing a Prefab in isolation. Right: editing a Prefab in context.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabContextVsIsolation.png) Left: editing a Prefab in isolation. Right: editing a Prefab in context.
  * **In isolation:** When you edit a Prefab in isolation, Unity hides the rest of your current working Scene, and you only see the GameObjects that relate to the Prefab itself (plus, optionally, a pre-set **editing environment** - see below).
  * **In context:** When you edit a Prefab in context, the rest of your current working Scene remains visible, but locked for editing. 


### Editing in isolation
You can begin to edit a Prefab in Prefab Mode in several ways. To open a Prefab Asset and edit it **in isolation** you can do it in the following ways:
  * Double-click the Prefab Asset in the Project window
  * Select a Prefab Asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) and click the **Open Prefab** button in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window

![A Prefab Asset selected in the Project window \(left\), and the Open Prefab button visible in the inspector \(right\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabAssetOpenPrefabButton.png) A Prefab Asset selected in the Project window (left), and the Open Prefab button visible in the inspector (right)
When you enter Prefab Mode in isolation, Unity only shows the contents of that Prefab in the ****Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView)** and the Hierarchy window. In the following image, the root of the Prefab is a regular **GameObject** - it doesn’t have the blue Prefab instance icon.
![The Scene view and Hierarchy, with Prefab Mode in isolation](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsSceneAndHierarchyInPrefabMode.png) The Scene view and Hierarchy, with Prefab Mode in isolation
In Prefab Mode, the **Scene** view displays a breadcrumb bar at the top. The rightmost entry is the currently open Prefab. Use the breadcrumb bar to navigate back to the main Scenes or other Prefab Assets that you might have opened.
![The breadcrumb bar at the top of the Scene view, visible when in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsBreadcrumbBar.png) The breadcrumb bar at the top of the Scene view, visible when in Prefab Mode
The **Hierarchy** window displays a Prefab header bar at the top which shows the currently open Prefab. You can use the back arrow in the header bar to navigate back one step, which is equivalent to clicking the previous breadcrumb in the breadcrumb bar in the Scene view.
![The back arrow in the header bar of the Hierarchy window, visible when in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsBackArrow.png) The back arrow in the header bar of the Hierarchy window, visible when in Prefab Mode
### Editing in context
Alternatively, you can open a Prefab Asset **in Context** via an instance of that Prefab. Ways of doing that include:
  * Select a Prefab instance in the Hierarchy window and click the **Open** button in the Inspector window
  * Select a Prefab instance in the Hierarchy window and press **P** on the keyboard. This is the default [keyboard binding](https://docs.unity3d.com/6000.0/Documentation/Manual/ShortcutsManager.html)
  * Use the **arrow button** next to the Prefab instance in the Hierarchy window

![The Open button in the Inspector when a Prefab Instance is selected](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabInstanceInspectorOpenButton.png) The Open button in the Inspector when a Prefab Instance is selected ![The arrow button next to a Prefab in the Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabHierarchyOpenArrow.png) The arrow button next to a Prefab in the Hierarchy window
By default, Unity displays the visual representation of the context in gray scale to visually distinguish it from the Prefab contents you edit. However, you can use the **Context:** control in the Prefab bar to set it to any of the following states:
  * **Normal** - Shows the context with its normal colors
  * **Gray** - Shows the context in gray scale
  * **Hidden** - Hides the context entirely so only the Prefab content is visible

![The Prefab Mode controls in the Prefab bar in at the top of the Scene view, including the Context control and the Show Overrides toggle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabModeContextControl.png) The Prefab Mode controls in the Prefab bar in at the top of the Scene view, including the Context control and the Show Overrides toggle
You cannot select the GameObjects that are part of the context, nor do they show in the Hierarchy. This is so you can focus on editing your Prefab without accidentally selecting other unrelated GameObjects, and without having a cluttered Hierarchy window. However, when you move GameObjects around that are part of the Prefab contents, you can use the snapping features in Unity to snap to GameObjects in the context, provided the context is not set to **Hidden**.
In Prefab Mode in Context, Unity displays the Prefab contents at a position that matches that of the Prefab instance it was opened through. This means that you might preview the **root Transform** The Transform at the top of a hierarchy of Transforms. In a Prefab, the Root Transform is the topmost Transform in the Prefab. In an animated humanoid character, the Root Transform is a projection on the Y plane of the Body Transform and is computed at run time. At every frame, a change in the Root Transform is computed, and then this is applied to the GameObject to make it move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RootTransform) of the Prefab contents with different position and rotation values than the Prefab Asset actually has. 
You cannot edit these values in Prefab Mode in Context. If you need to edit them, you can either open the Prefab in isolation, or select the Prefab Asset in the Project window and edit the values in the Inspector.
Apart from the root Transform properties, you can also override other properties of a Prefab instance, which might drastically change its appearance compared to the Prefab Asset it’s an instance of. To preview these overridden values from the Prefab instance, while in Prefab Mode in Context enable the **Show Overrides** toggle in the Prefab bar. While this setting is enabled, any properties that you override on the Prefab instance are previewed the same way on the Prefab contexts and you cannot edit them. To edit those properties, disable the **Show Overrides** toggle again.
## Auto Save
Prefab Mode has an **Auto Save** setting in the top right corner of the Scene view. When it is enabled, Unity automatically saves any changes that you make to a Prefab to the Prefab Asset. **Auto Save** is on by default.
![The Auto Save toggle in the upper right corner of the Scene view in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsAutoSave.png) The Auto Save toggle in the upper right corner of the Scene view in Prefab Mode
If you want to make changes without automatically saving those changes to the Preset Asset, disable the **Auto Save** checkbox. In this case, Unity asks you if you want to save unsaved changes or not when you exit Prefab Mode for the current Prefab. If editing a Prefab in Prefab Mode seems slow, turning off **Auto Save** might help.
## Changing between isolation or in context mode
When you open Prefab Mode via a Prefab Asset, Unity displays the contents of the Prefab in isolation. However, when you open Prefab Mode via a Prefab instance in the Hierarchy window, this opens **Prefab Mode in Context**. 
When you open Prefab Mode this way, you can see the context of the Prefab instance in the Scene view even though you are not editing the instance but rather the Prefab Asset itself. For example, if you open Prefab Mode in Context via a Prefab instance in a Scene, then you can see the surroundings in that Scene while you edit the Prefab. The Prefab is also shown with the same lighting conditions as in the Scene.
![A Prefab opened in Prefab Mode in Context, with the surrounding context displayed in gray scale](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabModeContextView.png) A Prefab opened in Prefab Mode in Context, with the surrounding context displayed in gray scale
If you have a Prefab instance that you do not want to open in context, but want to open in isolation, hold down the **Alt** key and click the **Open** button or the arrow button to open Prefab Mode. You can also set up a custom shortcut in the **Shortcuts** window for the command **Stage > Edit Prefab in Isolation**.
## Undo
When you make changes to a Prefab Asset while in Prefab Mode, you can only undo those changes while still in Prefab Mode. Once you exit Prefab Mode for a given Prefab Asset, your edits relating to that Prefab Asset are no longer available in the undo history.
## Editing Environment
You can assign a Scene as an **editing environment** to be used with Prefab Mode in Isolation. This allows you to edit your Prefab against a backdrop of your choosing rather than an empty Scene. This can be useful to see how your Prefab looks against a specific scenery of your choice. Unity only uses this editing environment when you open Prefab Mode in Isolation.
You cannot select the GameObjects in the Scene that you assign as the editing environment when in Prefab Mode, nor do they show in the Hierarchy. This is so you can focus on editing your Prefab without accidentally selecting other unrelated GameObjects, and without having a cluttered Hierarchy window.
To set a Scene as the editing environment, open the[ Editor](https://docs.unity3d.com/Manual/class-EditorManager.html) window (top menu: **Edit > Project Settings**, then select the **Editor** category) and go to the **Prefab Editing Environment** section. Use the **Regular Environment** setting for “non-UI” Prefabs, and the **UI Environment** setting for UI Prefabs. UI Prefabs are those which have a [Rect Transform](https://docs.unity3d.com/Manual/class-RectTransform.html) component on the root, rather than a regular Transform component. “non-UI” Prefabs are those which have a regular Transform component.
![Prefab editing environment settings in the Editor Project Settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PrefabsEnvironmentSettings1.png) Prefab editing environment settings in the Editor Project Settings
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html)
Create prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html)
Instance overrides
