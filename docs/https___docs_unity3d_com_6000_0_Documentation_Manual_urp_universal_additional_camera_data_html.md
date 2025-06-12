* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universal-additional-camera-data.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * Access camera data with the Universal Additional Camera Data component in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-debug-views.html)
Spatial-Temporal Post-processing Rendering Debugger reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
Camera Inspector windows reference for URP
# Access camera data with the Universal Additional Camera Data component in URP
The Universal Additional **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) Data component is a component the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) uses for internal data storage. The Universal Additional Camera Data component allows URP to extend and override the functionality and appearance of Unity’s standard Camera component.
In URP, a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that has a Camera component must also have a Universal Additional Camera Data component. If your Project uses URP, Unity automatically adds the Universal Additional Camera Data component when you create a Camera GameObject. You cannot remove the Universal Additional Camera Data component from a Camera GameObject.
If you don’t use **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to control and customise URP, you do not need to do anything with the Universal Additiona Camera Data component.
If you do use scripts to control and customise URP, you can access a Camera’s Universal Additional Camera Data component in a script like this:
```
UniversalAdditionalCameraData cameraData = camera.GetUniversalAdditionalCameraData();

```

**Note:** To use the `GetUniversalAdditionalCameraData()` method you must use the `UnityEngine.Rendering.Universal` namespace. To do this, add the following statement at the top of your script: `using UnityEngine.Rendering.Universal;`.
For more information, refer to the [UniversalAdditionalCameraData API](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html).
If you need to access the Universal Additional Camera Data component frequently in a script, you should cache the reference to it to avoid unnecessary CPU work.
**Note:** When a Camera uses a Preset, only a subset of properties are supported. Unsupported properties are hidden.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-debug-views.html)
Spatial-Temporal Post-processing Rendering Debugger reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
Camera Inspector windows reference for URP
