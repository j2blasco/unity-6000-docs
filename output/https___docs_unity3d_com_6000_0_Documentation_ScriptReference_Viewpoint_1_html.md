* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.html

# Viewpoint<T0>
class in UnityEditor
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Defines a Viewpoint that can be selected from the Cameras overlay.
Use this base class with [ICameraLensData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ICameraLensData.html) to define a Viewpoint and expose a component in the Cameras overlay. If you expose a component in the Cameras overlay, you can use the Cameras overlay to look through that component in the Scene view.   
  
To use this class, you must have a custom representation of your camera lens in a [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).  
  
When detected, the Cameras overlay creates an instance of the Viewpoint class for each component that is type T0 in the scene.  
  
The Cameras overlay uses the icon that is attached to the component in the UI.
```
using UnityEngine;  
  
public class MyVirtualCamera : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float fov;
    public float nearPlane;
    public float farPlane;  
  
    public bool physicalProps;
    public float focalLength;
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) sensor;
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) lensShift;
    public Camera.GateFitMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GateFitMode.html) gateFit;
}
```

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class VirtualCameraViewpoint : Viewpoint<MyVirtualCamera>, ICameraLensData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ICameraLensData.html)
{
    public VirtualCameraViewpoint(MyVirtualCamera target) : base(target) { }  
  
    public float NearClipPlane => Target.nearPlane;  
  
    public float FarClipPlane => Target.farPlane;  
  
    // If you are not using physical properties, FieldOfView can change from the SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) with the scrollwheel action while looking through a camera.
    public float FieldOfView { get => Target.fov; set => Target.fov = value; }  
  
    public bool UsePhysicalProperties => Target.physicalProps;  
  
    // If you are using physical properties, FocalLength can change from the SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) with the scrollwheel action while looking through a camera.
    public float FocalLength { get => Target.focalLength; set => Target.focalLength = value; }  
  
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) SensorSize => Target.sensor;  
  
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) LensShift => Target.lensShift;  
  
    public Camera.GateFitMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GateFitMode.html) GateFit => Target.gateFit;  
  
    // The SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sets orthographic to true when: 
    // - the 2DMode button is toggled on.
    // - orthographic view is set from the Orientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Orientation.html) gizmo.
    //
    // In this example, our representation doesn't consider orthographic view.
    public bool Orthographic { get => false; set { } }
    public float OrthographicSize { get => 0; set { } }
}
```

### Properties
Property | Description  
---|---  
[Position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.Position.html) | The world position.  
[Rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.Rotation.html) | The world rotation.  
[Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.Target.html) | Returns the component the Viewpoint is attached to cast as T.  
[TargetObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.TargetObject.html) | A reference to the Component of type T this Viewpoint is attached to.  
### Constructors
Constructor | Description  
---|---  
[Viewpoint_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[CreateVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.CreateVisualElement.html) | CreateVisualElement is called when a Viewpoint is selected in the Cameras Overlay.  
* * *
