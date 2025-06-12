* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/User-Render-Requests.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
  * Create a render request in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-a-render-texture.html)
Render a camera's output to a Render Texture in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-advanced.html)
Camera render order in URP
# Create a render request in URP
To trigger a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) to render to a **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) outside of the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) rendering loop, use the `SubmitRenderRequest` API in a C# script.
This example shows how to use render requests and callbacks to monitor the progress of these requests. You can see the full code sample in the [Example code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/User-Render-Requests.html#example-code) section.
## Render a single camera from a camera stack
To render a single camera without taking into account the full stack of cameras, use the `UniversalRenderPipeline.SingleCameraRequest` API. Follow these steps:
  1. Create a C# script with the name `SingleCameraRenderRequestExample` and add the `using` statements shown below.
```
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

public class SingleCameraRenderRequestExample : MonoBehaviour
{

}

```

  2. Create arrays to store the cameras and Render Textures that you want to render from and to.
```
public class SingleCameraRenderRequestExample : MonoBehaviour
{
    public Camera[] cameras;
    public RenderTexture[] renderTextures;
}

```

  3. In the `Start` method, add a check to ensure the `cameras` and `renderTextures` arrays are valid and contain the correct data before continuing with running the script.
```
void Start()
{
    // Make sure all data is valid before you start the component
    if (cameras == null || cameras.Length == 0 || renderTextures == null || cameras.Length != renderTextures.Length)
    {
        Debug.LogError("Invalid setup");
        return;
    }
}

```

  4. Make a method with the name `SendSingleRenderRequests` and the return type `void` within the `SingleCameraRenderRequest` class.
  5. In the `SendSingleRenderRequests` method, add a `for` loop that iterates over the `cameras` array as shown below.
```
void SendSingleRenderRequests()
{
    for (int i = 0; i < cameras.Length; i++)
    {

    }
}

```

  6. Inside the `for` loop, create a render request of the `UniversalRenderPipeline.SingleCameraRequest` type in a variable with the name `request`. Then check if the active render pipeline supports this render request type with `RenderPipeline.SupportsRenderRequest`.
  7. If the active render pipeline supports the render request, set the destination of the camera output to the matching Render Texture from the `renderTextures` array. Then submit the render request with `RenderPipeline.SubmitRenderRequest`.
```
void SendSingleRenderRequests()
{
    for (int i = 0; i < cameras.Length; i++)
    {
        UniversalRenderPipeline.SingleCameraRequest request =
            new UniversalRenderPipeline.SingleCameraRequest();

        // Check if the active render pipeline supports the render request
        if (RenderPipeline.SupportsRenderRequest(cameras[i], request))
        {
            // Set the destination of the camera output to the matching RenderTexture
            request.destination = renderTextures[i];
                
            // Render the camera output to the RenderTexture synchronously
            // When this is complete, the RenderTexture in renderTextures[i] contains the scene rendered from the point
            // of view of the Camera in cameras[i]
            RenderPipeline.SubmitRenderRequest(cameras[i], request);
        }
    }
}

```

  8. Above the `SendSingleRenderRequest` method, create an `IEnumerator` interface with the name `RenderSingleRequestNextFrame`.
  9. Inside `RenderSingleRequestNextFrame`, wait for the main camera to finish rendering, then call `SendSingleRenderRequest`. Wait for the end of the frame before restarting `RenderSingleRequestNextFrame` in a coroutine with `StartCoroutine`.
```
IEnumerator RenderSingleRequestNextFrame()
{
    // Wait for the main camera to finish rendering
    yield return new WaitForEndOfFrame();

    // Enqueue one render request for each camera
    SendSingleRenderRequests();

    // Wait for the end of the frame
    yield return new WaitForEndOfFrame();

    // Restart the coroutine
    StartCoroutine(RenderSingleRequestNextFrame());
}

```

  10. In the `Start` method, call `RenderSingleRequestNextFrame` in a coroutine with `StartCoroutine`.
```
void Start()
{
    // Make sure all data is valid before you start the component
    if (cameras == null || cameras.Length == 0 || renderTextures == null || cameras.Length != renderTextures.Length)
    {
        Debug.LogError("Invalid setup");
        return;
    }

    // Start the asynchronous coroutine
    StartCoroutine(RenderSingleRequestNextFrame());
}

```

  11. In the Editor, create an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and add `SingleCameraRenderRequestExample.cs` as a [component](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component).
  12. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, add the camera you want to render from to the **cameras** list, and the Render Texture you want to render into to the **renderTextures** list.


**Note:** The number of cameras in the **cameras** list and the number of Render Textures in the **renderTextures** list must be the same.
Now when you enter Play mode, the cameras you added render to the Render Textures you added.
### Check when a camera finishes rendering
To check when a camera finishes rendering, use any callback from the [RenderPipelineManager](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager.html) API.
The following example uses the [RenderPipelineManager.endContextRendering](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html) callback.
  1. Add `using System.Collections.Generic` to the top of the `SingleCameraRenderRequestExample.cs` file.
  2. At the end of the `Start` method, subscribe to the [`endContextRendering`](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager-endContextRendering.html) callback.
```
void Start()
{
    // Make sure all data is valid before you start the component
    if (cameras == null || cameras.Length == 0 || renderTextures == null || cameras.Length != renderTextures.Length)
    {
        Debug.LogError("Invalid setup");
        return;
    }

    // Start the asynchronous coroutine
    StartCoroutine(RenderSingleRequestNextFrame());
        
    // Call a method called OnEndContextRendering when a camera finishes rendering
    RenderPipelineManager.endContextRendering += OnEndContextRendering;
}

```

  3. Create a method with the name `OnEndContextRendering`. Unity runs this method when the `endContextRendering` callback triggers.
```
void OnEndContextRendering(ScriptableRenderContext context, List<Camera> cameras)
{
    // Create a log to show cameras have finished rendering
    Debug.Log("All cameras have finished rendering.");
}

```

  4. To unsubscribe the `OnEndContextRendering` method from the `endContextRendering` callback, add an `OnDestroy` method to the `SingleCameraRenderRequestExample` class.
```
void OnDestroy()
{
    // End the subscription to the callback
    RenderPipelineManager.endContextRendering -= OnEndContextRendering;
}

```



This script now works as before, but logs a message to the **Console Window** A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Consolewindow) about which cameras have finished rendering.
## Example code
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

