* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Using multiple cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
  * Configure multiple cameras


[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
Using multiple cameras
[](https://docs.unity3d.com/6000.0/Documentation/Manual/multiple-cameras-birp.html)
Set the order of multiple cameras
# Configure multiple cameras
When created, a Unity **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) contains just a single **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and this is all you need for most situations. However, you can have as many cameras in a scene as you like and their views can be combined in different ways, as described below.
## Swap camera views
By default, a camera renders its view to cover the whole screen and so only one camera view can be seen at a time (the visible camera is the one that has the highest value for its _depth_ property). By disabling one camera and enabling another from a script, you can “cut” from one camera to another to give different views of a scene. You might do this, for example, to switch between an overhead map view and a first-person view.
```
using UnityEngine;

public class ExampleScript : MonoBehaviour {
    public Camera firstPersonCamera;
    public Camera overheadCamera;

    // Call this function to disable FPS camera,
    // and enable overhead camera.
    public void ShowOverheadView() {
        firstPersonCamera.enabled = false;
        overheadCamera.enabled = true;
    }
    
    // Call this function to enable FPS camera,
    // and disable overhead camera.
    public void ShowFirstPersonView() {
        firstPersonCamera.enabled = true;
        overheadCamera.enabled = false;
    }
}

```

## Render a small camera view inside a larger one
Usually, you want at least one camera view covering the whole screen (the default setting) but it is often useful to show another view inside a small area of the screen. For example, you might show a rear view mirror in a driving game or show an overhead mini-map in the corner of the screen while the main view is first-person. You can set the size of a camera’s onscreen rectangle using its _Viewport Rect_ property.
The coordinates of the **viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport) rectangle are “normalized” with respect to the screen. The bottom and left edges are at the 0.0 coordinate, while the top and right edges are at 1.0. A coordinate value of 0.5 is halfway across. In addition to the viewport size, you should also set the _depth_ property of the camera with the smaller view to a higher value than the background camera. The exact value does not matter but the rule is that a camera with a higher depth value is rendered over one with a lower value.
![Two-player display created with the Viewport Rect property](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Camera-Viewport.jpg) Two-player display created with the Viewport Rect property
## Additional resources
  * [Multiple cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
Using multiple cameras
[](https://docs.unity3d.com/6000.0/Documentation/Manual/multiple-cameras-birp.html)
Set the order of multiple cameras
