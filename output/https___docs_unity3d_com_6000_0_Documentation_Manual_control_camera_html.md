* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/control-camera.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * Control a camera in first person


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html)
Scene view Camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html)
Scene visibility
# Control a camera in first person
Navigate through the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view while you look through a camera. In first-person, work through the lens of a camera to better frame your shots. 
You can use the [Cameras overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-overlay.html) to select and take first-person control of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that has a Camera or [Cinemachine camera](https://docs.unity3d.com/Packages/com.unity.cinemachine@latest/) component attached to it. 
While you control a camera, you can use Editor tools as you do when you use the Scene Camera. For example, select a GameObject and press the F key to frame the camera on a specific GameObject. You can also adjust the position, orientation, and scale of a GameObject while you look through a camera to change the composition of your shot. 
You can adjust the overscan of cameras you directly control with the Cameras overlay. Use overscan to intentionally see more or less of the Scene in the camera’s view than what the final output of the camera produces. 
The Cameras overlay supports Timeline and Animation camera path authoring and Animated cameras. Control a camera in first person to animate cameras and generate **keyframes** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) for their GameObjects. 
To control a camera in the first-person view:
  1. Press **`** to open the [Overlays menu](https://docs.unity3d.com/6000.0/Documentation/Manual/overlays.html).
  2. In the Overlays menu, enable the Cameras overlay.
  3. In the Cameras overlay dropdown list, select a camera you want to control in first person.
  4. Select **Control selected camera in first person**.
  5. To adjust overscan size and opacity, select **Configure overscan settings** and do the following: 
     * To select a size for the view guide, enter a value for **Overscan** or use the scroll wheel on your mouse. 1 is the default value. Enter a value greater than 1 to see more than the camera frustrum. Enter a value below 1 to zoom in and see less than the camera frustrum.
     * To adjust how opaque the view guide is, enter a value for **Overscan Opacity**.
  6. Use the [Scene view navigation controls](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html#tools) to move the camera through the scene.
  7. To exit the camera view, in the Cameras overlay, select **Return to Scene Camera**.


## Additional resources
  * [Overlays](https://docs.unity3d.com/6000.0/Documentation/Manual/overlays.html)
  * [Cameras overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-overlay.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)
  * [Cinemachine](https://docs.unity3d.com/Packages/com.unity.cinemachine@latest/)
  * [Timeline](https://docs.unity3d.com/Packages/com.unity.timeline@latest/)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html)
Scene view Camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html)
Scene visibility
