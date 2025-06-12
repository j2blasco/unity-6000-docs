* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-technical-overview.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-intro.html)
  * Technical limitations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browsercompatibility.html)
Web browser compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-gettingstarted.html)
Web development and publishing process
# Technical limitations
Web technology imposes restrictions on Unity web applications designed to run in web browsers. Make sure you’re aware of the following technical limitations before you build your application for the Web platform.
## Platform support
Most popular desktop browser versions support Unity Web content, but do note that different browsers offer [different levels of support](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browsercompatibility.html).
The following features in Web builds are either not available or limited due to constraints of the platform itself:
### Lack of Web build debug support in Visual Studio
Debugging Web builds isn’t supported in Visual Studio. For more information, refer to [Debug and troubleshoot Web builds](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-debugging.html).
### Lack of Unity cache and caching script support
Web builds don’t support the Unity Cache and Caching Scripting API due to restricted access to the filesystem in browsers. Network requests to asset data and AssetBundles are instead cached in the browser cache. Refer to [Cache behavior in Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-caching.html).
### Lack of managed threading support
Managed (C#) threads aren’t supported due to the lack of a multithreaded garbage collection feature in WebAssembly. You can enable partial support for threading in the form of native C/C++ threads with the experimental **Player** setting **Native C/C++ Multithreading**. Refer to [Multithreading support](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-technical-overview.html#multithreading-support).
Due to this limitation, anything in the C# `System.Threading` namespace isn’t supported. For example, use of the `System.Threading.Timer` class doesn’t trigger in Web builds. As well, any timeouts specified in `System.Threading.CancellationTokenSource` don’t actually time out, because the cancellation mechanism is based on `System.Threading.Timer`.
The following code highlights these behavioral differences:
```
using System.Threading;
using UnityEngine;

public class NoMultithreadedTimers : MonoBehaviour
{
    private Timer t;
    private static void TimerCallbackElapsed(object obj)
    {
        Debug.Log("Timer Callback Fired!"); // This will never fire in Web builds because multithreaded timers aren't available.
    }
    private void Awake()
    {
        t = new Timer(new TimerCallback(TimerCallbackElapsed), this, 1, -1);
    }
}

public class NoCancellationTokenSourceTimeouts : MonoBehaviour
{
    private CancellationTokenSource cs;
    private void Awake()
    {
        cs = new CancellationTokenSource(0); // millisecondsDelay=0 to time out immediately
    }
    private void Update()
    {
        Debug.Log(cs.IsCancellationRequested.ToString()); // Will return false in Web builds since timeouts aren't tracked for cancellation tokens.
    }
} 

```

### Networking limitations
There are a few **networking** The Unity system that enables multiplayer gaming across a computer network. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/multiplayer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Networking) features that Web platform doesn’t support: 
  * Browsers don’t allow direct access to IP sockets for networking due to security concerns. For more information, refer to [Web networking](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-networking.html).
  * .NET networking classes within the `System.Net` namespace aren’t supported.
  * Web platform doesn’t support native socket access because of security limitations within browsers. Therefore, Web also doesn’t support features like ICMP ping or [UnityEngine.Ping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping.html). 


### Graphics limitations
There are some limitations in Web platform with the **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) graphics API, which is based on the functionality of the OpenGL ES graphics library. For more information, refer to [Web graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-graphics.html).
### Audio limitations
Web builds use a custom back end for audio based on the **Web Audio** API, but it only supports the basic audio functionality. For more information, refer to [Audio in Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html).
### Dynamic generation of code
Web is an AOT platform, so it doesn’t allow dynamic generation of code using `System.Reflection.Emit`. This is the same on all other **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) platforms, iOS, and most consoles.
## Multithreading support 
Although Unity provides multithreading support for native C/C++ code, the Web platform doesn’t yet support C# multithreading due to limitations of WebAssembly. This means that applications built using the Web platform must run on a single C# thread. 
**Notes** : 
  * The Web platform supports C/C++ multithreading only if you enable [Native C/C++ support](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html#multithreading) in the Web **Player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings).
  * The Web platform supports multithreading, when your document is within a secure context. 
The following HTTP response headers must be set by the server.
    * [Cross-Origin-Opener-Policy: same-origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)
    * [Cross-Origin-Embedder-Policy: require-corp](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy)
    * [Cross-Origin-Resource-Policy: cross-origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Resource-Policy)


The recommended way to perform complex asynchronous tasks on the Web platform is to use [`Awaitable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Awaitable.html), which can replace `System.Threading.Tasks.Task` in most cases. For details, refer to [Introduction to asynchronous programming with Awaitable](https://docs.unity3d.com/6000.0/Documentation/Manual/async-awaitable-introduction.html).
You can also use [coroutines](https://docs.unity3d.com/6000.0/Documentation/Manual/Coroutines.html) for asynchronous workflows. But note that `Awaitable` can return values directly and automatically throws errors, while coroutines require additional logic for both of these tasks.
The following factors limit the multithreading support:
### Constraints on native stack scanning
The Web platform uses WebAssembly, which is a bytecode format for secure and efficient execution of Unity code in web browsers. Web browsers are designed to run the code in a secure and isolated environment which blocks direct access to the native WebAssembly stack. This affects multithreaded garbage collection as the Web garbage collector runs only once at the end of every frame unlike incrementally over multiple frames on other platforms.
### No pre-emptive thread signaling support
Background Workers on the web execute code in parallel independently from each other. On native platforms, the main thread can synchronously send signals to the other threads to pause for garbage collection. This synchronous signaling isn’t supported on the web, which prevents WebAssembly compiled C# code from running in multiple threads.
## Build and run limitations
Unity uses a web server with only basic functionality to host web builds created with **Build and Run** (menu: **Edit** > **Build Profiles** > **Build and Run**).
The server doesn’t support data caching, which affects:
  * The `.data` file, which includes all **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and assets of a build that don’t use [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html) or [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest?subfolder=/manual/index.html).
  * Addressables and AssetBundle files.


## Additional resources
  * [Secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts)
  * [Garbage collection](https://docs.unity3d.com/2023.3/Documentation/Manual/webgl-memory.html#garbagecollection)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browsercompatibility.html)
Web browser compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-gettingstarted.html)
Web development and publishing process
