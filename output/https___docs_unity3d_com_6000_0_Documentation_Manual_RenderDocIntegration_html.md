* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RenderDocIntegration.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * RenderDoc Integration


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VisualStudioIntegration.html)
Visual Studio C# integration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorAnalytics.html)
Editor analytics
# RenderDoc Integration
The Editor supports integrated launching and capture of the [RenderDoc](https://github.com/baldurk/renderdoc) graphics debugger, for detailed frame introspection and debugging.
The integration is only supported for RenderDoc versions 0.26 or later, so if an earlier version is currently installed it is required that you update to at least version 0.26.
**Note:** While the integration is only available in the Editor, it is quite possible to use RenderDoc as normal with no extra setup in standalone player builds.
**Note:** Frames can only be captured if Unity is running on a platform and API that RenderDoc supports. If another API is in use, the RenderDoc integration will be temporarily disabled until a supported API is enabled. Refer to the [RenderDoc documentation](https://renderdoc.org/docs/getting_started/features.html) for more information on supported platforms and APIs.
## Loading RenderDoc
If a RenderDoc installation is detected, then at any time after loading the Editor you can right click on the tab for the [Game View](https://docs.unity3d.com/6000.0/Documentation/Manual/GameView.html) or [Scene View](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) and click the ‘Load RenderDoc’ option. This will reload the graphics device so you must save any changes, but afterwards RenderDoc will be ready to capture without having to restart the editor or build a standalone player.
**Note:** You can also launch the Editor via RenderDoc as normal, or pass the -load-renderdoc command line option to load RenderDoc from startup.
## Capturing a frame with RenderDoc
When a compatible version of RenderDoc is detected as loaded into the Editor, a new button will appear on the right side of the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) on the Game and **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) Views.
![Capturing a frame with RenderDoc](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RenderDocCaptureButton.png) Capturing a frame with RenderDoc
Pressing this button will trigger a capture of the next frame of rendering for the view. If the RenderDoc tool UI has not been opened, a new instance will be launched to show the capture, and if it is already running the newest capture will automatically appear there. From there you can open the capture and debug using the tool.
![List of frame captures in RenderDoc](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RenderDocCaptureList.jpg) List of frame captures in RenderDoc
## Including shader debug information
By default to optimise the size of DirectX11 shaders, debugging information is stripped out. This means that constants and resources will have no names, and the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) source will not be available. To include this debugging information in your shader, include **#pragma enable_d3d11_debug_symbols** in your shader’s `HLSLPROGRAM` block.
## Alternative graphics debugging techniques
If you build a standalone player using D3D11, you can capture a frame and debug using the [Visual Studio graphics debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-DebuggingD3D11ShadersWithVS.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VisualStudioIntegration.html)
Visual Studio C# integration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorAnalytics.html)
Editor analytics
