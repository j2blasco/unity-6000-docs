* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-cast.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [The camera view](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraView.html)
  * [Rays from the camera](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays.html)
  * Cast a ray from a camera


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-introduction.html)
Introduction to raycasting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-move.html)
Move a camera along a ray
# Cast a ray from a camera
The most common use of a Ray from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is to perform a [raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html) out into the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). A raycast sends an imaginary “laser beam” along the ray from its origin until it hits a **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) in the scene. Information is then returned about the object and the point that was hit in a [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) object. This is a very useful way to locate an object based on its onscreen image. For example, the object at the mouse position can be determined with the following code:
```
using UnityEngine;
using System.Collections;

public class ExampleScript : MonoBehaviour {
    public Camera camera;

    void Start(){
        RaycastHit hit;
        Ray ray = camera.ScreenPointToRay(Input.mousePosition);
        
        if (Physics.Raycast(ray, out hit)) {
            Transform objectHit = hit.transform;
            
            // Do something with the object that was hit by the raycast.
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-introduction.html)
Introduction to raycasting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraRays-move.html)
Move a camera along a ray
