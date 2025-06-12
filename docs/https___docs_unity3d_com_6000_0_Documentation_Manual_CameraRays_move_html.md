* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-move.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [The camera view](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraView.html)
  * [Rays from the camera](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays.html)
  * Move a camera along a ray


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-cast.html)
Cast a ray from a camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
Using multiple cameras
# Move a camera along a ray
It is sometimes useful to get a ray corresponding to a screen position and then move the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) along that ray. For example, you may want to allow the user to select an object with the mouse and then zoom in on it while keeping it “pinned” to the same screen position under the mouse (this might be useful when the camera is looking at a tactical map, for example). The code to do this is fairly straightforward:
```
using UnityEngine;
using System.Collections;

public class ExampleScript : MonoBehaviour {
    public bool zooming;
    public float zoomSpeed;
    public Camera camera;

    void Update() {
        if (zooming) {
            Ray ray = camera.ScreenPointToRay(Input.mousePosition);
            float zoomDistance = zoomSpeed * Input.GetAxis("Vertical") * Time.deltaTime;
            camera.transform.Translate(ray.direction * zoomDistance, Space.World);
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-cast.html)
Cast a ray from a camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
Using multiple cameras
