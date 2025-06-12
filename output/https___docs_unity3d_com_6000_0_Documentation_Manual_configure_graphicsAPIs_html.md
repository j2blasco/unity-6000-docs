* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-graphicsAPIs.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
  * Configure graphics APIs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
Graphics API support
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html)
DirectX
# Configure graphics APIs
Unity uses a built-in set of graphics APIs or the graphics APIs that you select in the Unity Editor.
To use Unity’s default graphics APIs:
  1. Open the [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) (menu: **Edit** > **Project Settings** > **Player**).
  2. Navigate to **Other Settings** > **Rendering** section and enable **Auto Graphics API for a platform (Windows/Mac/Linux)** :
![Using the default graphics APIs](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AutoGraphicsAPICheckboxes.png) Using the default graphics APIs


When you enable **Auto Graphics API for a platform (Windows/Mac/Linux)** , the Player build includes a set of built-in graphics APIs and uses the appropriate one at runtime to produce a best case scenario.
## Override default graphics APIs
You can override the default graphics APIs and use an alternate graphics API for the Editor and Player. Use the following steps:
  1. In the **Player settings** > **Other settings** > **Rendering** section, disable the **Auto Graphics API for a platform (Windows/Mac/Linux)**. 
When **Auto Graphics API for a platform (Windows/Mac/Linux)** is disabled, the Unity Editor displays a list of supported graphics API for that platform and uses the first API in the list. The graphics API at the top of the **Graphics API** list is the default API. If the default API isn’t supported by a specific platform, Unity uses the next API in the **Graphics API** list.
  2. Select the **Add** (**+**) button, then select the graphics API from the dropdown.
![Adding OpenGLCore to the Graphics APIs for Windows list](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SelectGraphicsAPIs.png).


You can reorder the graphics APIs in the list. For example, to check how your application runs on OpenGL Core in the Editor, move **OpenGLCore** to the top of the list and the Editor switches to use OpenGL Core rendering.
For information on how graphics rendering behaves between the platforms and **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) language semantics, refer to [Platform-specific rendering differences](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html).
## Additional resources
  * [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
  * [Surface Shaders with DX11 / OpenGL Core Tessellation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
Graphics API support
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html)
DirectX
