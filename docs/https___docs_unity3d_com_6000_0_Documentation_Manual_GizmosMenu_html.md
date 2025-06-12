* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * [Gizmos and handles](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html)
  * Gizmos menu


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html)
Gizmos and handles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-handles-programming.html)
Programming with gizmos and handles
# Gizmos menu
The [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) and the [Game view](https://docs.unity3d.com/6000.0/Documentation/Manual/GameView.html) both have a **Gizmos** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) menu. Click the **Gizmos** button in the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) of the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view or the Game view to access the **Gizmos** menu.
![The Gizmos button in the Scene view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/gizmo-button-scene-view.png) The **Gizmos** button in the Scene view ![The Gizmos button in the Game view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/gizmo-button-game-view.png) The **Gizmos** button in the Game view
## General options
**Property** | **Function**  
---|---  
**3D Icons** | The **3D Icons** checkbox controls whether component icons (such as those for Lights and Cameras) are drawn by the Editor in 3D in the Scene view.  
  
When the **3D Icons** checkbox is ticked, component icons are scaled by the Editor according to their distance from the Camera, and obscured by GameObjects in the Scene. Use the slider to control their apparent overall size. When the **3D Icons** checkbox is not ticked, component icons are drawn at a fixed size, and are always drawn on top of any GameObjects in the Scene view.  
  
See [Gizmos and Icons](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons), below, for images and further information.  
**Fade Gizmos** | Fade out and stop rendering gizmos that are small on screen.  
**Selection Outline** | Check **Selection Outline** to display selected GameObjects with a colored outline, and their children with a different colored outline. By default, Unity highlights the selected GameObject in orange, and child GameObjects in blue.  
  
**NOTE:** This option is only available in the Scene view Gizmos menu; you cannot enable it in the Game view Gizmos menu.   
  
See [Selection Outline and Selection Wire](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#SelectionOutlineWire), below, for images and further information.  
**Selection Wire** | Check **Selection Wire** to show the selected GameObjects with their wireframe Mesh visible. To change the colour of the Selection Wire, go to **Edit > Preferences** (macOS: **Unity > Settings**) in the main menu, select **Colors** , and alter the **Selected Wireframe** setting.  
  
This option is only available in the Scene view Gizmos menu; you cannot enable it in the Game view Gizmos menu.  
  
See [Selection Outline and Selection Wire](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#SelectionOutlineWire), below, for images and further information.  
**Display Weights** | When enabled, Unity draws a line from the Light Probe used for the active selection to the positions on the tetrahedra used for interpolation. This is a way to debug probe interpolation and placement problems.  
**Display Occlusion** | When enabled, Unity displays occlusion data for Light Probes if the **Lighting Mode** is set to **Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask).  
**Highlight Invalid Cells** | Enable to highlight tetrahedrons that Unity can’t use for indirect lighting. For example, if the Light Probes are very close together.  
**Recently Changed** | Controls the visibility of the icons and gizmos for components and scripts that you modified recently.  
  
This section appears the first time you change one or more items, and updates after subsequent changes.  
  
For more information, refer to [Built-in components, scripts, and recently changed items](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#Components), below.  
**Scripts** | Controls the visibility of the icons and gizmos for scripts in the Scene.  
  
This section appears only when your Scene uses scripts that meet specific criteria.  
  
For more information, refer to [Built-in components, scripts, and recently changed items](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#Components) below.  
**Built-in Components** | Controls the visibility of the icons and gizmos for all component types that have an icon or gizmo.  
  
For more information, refer to [Built-in components, scripts, and recently changed items](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#Components) below.  
## Light Probe Visualization options
Select which [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) to display in the Scene view. The default value is **Only Probes Used By Selection**.
**Property** | **Function**  
---|---  
**Only Probes Used By Selection** | Display only Light Probes that affect the current selection.  
**All Probes No Cells** | Display all Light Probes.  
**All Probes With Cells** | Display all Light Probes, and the tetrahedrons that Unity uses for interpolation of Light Probe data.  
**None** | Display no Light Probes.  
## Gizmos and Icons
### Gizmos
**Gizmos** are graphics associated with GameObjects in the Scene. Some Gizmos are only drawn when the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. They are usually wireframes, drawn with code rather than bitmap graphics, and can be interactive. The ****Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)** Gizmo and **Light direction** Gizmo (shown below) are both examples of built-in Gizmos; you can also create your own Gizmos using script. See documentation on [Understanding Frustum](https://docs.unity3d.com/6000.0/Documentation/Manual/UnderstandingFrustum.html) for more information about the Camera.
Some Gizmos are passive graphical overlays, shown for reference (such as the **Light direction** Gizmo, which shows the direction of the light). Other Gizmos are interactive, such as the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html) **spherical range** Gizmo, which you can click and drag to adjust the maximum range of the AudioSource.
The **Move** , **Scale** , **Rotate** and **Transform** tools are also interactive Gizmos. See documentation on [Positioning GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html) to learn more about these tools.
![The Camera Gizmo and a Light Gizmo. These Gizmos are only visible when they are selected.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/IconAndGizmoForLightAndCamera.png) The Camera Gizmo and a Light Gizmo. These Gizmos are only visible when they are selected.
See the Script Reference page for the [OnDrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmos.html) function for further information about implementing custom Gizmos in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
### Icons
You can display **icons** in the Game view or Scene view. They are flat, billboard-style overlays which you can use to clearly indicate a GameObject’s position while you work on your game. The **Camera** icon and **Light** icon are examples of built-in icons; you can also assign your own to GameObjects or individual scripts (see documentation on [Assigning Icons](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorOptions.html#assigning-icons) to learn how to do this).
![The built-in icons for a Camera and a Light](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GizmosMenu2.png) The built-in icons for a Camera and a Light ![Left: icons in 3D mode. Right: icons in 2D mode.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GizmoMenu2Dvs3Dicons.png) **Left** : icons in 3D mode. **Right** : icons in 2D mode.
## Selection Outline and Selection Wire
### Selection Outline
When **Selection Outline** is enabled, an outline appears around selected GameObjects and their child GameObjects. By default, Unity outlines selected GameObjects in orange, and child GameObjects in blue. You can change these colors in the Unity preferences (see [Selection Colors](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#SelectionColors), below).
![Selecting a GameObject \(the far left box\) outlines it in orange, and outlines its child GameObjects \(the middle and right boxes\) in blue.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectSelectedOutline.jpg) Selecting a GameObject (the far left box) outlines it in orange, and outlines its child GameObjects (the middle and right boxes) in blue.
When you select a GameObject, Unity outlines all of its child GameObjects (and their child GameObjects, and so on), but does not outline parent GameObjects (or their parent GameObjects, and so on).
![Selecting the middle box highlights it in orange, and highlights its child GameObject \(the far right box\) in blue, but does not highlight its parent GameObject \(the far left box\).](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectSelectedOutlineParentChild.jpg) Selecting the middle box highlights it in orange, and highlights its child GameObject (the far right box) in blue, but does not highlight its parent GameObject (the far left box).
If selected GameObjects extend beyond the edges of the Scene view, the selection outline runs along the edge of the window:
![The selection outline along the edge of the window, when the GameObject you selected extends beyond the Scene view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectSelectedBeyondEdges.png) The selection outline along the edge of the window, when the GameObject you selected extends beyond the Scene view
### Selection Wire
When **Selection Wire** is enabled, then when you select a GameObject in the Scene view or Hierarchy window, the wireframe **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) for that GameObject is made visible in the Scene view:
![The wireframe visible on a mesh](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameObjectSelectedWire.png) The wireframe visible on a mesh
### Selection colors
You can set custom colors for selection wireframes.
  1. Go to **Unity** > **Preferences** (macOS) or **Edit** > **Preferences** (Windows) to open the [Preferences](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html) editor.
  2. On the colors tab, change one or more of the following colors: 
     * **Selected Children Outline** : outline color for selected GameObjects’ children.
     * **Selected Outline** : outline color for selected GameObjects.
     * **Wireframe Selected** : outline color for selected GameObjects’ wireframes.


## Built-in components, scripts, and recently changed items
Use the list in the **Gizmos** menu to control the visibility of icons and gizmos for various components. The list is divided into sections:
![The Gizmos menu, displaying items with custom icons and some recently modified items](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GizmosMenuAll.png) The Gizmos menu, displaying items with custom icons and some recently modified items
### Recently Changed
The **Recently Changed** section controls the visibility of the icons and gizmos for items that you’ve modified recently. It appears the first time you change one or more items. Unity updates the list after subsequent changes.
### Scripts
The **Scripts** section controls the visibility of the icons and gizmos for scripts that:
  * Have an icon assigned to them (see documentation on [Assigning Icons](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorOptions.html#assigning-icons)).
  * Implement the [OnDrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmos.html) function.
  * Implement the [OnDrawGizmosSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html) function.


This section appears when your Scene contains one or more scripts that meet the above criteria.
### Built-in Components
The **Built-in Components** section controls the visibility of the icons and gizmos for all component types that have an icon or gizmo.
Built-in component types that do not have an icon or gizmo shown in the Scene view (for example, Rigidbody) are not listed here.
### Toggling icon visibility
The **icon** column shows or hides the icons for each component type. Full-color icons are displayed in the main Scene view window, faded icons are not.
![The Light icon is faded, indicating that the Editor does not display light icons in the Scene view. The Camera icon is full-color, indicating that the Editor does display camera icons in the Scene view.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/gizmos-icon.png) The **Light** icon is faded, indicating that the Editor does not display light icons in the Scene view. The **Camera** icon is full-color, indicating that the Editor does display camera icons in the Scene view.
To toggle an icon’s visibility in the Scene view, click any icon in the **icon** column.
**Note:** If an item in the list has a gizmo but no icon, the **icon** column for that item is empty.
### Changing script icons
Scripts with custom icons show a small drop-down menu arrow in the **icon** column. To change a custom icon, click the arrow to open the [Select Icon](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorOptions.html#assigning-icons) menu.
![The Select Icon menu for script](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GizmosMenuIconsMenu.png) The Select Icon menu for script
### Toggling gizmo visibility
To control whether the Editor draws gizmo graphics for a particular component type (for example, a **Collider’s** wireframe gizmo or a **Camera’s** [view frustum](https://docs.unity3d.com/6000.0/Documentation/Manual/UnderstandingFrustum.html) gizmo) or script, use the checkboxes in the **Gizmo** column.
  * When a checkbox is checked, the Editor draws gizmos for that component type.
  * When a checkbox is cleared, the Editor does not draw gizmos for that component type.


**Note:** If an item in the list has an icon but no gizmo, the **Gizmo** column for that item is empty.
To toggle gizmo visibility for an entire section (all **Built-in Components** , all **Scripts** , and so on), use the checkboxes next to the section names.
The **Built-in Components** checkbox toggles gizmo visibility for every type of component listed in that section
When the checkbox is toggled on, gizmo visibility is toggled on for one or more item types in the section.
* * *
  * Selection outline for child GameObjects added in [2018.3](https://docs.unity3d.com/2018.3/Documentation/Manual/30_search.html?q=newin20183) NewIn20183
  * Gizmo menu option to toggle Gizmo visibility for all components in a section added in [2019.1](https://docs.unity3d.com/2019.1/Documentation/Manual/30_search.html?q=newin20191) NewIn20191


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html)
Gizmos and handles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-handles-programming.html)
Programming with gizmos and handles
