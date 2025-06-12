* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Custom rendering in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-landing.html)
  * CommandBuffer fundamentals in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-landing.html)
Custom rendering in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-order.html)
CameraEvent and LightEvent events order reference for the Built-In Render Pipeline
# CommandBuffer fundamentals in the Built-In Render Pipeline
A [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) holds a list of rendering commands (such as setting the render target, or drawing a given mesh). You can instruct Unity to schedule and execute those commands at various points in the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), which allows you to customize and extend Unity’s rendering functionality.
![Blurry refraction, using Command Buffers.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RenderingCommandBufferBlurryRefraction.jpg) Blurry refraction, using Command Buffers.
You can execute CommandBuffers immediately using the [Graphics.ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBuffer.html) API, or you can schedule them so that they occur at a given point in the render pipeline. To schedule them, use the [Camera.AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.AddCommandBuffer.html) API with the [CameraEvent enum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html), and the [Light.AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html) API with the [LightEvent enum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html). To see when Unity executes CommandBuffers that you schedule in this way, see [CameraEvent and LightEvent order of execution](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html).
For a full list of the commands that you can execute using CommandBuffers, see the [CommandBuffer API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html). Note that some commands are supported only on certain hardware; for example, the commands relating to **ray tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Raytracing) are supported only in DX12.
  * [Introduction to render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-overview.html)
  * [Execute rendering commands in a Scriptable Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/index.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-landing.html)
Custom rendering in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-order.html)
CameraEvent and LightEvent events order reference for the Built-In Render Pipeline
