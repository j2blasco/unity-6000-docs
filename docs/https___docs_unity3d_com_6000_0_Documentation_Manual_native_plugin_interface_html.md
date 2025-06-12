* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)
  * Low-level native plug-in interface


[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html)
Building plug-ins for desktop platforms
[](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-rendering-extensions.html)
Low-level native plug-in rendering extensions
# Low-level native plug-in interface
[Native Plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in) in Unity can receive callbacks when certain events happen. You can use this to implement low-level rendering in your **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) so it can work with Unity’s multithreaded rendering.
## Interface Registry
To handle main Unity events, a plug-in must export `UnityPluginLoad` and `UnityPluginUnload` functions. IUnityInterfaces enables the plug-in to access these functions, which you can find in `IUnityInterface.h` in the plug-in API:
```
#include "IUnityInterface.h"
#include "IUnityGraphics.h"
// Unity plugin load event
extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginLoad(IUnityInterfaces* unityInterfaces)
{
    IUnityGraphics* graphics = unityInterfaces->Get<IUnityGraphics>();
}

```

## Access to the graphics device
Use the `IUnityGraphics` interface, which you can find in `IUnityGraphics.h`, to give a plug-in access to generic graphics device functionality. This script demonstrates how you can use the `IUnityGraphics` interface to register a callback:
```
#include "IUnityInterface.h"
#include "IUnityGraphics.h"
    
static IUnityInterfaces* s_UnityInterfaces = NULL;
static IUnityGraphics* s_Graphics = NULL;
static UnityGfxRenderer s_RendererType = kUnityGfxRendererNull;
    
// Unity plugin load event
extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginLoad(IUnityInterfaces* unityInterfaces)
{
    s_UnityInterfaces = unityInterfaces;
    s_Graphics = unityInterfaces->Get<IUnityGraphics>();
        
    s_Graphics->RegisterDeviceEventCallback(OnGraphicsDeviceEvent);
        
    // Run OnGraphicsDeviceEvent(initialize) manually on plugin load
    // to not miss the event in case the graphics device is already initialized
    OnGraphicsDeviceEvent(kUnityGfxDeviceEventInitialize);
}
    
// Unity plugin unload event
extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginUnload()
{
    s_Graphics->UnregisterDeviceEventCallback(OnGraphicsDeviceEvent);
}
    
static void UNITY_INTERFACE_API
    OnGraphicsDeviceEvent(UnityGfxDeviceEventType eventType)
{
    switch (eventType)
    {
        case kUnityGfxDeviceEventInitialize:
        {
            s_RendererType = s_Graphics->GetRenderer();
            //TODO: user initialization code on graphics device initialization. 
            For example, D3D11 resource creation.
            break;
        }
        case kUnityGfxDeviceEventShutdown:
        {
            s_RendererType = kUnityGfxRendererNull;
            //TODO: user graphics API code to call on graphics device shutdown.
            break;
        }
        case kUnityGfxDeviceEventBeforeReset:
        {
            //TODO: user graphics API code to call before graphics device reset.
            break;
        }
        case kUnityGfxDeviceEventAfterReset:
        {
            //TODO: user graphics API code to call after graphics device reset.
            break;
        }
    };
}

```

## Plug-in callbacks on the rendering thread
You can use multithreading to render in Unity, if the platform and number of available CPUs allows for it. 
**Note** : When you use multithreaded rendering, the rendering API commands happen on a thread that’s completely separate from the thread that runs MonoBehaviour **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). The communication between the main thread and the render thread means that your plug-in might not start rendering immediately, depending on how much work the main thread has pushed to the render thread.
To render from the plug-in, call [GL.IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.IssuePluginEvent.html) from your **managed plug-in** A managed .NET assembly that is created with tools like Visual Studio for use in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Managedplug-in) script. This causes Unity’s rendering pipeline to call the native function from the render thread, as demonstrated in the code example below. For example, if you call GL.IssuePluginEvent from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s OnPostRender function, the function will call a plug-in callback immediately after the camera has finished rendering.
Native plugin code:
```
// Plugin function to handle a specific rendering event
static void UNITY_INTERFACE_API OnRenderEvent(int eventID)
{
    // User rendering code
}
    
// Freely defined function to pass a callback to plugin-specific scripts
extern "C" UnityRenderingEvent UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    GetRenderEventFunc()
{
    return OnRenderEvent;
}

```

Managed plug-in code:
```
#if UNITY_IPHONE && !UNITY_EDITOR
[DllImport ("__Internal")]
#else
[DllImport("RenderingPlugin")]
#endif
private static extern IntPtr GetRenderEventFunc();
    
// Queue a specific callback to be called on the render thread
GL.IssuePluginEvent(GetRenderEventFunc(), 1);

```

The signature for the `UnityRenderingEvent` callback is provided in [IUnityGraphics.h in the Native Rendering Plugin sample](https://github.com/Unity-Technologies/NativeRenderingPlugin/tree/master/PluginSource/source/Unity).
## Plug-in using the OpenGL graphics API
There are two kinds of OpenGL objects: 
  * **Objects shared across OpenGL contexts** , such as texture, buffer, renderbuffer, samplers, query, **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), and program objects.
  * **Per-OpenGL context objects** , such as vertex array, framebuffer, program pipeline, transform feedback, and sync objects.


Unity uses multiple OpenGL contexts. When initializing and closing the Editor and the Player, Unity relies on a master context, but when rendering it uses dedicated contexts. That is, you can’t create per-context objects during `kUnityGfxDeviceEventInitialize` and `kUnityGfxDeviceEventShutdown` events.
## Additional resources
  * [Low-level native plug-in rendering extensions](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-rendering-extensions.html)
  * [Low-level native plug-in shader compiler access](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [Low-level native plug-in memory manager API](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-memory-manager-api.html)
  * [Low-level native plug-in memory manager API reference](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-memory-manager-api-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html)
Building plug-ins for desktop platforms
[](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-rendering-extensions.html)
Low-level native plug-in rendering extensions
