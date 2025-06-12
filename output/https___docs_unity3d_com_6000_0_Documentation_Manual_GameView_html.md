* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GameView.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * The Game view


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingCustomEditorTools.html)
Custom Editor tools
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator.html)
Device Simulator
# The Game view
![The Game view in the Editor](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/game-view-window.png) The Game view in the Editor
The Game view is rendered from the [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in your application. The Game view displays how your final, built application looks. You need to use one or more [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html) to control what the player sees when they’re using your application. 
The Game view is included in the [default Unity Editor layout](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomizingYourWorkspace.html). If the Game view is not open, go to **Window > General** and select **Game** to open the Game view.
In the Editor, you can toggle between the Game view and the [Simulator view](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-view.html). The [Simulator view](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-view.html) displays how your built application looks on a mobile device.
## Play mode
![The Play mode menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Editor-PlayButtons.png) The Play mode menu
Use Play mode to run your project and test how it works as it would in a built application. 
Use the Play mode control buttons in the [Toolbar](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) to control the Play mode:
  * Press the Play button to switch the Editor to Play mode.
  * Press the Pause button to pause Play mode.
  * Press the Step button to move Play mode forward by one frame.


In Play mode, any changes you make are temporary and are reset when you exit Play mode. When you enter the Play mode, the Editor darkens parts of the interface outside the Game view.
## Using the Simulator view
Use the Simulator view to preview how your built application looks on a mobile device.
To change between Game and [Simulator](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-view.html) views, in the **Game/Simulator** tab, select an option from the **Game/Simulator** menu.
Alternatively, to open the Simulator view, go to **Window > General** and select **Device Simulator**. If there are no instances of the Simulator view open, it opens as a floating window. However, if the Simulator view is already open in the Editor, then trying to open the Simulator view from the menu brings it into focus
## Game view control bar
The Game view control bar is at the top of the Game view and contains options to control the Game view. 
**Property** | **Description**  
---|---  
**Game/Simulator** | Select the **Game** or **[Simulator](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-view.html)** view. Use the Game view to preview how your final, built application looks. Use the Simulator view to preview how your built application looks on a mobile device.  
**Display** | Select a display to render in the Game view. If you have multiple **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with camera components in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), select an option to switch between them. By default, **Display** is set to **Display 1**. You can assign displays to cameras in the Camera component **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), under **Target Display**.  
**Scale slider** | Increase or decrease the scale of the Game view. Scroll right to zoom in and examine areas of the Game view in more detail. This slider lets you zoom out to display the entire screen where the device resolution is higher than the Game view window size. You can also use the scroll wheel and middle mouse button to do this while the application is stopped or paused.  
**Open the Frame Debugger** | Open the [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html) window.  
**Mute audio** | Disable in-application audio when you enter Play mode.  
**Unity Shortcuts** | Disable Editor keyboard shortcuts from triggering during Play mode when the Game view window is not in focus.  
**Stats** | Display or hide the Statistics overlay, which contains [Rendering Statistics](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html) about your application’s audio and graphics. Use the Statistics overlay to monitor the performance of your application in Play mode.  
**Gizmos** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) | Display or hide the [Gizmos menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html). Use the **Gizmos** menu to select Gizmos to hide or display in the Play mode.  
### Aspect ratio options
Test how your game looks on monitors with different aspect ratios. By default, **Aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) is set to **Free Aspect**. 
**Property** | **Description**  
---|---  
**Low Resolution Aspect Ratios** | Emulate the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) density of lower-resolution displays and reduce the resolution of the Game view when an aspect ratio is selected. **Low Resolution Aspect Ratios** is always enabled when the Game view is on a non-Retina display.  
**VSync (Game view only)** | Allow syncing. Syncing can be useful when you record a video, for example. The Editor attempts to render the Game view at the refresh rate of the monitor, though this is not guaranteed. When this option is enabled, it can still be useful to maximize the Game view in Play mode to hide other views and reduce the number of views that the Editor renders.  
### Play mode behavior options
This section describes the Play mode behavior based on your selection below. 
You cannot change these properties while you’re in Play mode. You must pause or stop Play mode to change these settings. 
**Property** | **Description**  
---|---  
**Play Focused** | Shift the focus on the selected Game view when the Editor is in Play mode.   
Only one Game view can be in focus when you enter the Play mode. Using Maximized mode implies focus on the Maximized Game view. Enable Focused on a Game view to disable it on other Game views.  
**Play Maximized** | Run Play mode with the Game view maximized to 100% of the Editor window. Even if you enable **Play Maximized** , when you pause Play mode, the Game view returns to the window state it was in before you entered Play mode. This means that the Game view stays maximized when you pause Play mode only if it was maximized before you entered Play mode.  
**Play Unfocused** | Do not shift the focus to the selected Game view when you enter Play mode.  
## Gizmos menu
The Gizmos menu contains options for how Unity displays gizmos for GameObjects and other items in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) and Game view. This menu is available in both the Scene view and the Game view. For more information, refer to [Gizmos Menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html).
## Advanced options
Right-click the **Game** tab to display advanced Game view options.
![The Game tab context menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GameView-AdvancedOptions.png) The Game tab context menu
Advanced Game view options contain: 
  * **Warn if No Cameras Rendering** : Causes the Editor to display a warning if no Cameras are rendering to the screen. For example, use this for diagnosing problems such as accidentally deleting or disabling a Camera. Enable this unless you are intentionally not using Cameras to render your application. This option is enabled by default.
  * **Clear Every Frame in Edit Mode** : Causes the Editor to clear the Game view from every frame when your application is not playing. This prevents smearing effects while you are configuring your application. Leave this enabled unless you are depending on the previous frame’s contents when not in the Play mode. This option is enabled by default.


## Additional resources
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)
  * [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html)
  * [Gizmos Menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html)
  * [Toolbar](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)
  * [Scene view Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html)
  * [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingCustomEditorTools.html)
Custom Editor tools
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator.html)
Device Simulator
