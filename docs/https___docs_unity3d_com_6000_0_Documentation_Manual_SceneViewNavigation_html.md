* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * Scene view navigation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html)
Position GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html)
Scene view Camera
# Scene view navigation
By default, you look through and control the [Scene Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html) when you navigate through the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view. To look through and control a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that has a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) component attached to it, use the [Cameras overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-overlay.html). 
You can use the following navigation controls to move the Scene Camera or a [GameObject that has a camera component attached to it](https://docs.unity3d.com/6000.0/Documentation/Manual/control-camera.html) around the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView):
  * The [Orientation overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#gizmo)
  * The [Move, Orbit and Zoom](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#tools) tools
  * The [Center](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#center) tool


## Orientation overlay
The Orientation overlay appears in the Scene view. This displays the Scene Camera’s current orientation, and allows you to change the viewing angle and projection mode.
![The scene cameras current orientation](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Editor-SceneGizmo.png) The scene camera’s current orientation
The Orientation overlay has a conical arm on each side of the cube. The arms at the forefront are labelled **X** , **Y** , and **Z**. Click on any of the conical axis arms to snap the Scene Camera to the axis it represents (for example: top view, left view, and front view). You can also right-click the cube to see a menu with a list of viewing angles. To return to the default viewing angle, right-click the Orientation overlay and select **Free**.
You can also toggle **Perspective** on and off. This changes the projection mode of the Scene view between **Perspective** and **Orthographic** (sometimes called “isometric”). To do this, click the cube in the center of the Orientation overlay, or the text below it. The Orthographic view has no perspective, and is useful in combination with clicking one of the conical axis arms to get a front, top or side elevation.
![A Scene shown in Perspective mode \(left\) and Orthographic mode \(right\) ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-view-perspect-and-ortho.png) A Scene shown in Perspective mode (left) and Orthographic mode (right)  ![The same Scene viewed in top and right view, in orthographic mode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneViewOrthoTopAndSide.png) The same Scene viewed in top and right view, in orthographic mode
If your Scene view is in an awkward viewpoint (upside-down or just an angle you find confusing), **Shift** -click the cube at the center of the Orientation overlay to get back to a **Perspective** view with an angle that looks at the Scene from the side and slightly from above.
Click on the padlock on the top right of the Orientation overlay to enable or disable rotation of the Scene. Once Scene rotation is disabled, right-click to pan the view instead of rotating it. This is the same as the [View tool](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#handtool).
Note that in **2D Mode** , the Orientation overlay doesn’t appear. The only view option in **2d Mode** is to look perpendicularly at the XY plane.
### Mac trackpad gestures
On a Mac with a trackpad, you can drag with two fingers to zoom the view.
You can also use three fingers to simulate the effect of clicking the arms of the Orientation overlay: drag up, left, right or down to snap the Scene Camera to the corresponding direction. You must enable three-finger swiping in the MacOS trackpad gesture settings to use this feature. 
## Move, orbit and zoom in the Scene view
Moving, orbiting, and zooming are key operations in Scene view navigation. Unity provides several ways to perform them for maximum accessibility:
  * [Use the arrow keys](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#arrow)
  * [Use the View tool](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#handtool)
  * [Use flythrough mode](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#flythrough)
  * [Change the move speed of the camera](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#speed)
  * [Use movement shortcuts](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#shortcuts)


### Use the arrow keys
You can use the **Arrow Keys** to move around the Scene as though “walking” through it. The Up and Down arrow keys move the Camera forward and backward in the direction it faces. The Left and Right arrow keys pan the view sideways. Hold down the **Shift** and an arrow key to move faster.
### Use the View tool
When the View tool is selected (shortcut: **Q**), the following mouse controls are available:
**Control** | **Description**  
---|---  
**Pan** |  ![In View tool mode, the Move icon appears](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Editor-MoveTool.png)  
  
Click and drag to pan the Camera around.  
**Orbit** |  ![When you hold down the Alt button in View tool mode, the Orbit icon appears](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Editor-EyeTool.png)   
  
Hold **Alt** (Windows) or **Option** (macOS), and left-click and drag to orbit the Camera around the current pivot point.   
  
This option isn’t available in 2D mode, because the view is orthographic.   
**Note** : If you can’t orbit the Camera, make sure that the padlock on the top right of the [Orientation overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#gizmo) is disabled.  
**Zoom** |  ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Editor-ZoomTool.png)   
  
Hold **Alt** (Windows) or **Option** (macOS), and right-click and drag to zoom the Scene view.   
  
On macOS, you can also hold **Control** , and left-click and drag instead.  
Hold down **Shift** to increase the rate of movement and zooming.
### Use flythrough mode
Use the **Flythrough mode** A Scene view navigation mode that allows you to fly around the scene in first-person, similar to how you would navigate in many games. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#flythrough)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Flythroughmode) to fly around the Scene view in first-person, similar to how you would navigate in many games.
Flythrough mode is designed for **Perspective Mode**. In **Orthographic Mode** , if you click and hold the right mouse button and move your mouse, your view orbits the Camera instead.
Flythrough mode isn’t available in 2D mode. In 2D mode, if you click and hold the right mouse button and move your mouse, your view pans around the Scene view. 
To enter **Flythrough mode** and navigate through the Scene view in **Flythrough mode** :
  1. Click and hold the right mouse button.
  2. Do the following to navigate through the Scene view: 
     * Use your mouse to move the view.
     * To move forward or backward, press **W** or **S**.
     * To move left or right, press **A** or **D**.
     * To move up or down, press **Q** or **E**.
     * To move faster, press and hold **Shift**.


### Change the move speed of the camera
The [Scene Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html) displays the Scene view in the Editor. By default, the Scene Camera is what you control and look through when you navigate through the Scene view. To learn how to control a GameObject that has a camera component attached, refer to [Control a camera in first person](https://docs.unity3d.com/6000.0/Documentation/Manual/control-camera.html).
To change the speed that a Camera moves at in the Scene view, select the Camera icon in the View Options [overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/overlays.html) then adjust the value of the **Camera Speed** property to the speed you want. 
**Note** : To find the View Options overlay, press **`** to open the Overlays menu. In the Overlays menu, hover over **View Options** to highlight the View Options overlay in the Scene view.
In **Flythrough mode** , use the scroll wheel on your mouse or drag two fingers on a trackpad to change the speed that the Scene Camera moves at through the Scene. 
### Movement shortcuts
For extra efficiency, these controls can also be used regardless of which transform tool is selected. The most convenient controls depend on which mouse or track-pad you are using.
**Action** | **3-button mouse** | **2-button mouse or track-pad** | **Mac with only one mouse button or track-pad**  
---|---|---|---  
**Pan** | Hold the middle-mouse button then drag | Hold **Alt** +**Control** +left-click, then drag | Hold **Option** +**Command** +left-click, then drag  
**Orbit** (Not available in 2D mode) | Hold **Alt** +left-click, then drag | Hold **Alt** +left-click, then drag | Hold **Option** +left-click, then drag  
**Zoom** | Use the scroll wheel, or hold **Alt** +right-click, then drag | Hold **Alt** +right-click, then drag | Use the two-finger swipe method to scroll in and out, or hold **Option** +**Control** +left-click, then drag  
**Change speed**(only available in Flythrough mode) | Use the scroll wheel while moving. | Drag with two fingers while moving | Drag with two fingers while moving  
## Center the view on a GameObject
To center the Scene view on a GameObject, select the GameObject in the Hierarchy, then move the mouse over the Scene view and press **F**. If the GameObject is already selected, **F** zooms in to the pivot point. This feature can also be found in the menu bar under **Edit** > **Frame Selected**.
To lock the view to the GameObject even when the GameObject is moving, press **Shift+F**. This feature is also in the menu bar under **Edit** > **Lock View to Selected**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html)
Position GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html)
Scene view Camera
