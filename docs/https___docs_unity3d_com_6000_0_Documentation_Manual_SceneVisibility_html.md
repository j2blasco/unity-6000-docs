* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * Scene visibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/control-camera.html)
Control a camera in first person
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ViewModes.html)
Scene view Draw Modes and View Options overlays
# Scene visibility
Unity’s **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) visibility controls allow you to quickly hide and display **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) without changing their in-game visibility. This is useful for working with large or complex scenes where it can be difficult to view and select specific GameObjects.
![Selected GameObjects are highlighted in blue](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisExVisible.png) Selected GameObjects are highlighted in blue ![Changing the Scene visibility settings hides the selected GameObjects in the scene view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisExHidden.png) Changing the Scene visibility settings hides the selected GameObjects in the scene view
Using visibility options is safer than [deactivating GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/DeactivatingGameObjects.html) because visibility options only affect the Scene view. This means you can’t accidentally remove GameObjects from the rendered scene, or trigger unnecessary bake jobs for lighting, occlusion, and other systems.
The Editor saves Scene visibility settings to a file called `SceneVisibilityState.asset` in the Project’s `Library` folder. The scene reads from this file and updates it automatically whenever you change the visibility settings. This makes it possible for your settings to persist from one session to the next. Because source control setups for Unity typically ignore the `Library` folder, changing visibility settings should not create source control conflicts.
You can set visibility on specific scene items in the [Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html), but if the scene-wide visibility setting is disabled, items marked as hidden might still appear in the Scene view. To change this setting, you can [toggle Scene visibility on the Toolbar](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html#scenewide-vis).
To control the scene visibility from script, refer to [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html). 
Scene visibility controls are very similar to the [Scene picking](https://docs.unity3d.com/6000.0/Documentation/Manual/ScenePicking.html) controls.
## Set Scene visibility for GameObjects and their children
You control Scene visibility for individual GameObjects from the [Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html).
![Every GameObject has a Scene visibility icon/toggle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisIconsHierarchy.png) Every GameObject has a Scene visibility icon/toggle
To toggle between hiding and showing the GameObject and its children:
  * Click a GameObject’s visibility icon in the [Hierarchy](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html) window, or press **H**.
  * For multiple GameObjects, press **H**.


Toggling visibility for an object and its children affects all child objects, from the “target” object all the way down to the bottom of the hierarchy.
  * **Alt** + Click a GameObject’s visibility icon in the Hierarchy window to toggle between hiding and showing the GameObject only.


Toggling visibility for a single object does not affect its children. They retain whatever visibility status they had previously.
**Tip** : You can also click the [Scene’s visibility icon](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html#scenewide-vis) to toggle between hiding and showing items marked hidden in the Scene.
Because you can toggle visibility for a whole branch or a single GameObject, you can end up with GameObjects that are visible, but have hidden children or parents. To help you track what’s going on, the visibility icon changes to indicate each GameObject’s status.
![GameObject visibility states in the Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisIconsOvw.png) GameObject visibility states in the Hierarchy window Label | Icon | Description  
---|---|---  
**A** | ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisVisibleHiddenChildren.png) | The GameObject is visible, but some of its children are hidden.  
**B** | ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisHiddenVisibleChildren.png) | The GameObject is hidden, but some of its children are visible.  
**C** | ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisVisible.png) | The GameObject and its children are visible. This icon only appears when you hover over the GameObject.  
**D** | ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisHidden.png) | The GameObject and its children are hidden.  
Scene visibility changes you make in the Hierarchy window are persistent. Unity re-applies them whenever you toggle scene visibility off and on again in the Scene view, close and re-open the Scene, and so on.
## Turn Scene visibility on and off
The Scene visibility switch in the [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/ViewModes.html) View Options Overlay **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) shows or hides GameObjects in the scene. Click it to toggle Scene visibility on and off.
![The Scene visibility icon in the View Options Overlay toolbar](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisSceneViewToggle.png) The Scene visibility icon in the View Options Overlay toolbar
Turning Scene visibility off essentially mutes the Scene visibility settings you set in the Hierarchy window, but doesn’t delete or change them. All hidden GameObjects are temporarily visible.
Turning Scene visibility back on re-applies the visibility settings set in the Hierarchy window.
## Isolate selected GameObjects
The Isolation view temporarily overrides the Scene visibility settings so that only the selected GameObjects are visible, and everything else is hidden.
![Isolation view overrides Scene visibility settings so only the selection and its children \(A\) are visible.<br/>Clicking the Exit button \(B\) reverts to the previous Scene visibility settings.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneVisIsolation.png) Isolation view overrides Scene visibility settings so only the selection and its children (A) are visible.  
Clicking the Exit button (B) reverts to the previous Scene visibility settings.
To enter the Isolation view:
  * Press **Shift + H**.
This isolates all selected GameObjects and their children. Isolating hidden GameObjects makes them visible until you exit the Isolation view.


While in the Isolation view, you can continue to change Scene visibility settings, but any changes you make are lost on exit.
To exit the Isolation view:
  * Press **Shift + H** again, or click the **Exit** button in the Scene view.
Exiting the Isolation view reverts back to your original Scene visibility settings.


## Additional resources
  * [Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html)
  * [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * [Scene picking](https://docs.unity3d.com/6000.0/Documentation/Manual/ScenePicking.html)
  * [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/control-camera.html)
Control a camera in first person
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ViewModes.html)
Scene view Draw Modes and View Options overlays
