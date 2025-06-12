* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ScenePickingControls.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * [Pick and select GameObjects in the Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/ScenePicking.html)
  * Scene picking controls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SelectionPiercingMenu.html)
Select a GameObject that overlaps with other GameObjects 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html)
Position GameObjects
# Scene picking controls
You can toggle the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) picking status of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to choose which GameObjects are selectable in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). By default, all GameObjects are pickable, which means you can select them in the Scene view. You can disable the pickability of a GameObject to prevent that GameObject from being added to selections in the Scene view. For example, if you are working in a large scene with many GameObjecets, you can temporarily block specific GameObjects from being selected to prevent them from being edited accidentally.
A GameObject that has its scene picking disabled is still rendered in the Scene view, but you cannot select or modify it in the Scene view. The pickability state persists only in the Editor and only for the user in the project where the pickability was set. Changing the pickability state of a GameObject is not recorded as a modification to the scene. 
Scene picking controls are similar to the [Scene visibility](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html) controls.
## Toggle the pickability of a GameObject
Control scene picking status for individual GameObjects from the [Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html).
![Every GameObject has a Scene pickability icon/toggle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-picking-icons-hierarchy.png) Every GameObject has a Scene pickability icon/toggle
To toggle the scene picking status of a GameObject:
  * Select a GameObject’s pickability icon in the [Hierarchy](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html) window to toggle between enabling and disabling picking the GameObject and its children. Toggling pickability for a GameObject and its children affects all child GameObjects, from the target GameObject to the bottom of the hierarchy.
  * For multiple GameObjects, press **L**.
  * Select a GameObject in the Scene view, and press **L** to toggle the pickability of the GameObject and its children.
  * Hold **Alt** (macOS: **Option**) and select a GameObject’s pickability icon in the Hierarchy window to toggle between enabling and disabling picking the GameObject only. Toggling pickability for a single GameObject does not affect its children. They retain whatever pickability status they had previously.


## Pickability icons
You can toggle pickability for a whole branch of GameObjects or a single GameObject, so you can have GameObjects that are selectable but have children or parents that you cannot select. To help you track what is pickable or not, the pickability icon changes to show the status of each GameObject.
Any scene picking changes you make in the Hierarchy window are persistent. Scene picking changes are reapplied whenever you use **Select All** , **Deselect All** , or close and re-open the Scene.
![Unity only selects pickable items when you draw a selection bounding box in the Scene view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-picking-icons-ovw.png) Unity only selects pickable items when you draw a selection bounding box in the Scene view Screenshot annotation | Pickability icon | Description  
---|---|---  
**A** | ![Pick](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScenePickingPickableUnpickableChildren.png) | You can pick the GameObject, but you cannot pick some of its children.  
**B** | ![Cant pick](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScenePickingUnpickablePickableChildren.png) | You cannot pick the GameObject, but you can pick some of its children.  
**C** | ![Cant pick](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScenePickingUnpickable.png) | You cannot pick the GameObject nor its children.  
**D** | ![Pick](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScenePickingPickable.png) | You can pick the GameObject and its children. This icon only appears when you hover over the GameObject.  
## Additional resources
  * [Pick and select GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/ScenePicking.html)
  * [Scene visibility](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html)
  * [Select GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/SelectGameObjects.html)
  * [Select a GameObject that shares space with other GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/SelectionPiercingMenu.html)**


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SelectionPiercingMenu.html)
Select a GameObject that overlaps with other GameObjects 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html)
Position GameObjects
