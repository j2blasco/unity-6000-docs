* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Camera Inspector windows reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
  * Camera Inspector window reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
Camera Inspector windows reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html)
Physical Camera Inspector window reference for URP
# Camera Inspector window reference for URP
In the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), Unity exposes different properties of the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) component in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) depending on the camera type. To change the type of the camera, select a [Render Type](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type.html).
Base cameras expose the following properties:
  * [Projection](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Projection)
  * [Physical Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#PhysicalCamera)
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Rendering)
  * [Stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Stack)
  * [Environment](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Environment)
  * [Output](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Output)


Overlay cameras expose the following properties:
  * [Projection](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Projection)
  * [Physical Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#PhysicalCamera)
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Rendering)
  * [Environment](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Environment)


## Projection
**Property** | **Description**  
---|---  
**Projection** | Control how the camera simulates perspective.  
**Perspective** | Render objects with perspective intact.  
**Orthographic** | Render objects uniformly, with no sense of perspective.  
**Field of View Axis** | Set the axis Unity measures the camera’s field of view along.  
  
Available options:
  * **Vertical**
  * **Horizontal**

This property is only visible when **Projection** is set to **Perspective**.  
**Field of View** | Set the width of the camera’s view angle, measured in degrees along the selected axis.  
  
This property is only visible when **Projection** is set to **Perspective**.  
**Size** | Set the viewport size of the camera.  
  
This property is only visible when **Projection** is set to **Orthographic**.  
****Clipping Planes** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane)** | Set the distances from the camera where rendering starts and stops.  
**Near** | The closest point relative to the camera where drawing occurs.  
**Far** | The furthest point relative to the camera where drawing occurs.  
**Physical Camera** | Displays additional properties for the camera in the Inspector to simulate a physical camera. A physical camera calculates the Field of View with properties simulating real-world camera attributes: **Focal Length** , **Sensor Size** , and **Shift**.  
  
The **Physical Camera** property is only available when **Projection** is set to **Perspective**.  
### Physical Camera
The **Physical Camera** property adds additional properties to the camera to simulate a real-world camera. For more information, refer to the [Physical Camera reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html).
## Rendering
**Property** | **Description**  
---|---  
**Renderer** | Select which renderer this camera uses.  
**Post Processing** | Enable **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects.  
**Anti-Aliasing** | Select the method that this camera uses for post-process anti-aliasing. A camera can still use Multisample Anti-aliasing (MSAA), which is a hardware feature, at the same time as post-process anti-aliasing unless you use Temporal Anti-aliasing.  
  
The following Anti-aliasing options are available:
  * **None** : This camera can process MSAA but does not process any post-process anti-aliasing.
  * **Fast Approximate Anti-aliasing (FXAA)** : Performs a full screen pass which smooths edges on a per-pixel level.
  * **Subpixel Morphological Anti-aliasing (SMAA)** : Finds edge patterns in the image and blends the pixels on these edges according to those patterns.
  * **Temporal Anti-aliasing (TAA)** : Uses previous frames accumulated into a color history buffer to smooth edges over the course of multiple frames.

For more information, refer to [Anti-aliasing in the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html).  
  
This property is only visible when **Render Type** is set to **Base**.  
**Quality (SMAA)** | Select the quality of SMAA. The difference in resource intensity is fairly small between **Low** and **High**.  
  
Available options:
  * **Low**
  * **Medium**
  * **High**

This property only appears when you select **Subpixel Morphological Anti-aliasing (SMAA)** from the **Anti-aliasing** drop-down.  
**Quality (TAA)** | Select the quality of TAA.  
  
Available options:
  * **Very Low**
  * **Low**
  * **Medium**
  * **High**
  * **Very High**

This property only appears when you select **Temporal Anti-aliasing (TAA)** from the **Anti-aliasing** drop-down.  
**Contrast Adaptive Sharpening** | Enable high quality post sharpening to reduce TAA blur.  
  