public class SingleCameraRenderRequest : MonoBehaviour
{
    public Camera[] cameras;
    public RenderTexture[] renderTextures;

    void Start()
    {
        // Make sure all data is valid before you start the component
        if (cameras == null || cameras.Length == 0 || renderTextures == null || cameras.Length != renderTextures.Length)
        {
            Debug.LogError("Invalid setup");
            return;
        }

        // Start the asynchronous coroutine
        StartCoroutine(RenderSingleRequestNextFrame());
        
        // Call a method called OnEndContextRendering when a camera finishes rendering
        RenderPipelineManager.endContextRendering += OnEndContextRendering;
    }

    void OnEndContextRendering(ScriptableRenderContext context, List<Camera> cameras)
    {
        // Create a log to show cameras have finished rendering
        Debug.Log("All cameras have finished rendering.");
    }

    void OnDestroy()
    {
        // End the subscription to the callback
        RenderPipelineManager.endContextRendering -= OnEndContextRendering;
    }

    IEnumerator RenderSingleRequestNextFrame()
    {
        // Wait for the main camera to finish rendering
        yield return new WaitForEndOfFrame();

        // Enqueue one render request for each camera
        SendSingleRenderRequests();

        // Wait for the end of the frame
        yield return new WaitForEndOfFrame();

        // Restart the coroutine
        StartCoroutine(RenderSingleRequestNextFrame());
    }

    void SendSingleRenderRequests()
    {
        for (int i = 0; i < cameras.Length; i++)
        {
            UniversalRenderPipeline.SingleCameraRequest request =
                new UniversalRenderPipeline.SingleCameraRequest();

            // Check if the active render pipeline supports the render request
            if (RenderPipeline.SupportsRenderRequest(cameras[i], request))
            {
                // Set the destination of the camera output to the matching RenderTexture
                request.destination = renderTextures[i];
                
                // Render the camera output to the RenderTexture synchronously
                RenderPipeline.SubmitRenderRequest(cameras[i], request);

                // At this point, the RenderTexture in renderTextures[i] contains the scene rendered from the point
                // of view of the Camera in cameras[i]
            }
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-a-render-texture.html)
Render a camera's output to a Render Texture in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-advanced.html)
Camera render order in URP
