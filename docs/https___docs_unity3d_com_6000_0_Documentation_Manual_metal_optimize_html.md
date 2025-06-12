* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/metal-optimize.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
  * [Metal](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html)
  * Optimize Metal graphics


[](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-debug.html)
Debug Metal graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OpenGLCoreDetails.html)
OpenGL Core
# Optimize Metal graphics
Metal supports multiple optimizations that you can use to increase the performance of your application.
## Use memoryless render targets
Metal supports memoryless render targets which enables you to render to a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) without backing it up in system memory. Unity only stores the contents temporarily in the on-tile memory during rendering.
Metal supports memoryless render targets on mobile devices from iOS 10.0, tvOS 10.0, visionOS 1.0, and on desktop devices (including Apple silicon) from macOS 11.
## Additional resources
  * [RenderTexture.memorylessMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-memorylessMode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-debug.html)
Debug Metal graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OpenGLCoreDetails.html)
OpenGL Core