This setting is overridden when you enable either [AMD FidelityFX Super Resolution (FSR) or Scalable Temporal Post-Processing (STP –>(universalrp-asset#quality) upscaling in the URP Asset as they both handle sharpening as part of the upscaling process.   
  
This property only appears when you select **Temporal Anti-aliasing (TAA)** from the **Anti-aliasing** drop-down.  
**Base Blend Factor** | Set how much the history buffer blends with the current frame result. Higher values mean more history contribution, which improves the anti-aliasing, but also increases the chance of ghosting.  
  
This property only appears when you select **Temporal Anti-aliasing (TAA)** from the **Anti-aliasing** drop-down and enable **Advanced Properties** in the Inspector.  
**Jitter Scale** | Set the scale of the jitter applied when TAA is enabled. A lower value reduces visible flickering and jittering, but also reduces the effectiveness of the anti-aliasing.  
  
This property only appears when you select **Temporal Anti-aliasing (TAA)** from the **Anti-aliasing** drop-down and enable **Advanced Properties** in the Inspector.  
**Mip Bias** | Set how much texture mipmap selection is biased when rendering.  
  
A positive bias makes a texture appear more blurry, while a negative bias sharpens the texture. However, a lower value also has a negative impact on performance.  
  
**Note** : Requires mipmaps in textures.  
  
This property only appears when you select **Temporal Anti-aliasing (TAA)** from the **Anti-aliasing** drop-down and enable **Advanced Properties** in the Inspector.  
**Variance Clamp Scale** | Set the size of the color volume Unity uses to find nearby pixels when the color history is incorrect or unavailable. The clamp limits how much a pixel’s color can vary from the color of the surrounding pixels.  
  
Lower values can reduce ghosting, but produce more flickering. Higher values reduce flickering, but are prone to blur and ghosting.  
  
This property only appears when you select **Temporal Anti-aliasing (TAA)** from the **Anti-aliasing** drop-down and enable **Advanced Properties** in the Inspector.  
**Stop NaNs** | Replaces Not a Number (NaN) values with a black pixel for the camera. This stops certain effects from breaking, but is a resource-intensive process which causes a negative performance impact. Only enable this feature if you experience NaN issues you can’t fix.  
  
The Stop NaNs pass executes at the start of the post-processing passes. You must enable **Post Processing** for the camera to use **Stop NaNs**.  
  
Only available when **Render Type** is set to **Base**.  
**Dithering** | Enable to apply 8-bit dithering to the final render to help reduce banding on wide gradients and low light areas.  
  
This property is only visible when **Render Type** is set to **Base**.  
**Clear Depth** | Enable to clear depth from previous camera on rendering.  
  
This property is only visible when **Render Type** is set to **Overlay**.  
**Render Shadows** | Enable shadow rendering.  
**Priority** | A camera with a higher priority is drawn on top of a camera with a lower priority. Priority has a range from –100 to 100.  
  
This property is only visible when **Render Type** is set to **Base**.  
**Opaque Texture** | Control whether the camera creates a CameraOpaqueTexture, which is a copy of the rendered view.  
  
Available options:
  * **Off** : Camera does not create a CameraOpaqueTexture.
  * **On** : Camera creates a CameraOpaqueTexture.
  * **Use Pipeline Settings** : The Render Pipeline Asset determines the value of this setting.

This property is only visible when **Render Type** is set to **Base**.  
**Depth Texture** | Control whether the camera creates `_CameraDepthTexture`, which is a copy of the rendered depth values.  
  
Available options:
  * **Off** : Camera does not create a CameraDepthTexture.
  * **On** : Camera creates a CameraDepthTexture.
  * **Use Pipeline Settings** : The Render Pipeline Asset determines the value of this setting.

**Note** : `_CameraDepthTexture` is set between the `AfterRenderingSkybox` and `BeforeRenderingTransparents` events, or at the `BeforeRenderingOpaques` event if you use a depth prepass. For more information on the order of events in the rendering loop, refer to [Injection points](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html).  
****Culling Mask** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask)** | Select which Layers the camera renders to.  
****Occlusion Culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling)** | Enable Occlusion Culling.  
## Stack
**Note:** This section is only available if **Render Type** is set to **Base**
A camera stack allows to composite results of several cameras together. The camera stack consists of a Base camera and any number of additional Overlay cameras.
You can use the stack property add Overlay cameras to the stack and they will render in the order as defined in the stack. For more information on configuring and using camera stacks, refer to [Set up a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html).
## Environment
**Property** | **Description**  
---|---  
**Background Type** | Control how to initialize the color buffer at the start of this camera’s render loop. For more information, refer to [the documentation on clearing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-advanced.html#clearing-the-color-and-depth-buffers).  
  
This property is only visible when **Render Type** is set to **Base**.  
****Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox)** | Initializes the color buffer by clearing to a Skybox. Defaults to a background color if no Skybox is found.  
**Solid Color** | Initializes the color buffer by clearing to a given color.  
If you select this property, Unity shows the following extra property:  
**Background** : The camera clears its color buffer to this color before rendering.  
**Uninitialized** | Does not initialize the color buffer. This means that the load action for that specific RenderTarget will be `DontCare` instead of `Load` or `Clear`. `DontCare` specifies that the previous contents of the RenderTarget don’t need to be preserved.  
  
Only use this option in order to optimize performance in situations where your camera or Camera Stack will draw to every pixel in the color buffer, otherwise the behaviour of pixels the camera doesn’t draw is undefined.  
  
**Note** : The results might look different between Editor and Player, as the Editor doesn’t run on Tile-Based Deferred Rendering (TBDR) GPUs (found in mobile devices). If you use this option on TBDR GPUs, it causes uninitialized tile memory and the content is undefined.  
**Volumes** | The settings in this section define how Volumes affect this camera.  
**Update** **Mode** | Select how Unity updates Volumes.  
  
Available options:
  * **Every Frame** : Update Volumes with every frame Unity renders.
  * **Via Scripting** : Only update volumes when triggered by a script.
  * **Use Pipeline Settings** : Use the default setting for the Render Pipeline.

  
**Volume** **Mask** | Use the drop-down to set the **Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask) that defines which Volumes affect this camera.  
**Volume** **Trigger** | Assign a Transform that the [Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html) system uses to handle the position of this camera. For example, if your application uses a third person view of a character, set this property to the character’s Transform. The camera then uses the post-processing and **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) settings for Volumes that the character enters. If you do not assign a Transform, the camera uses its own Transform instead.  
## Output
This section is only available if you set the **Render Type** to **Base**
**Note:** When a camera’s **Render Type** is set to **Base** and its **Render Target** is set to **Texture** , Unity does not show the following properties in the Inspector for the camera:
  * **Target Display**
  * ****HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) rendering**
  * **MSAA**
  * **Allow**Dynamic Resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution)**


This is because the **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) determines these properties. You can change them in the Render Texture Asset.
**Property** | **Description**  
---|---  
**Output Texture** | Render this camera’s output to a RenderTexture if this field is assigned, otherwise render to the screen.  
**Target Display** | Select which external device to render to.  
**Target Eye** | Select the target eye for this camera.  
  
Available options:
  * **Both** : Allows XR rendering from the selected camera.
  * **None** : Disables XR rendering for the selected camera.

  
****Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport) Rect** | Four values that indicate where on the screen this camera view is drawn. Measured in Viewport Coordinates (values 0–1).  
**X** | The beginning horizontal position Unity uses to draw the camera view.  
**Y** | The beginning vertical position Unity uses to draw the camera view.  
**W** | Width of the camera output on the screen.  
**H** | Height of the camera output on the screen.  
**HDR Rendering** | Enable High Dynamic Range rendering for this camera.  
**MSAA** | Enable [Multisample Anti-aliasing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#msaa) for this camera.  
**Allow Dynamic Resolution** | Enable Dynamic Resolution rendering for this camera.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
Camera Inspector windows reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html)
Physical Camera Inspector window reference for URP
