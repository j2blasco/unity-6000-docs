* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-landing.html)
  * Introduction to the Frame Debugger


[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-landing.html)
Frame Debugger
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-debug.html)
Debug a frame
# Introduction to the Frame Debugger
Debug frames to help identify rendering artefacts and other issues. Unity includes a dedicated [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html) that can pause the application on a particular frame and display the list of rendering events that constitute the frame. The Frame Debugger can step through each event and display the graphical state of the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) at that point in the rendering process. You can use this to find where graphical issues arise or to just see how Unity constructs the scene from graphical elements.
## Render Pipeline compatibility
**Feature** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Frame Debugger** | Yes | Yes | Yes | Yes  
## 3rd-party frame debugging software
If you need information about a frame that Unity’s Frame Debugger doesn’t provide, there are 3rd-party frame debugging programs that support Unity. The Unity Editor supports native launching and frame capturing for [RenderDoc](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderDocIntegration.html). You can also build a standalone Player and attach a supported frame debugger. For information about supported frame debugging software, see [Profiling tools](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-profiling-tools.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-landing.html)
Frame Debugger
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-debug.html)
Debug a frame
