* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/vulkan-swapchain-pre-rotation.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Graphics for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-graphics.html)
  * Framebuffer orientation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Android-SinglePassStereoRendering.html)
Single-pass stereo rendering for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/allow-deny-vulkan-usage.html)
Allow or deny Vulkan API usage
# Framebuffer orientation
If your application’s framebuffer orientation doesn’t match the device’s native display orientation (portrait, for most devices), Android rotates the application’s framebuffer to match the device’s display every frame. Depending on the device’s hardware capabilities, this additional rotation can negatively affect performance. If your application uses the [Vulkan Graphics API](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#auto-graphics-api) and the device supports Vulkan, Unity can apply this rotation during rendering which reduces the performance impact of the rotation. This is called[ pre-rotation](https://android-developers.googleblog.com/2020/02/handling-device-orientation-efficiently.html).
## Using pre-rotation in Unity
To make Unity apply pre-rotation, you can use C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) or the Unity Editor:
  * Through C# scripts: Set [PlayerSettings.vulkanEnablePreTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-vulkanEnablePreTransform.html) to `true`.
  * Through the Unity Editor:
  * Select **Edit** > **Project Settings**.
  * In the **Project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) window, select the **Player** tab, then open [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html).
  * In the **Other Settings** section, enable **Apply display rotation during rendering**.


## How Unity applies pre-rotation
Unity applies pre-rotation when it renders directly to the device’s backbuffer, not when it renders to a [Render Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture). To apply the rotation, Unity modifies the projection matrix which affects the `UNITY_MATRIX_MVP` and `UNITY_MATRIX_P` [Built-in shader variables](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UnityShaderVariables.html). This means that Unity applies the rotation in the vertex **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
Using pre-rotation doesn’t affect the behavior of Unity’s C# API. For example, you can still use `Screen.width` to access the width of the screen. The same applies to **viewports** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport) and [scissor rects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableScissorRect.html). Unity adjusts these as needed, and also handles readback operations from the backbuffer such as Grab Pass, ReadPixels, or Screenshot.
Unity provides utility macros to handle special cases in shaders (for more information, see the [Limitations](https://docs.unity3d.com/6000.0/Documentation/Manual/vulkan-swapchain-pre-rotation.html#limitations) section below).
The macro UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION is only defined if all of the following conditions are true (otherwise, it’s undefined):
  * `preTransform` is enabled in the Player Settings
  * the platform is set to Android
  * the graphics API is set to Vulkan


UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is a constant that is set to the current `preTransform` rotation. Its value is one of the following:
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_0`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_90`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_180`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_270`


If UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION is undefined, or when rendering to a Render Texture, the value of UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is UNITY_DISPLAY_ORIENTATION_0.
UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is translated into a Vulkan specialization constant, which makes it efficient to use in if or switch statements.
## Limitations
In the following cases, it’s likely that enabling preTransform requires additional modifications to your Unity Project before you can use it:
  * Shaders that don’t use Unity’s projection matrix
  * Shaders that depend on the current **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) position in the fragment shader (`SV_Position`)
  * Shaders that use screen space derivatives (ddx, ddy)
  * Native rendering plugins that use the Vulkan swapchain image might need to be modified
  * Use of backbuffer with Unity RenderPass API in an MRT setup together with other Render Textures


These cases only apply when rendering directly to the backbuffer.
## Additional resources
  * [Vulkan Design Guidelines](https://developer.android.com/ndk/guides/graphics/design-notes?hl=sk&authuser=3) on the Android developer website.
  * [Vulkan Mobile Best Practice - Appropriate Use of Surface Rotation](https://community.arm.com/developer/tools-software/graphics/b/blog/posts/appropriate-use-of-surface-rotation) on the arm community website.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Android-SinglePassStereoRendering.html)
Single-pass stereo rendering for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/allow-deny-vulkan-usage.html)
Allow or deny Vulkan API usage
