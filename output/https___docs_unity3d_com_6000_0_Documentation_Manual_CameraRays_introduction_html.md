* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-introduction.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [The camera view](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraView.html)
  * [Rays from the camera](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays.html)
  * Introduction to raycasting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays.html)
Rays from the camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-cast.html)
Cast a ray from a camera
# Introduction to raycasting
In the section [Understanding the View Frustum](https://docs.unity3d.com/6000.0/Documentation/Manual/UnderstandingFrustum.html), it was explained that any point in the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s view corresponds to a line in world space. It is sometimes useful to have a mathematical representation of that line and Unity can provide this in the form of a [Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) object. The Ray always corresponds to a point in the view, so the Camera class provides the [ScreenPointToRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenPointToRay.html) and [ViewportPointToRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportPointToRay.html) functions. The difference between the two is that ScreenPointToRay expects the point to be provided as a **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) coordinate, while ViewportPointToRay takes normalized coordinates in the range 0..1 (where 0 represents the bottom or left and 1 represents the top or right of the view). Each of these functions returns a Ray which consists of a point of origin and a vector which shows the direction of the line from that origin. The Ray originates from the near **clipping plane** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane) rather than the Camera’s transform.position point.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays.html)
Rays from the camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-cast.html)
Cast a ray from a camera
