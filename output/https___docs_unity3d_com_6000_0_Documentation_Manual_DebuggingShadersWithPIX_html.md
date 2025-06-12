* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DebuggingShadersWithPIX.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Debugging shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-debugging.html)
  * Debug shaders with PIX


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-DebuggingD3D11ShadersWithVS.html)
Debug shaders with Visual Studio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
Shader languages reference
# Debug shaders with PIX
PIX is a performance tuning and debugging tool by Microsoft, for Windows developers. It offers a range of modes for analyzing an application’s performance, and includes the ability to capture frames of DirectX projects from an application for debugging.
Use PIX to investigate issues in Windows 64-bit (x86_64) Standalone or Universal Windows Platform applications.
To install PIX, [download and run the Microsoft PIX installer](https://blogs.msdn.microsoft.com/pix/download/) and follow the instructions.
For more information about PIX, see Microsoft’s [PIX Introduction](https://blogs.msdn.microsoft.com/pix/introduction/) and [PIX Documentation](https://blogs.msdn.microsoft.com/pix/documentation/).
## Debugging DirectX shaders with PIX
You should use a built version of your Unity application to capture frames, rather than a version running in the Unity Editor. This is because you need to launch the target application from within PIX to capture GPU frames.
Using a **development build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild) adds additional information to PIX, which makes navigating the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) capture easier.
### Create a project with a debug-enabled Shader
To debug the shader with source code in PIX, you need to insert the following pragma into the shader code: `#pragma enable_d3d11_debug_symbols`
### Example
The following walkthrough uses a basic example to demonstrate the entire process.
#### Create a basic project:
  1. Create a new Unity project (see the Hub documentation on [Projects](https://docs.unity3d.com/hub/manual/Projects.html)).
  2. In the top menu, go to **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) > **Create** > **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) > **Standard Surface Shader**. This creates a new shader file in your **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Project) folder.
  3. Select the shader file, and in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, click **Open**. This opens the shader file in your scripting editor. Insert `#pragma enable_d3d11_debug_symbols` into the shader code, underneath the other `#pragma` lines.
  4. Create a new Material (menu: **Assets** > **Create** > **Material** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material)).
  5. In the Material’s Inspector window, select the **Shader** dropdown, go to **Custom** , and select the shader you just created. 
  6. Create a 3D cube GameObject (menu: **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) > **3D Object** A 3D GameObject such as a cube, terrain or ragdoll. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#3DObject) > **Cube**).
  7. Assign your new Material to your new GameObject. To do this, drag the Material from the **Project** window to the 3D cube.


### Capture a frame from a Windows Standalone application:
  1. Go to **File** > **Build Profiles** , and under **Platforms** , select **Windows** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Windows** platform. Set the **Architecture** to **Intel 64-bit** , and enable the **Development Build**.
  2. Click **Build** The process of compiling your project into a format that is ready to run on a specific platform or platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#build).
  3. Launch **PIX.**
  4. Click on **Home** , then **Connect**
  5. Select Computer **localhost** to use your PC for capturing, and click **connect**.
  6. In the **Select Target Process** box, select the **Launch Win32** tab and use the **Browse** button to select your application’s executable file. Note that here, “Win32” means a non-UWP application; your application file must be a 64-bit binary file.
  7. Enable **Launch for GPU Capture** , then use the **Launch** button to start the application.
  8. Use your application as normal until you are ready to capture a frame. To capture a frame, press **Print Screen** on your keyboard, or click the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) icon on the GPU Capture Panel. A thumbnail of the capture appears in the panel. To open the capture, click the thumbnail.
  9. To start analysis on the capture, click the highlighted text or the small **Play** icon on the menu bar.
  10. Select the **Pipeline** tab and use the__ Events__ window to navigate to a draw call you are interested in.
  11. In the lower half of the **Pipeline** tab, select a render target from the **OM** (Output Merger) list to view the output of draw call. Select a **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) on the object you want to debug. Note that you can right-click a pixel to view the draw call history, as a way of finding draw calls you are interested in.
  12. Select **Debug Pixel** on the **Pixel Details** panel.
  13. On the debug panel, use the Shader Options to select which shader stage to debug.
  14. Use the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) or keyboard shortcuts to step through the code.


For more information on debugging shaders with PIX, see Microsoft’s video series [PIX on Windows](https://www.youtube.com/playlist?list=PLeHvwXyqearWuPPxh6T03iwX-McPG5LkB), particularly [Part 5 - Debug Tab](https://www.youtube.com/watch?v=jRflMYmXv2g).
For more information on GPU capture in PIX, see Microsoft’s documentation on [GPU Captures](https://blogs.msdn.microsoft.com/pix/gpu-captures/). 
  * 2018–09–17 Page published 


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-DebuggingD3D11ShadersWithVS.html)
Debug shaders with Visual Studio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
Shader languages reference
