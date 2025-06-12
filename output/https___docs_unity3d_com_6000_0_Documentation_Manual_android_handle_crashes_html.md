* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-handle-crashes.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * Handle Android crashes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html)
Request runtime permissions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-quit.html)
Quit a Unity Android application
# Handle Android crashes
Crash handling for Unity applications on Android works as a chain of crash handlers. The crash handler at the start of the chain receives the crash first and it can process the crash and also forward the crash to the next crash handler in the chain. The order of the crash handlers in the chain is defined by the order in which they’re installed. The crash handler installed first is the last one to receive the crash and the crash handler installed last is the first one to receive the crash. By default, Unity acts as the first crash handler in the chain. It processes crashes and forwards them to the next crash handler in the chain, which is the Android system crash handler by default.
You can configure Unity to react differently to crashes and also add your own custom crash handler to the chain. This page explains how to specify the method Unity uses to handle crashes and how to create a custom crash handler.
## Specify how Unity handles crashes
If you don’t want to use Unity’s default crash handling behavior, you can use the `-androidChainedSignalHandlerBehavior` command-line argument to change how Unity reacts to crashes. This argument takes one of the following values:
**Behavior value** | **Description**  
---|---  
`legacy` | When a native crash occurs, Unity wraps and throws the crash as a java exception. Unity doesn’t forward the crash to any installed crash handlers or to the default system.  
  
**Note:** This behavior value isn’t supported by GameActivity and will be removed in future Unity versions.  
`disabled` | When a native crash occurs, Unity ignores it and Android forwards the crash directly to the next crash handler in the chain. This is either a custom crash handler, if one is installed, or the default system if not.  
  
**Note** : If you use this value, Unity services such as Unity Cloud Diagnostics no longer handle crashes and won’t report them.  
For information on how to pass this command-line argument to Unity, see [Specify Unity start-up arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity-command-line.html).
## Create and setup a custom crash handler
This section contains an example of how to create and set up your own crash handler. For this to work, you must not use Unity’s legacy crash handling behavior. For more information, refer to [Specify how Unity handles crashes](https://docs.unity3d.com/6000.0/Documentation/Manual/android-handle-crashes.html#specify-how-unity-handles-crashes).
### Create a crash handler
The following code sample shows a custom crash handler. If you use the [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) [scripting backend](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend), you can place this example `cpp` file directly into your Unity project. Unity then compiles it as part of `libil2cpp.cpp`. If you use the [Mono](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-mono.html)A scripting backend used in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mono) scripting backend, you must compile and link your own shared library. For more information, refer to [Create a native plug-in for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-create.html). 
**android_crash_handler.cpp**
```
#include <android/log.h>
#include <jni.h>
#include <signal.h>

struct sigaction s_PreviousHandler;
bool s_SignalHandlerInstalled;

static void MyCustomHandler(int sig, siginfo_t* info, void* ucontext)
{
  __android_log_print(ANDROID_LOG_VERBOSE, "CustomCrashHandler", "Handling signal %d", sig);
  s_PreviousHandler.sa_sigaction(sig, info, ucontext);
}

extern "C" void InstallCustomSignalHandlers()
{
  struct sigaction Action = {};
  Action.sa_sigaction = MyCustomHandler;
  // Note: Register more signals if you want.
  Action.sa_flags = SIGSEGV;
  sigaction(SIGSEGV, &Action, &s_PreviousHandler);
  s_SignalHandlerInstalled = true;
}

extern "C" JNIEXPORT void Java_com_unity3d_player_UnityPlayerActivity_InstallCustomSignalHandlersFromJava()
{
  InstallCustomSignalHandlers();
}

extern "C" void UninstallCustomSignalHandlers()
{
  if (s_SignalHandlerInstalled)
  {
      sigaction(SIGSEGV, &s_PreviousHandler, nullptr);
      s_SignalHandlerInstalled = false;
  }
}

```

### Install the crash handler
To install the crash handler and have Unity use it to handle crashes, call the `InstallCustomSignalHandlers` method in the above `cpp` file. You can do this either through [C#](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-call.html) or Java code, however it’s best practice to call this method from Java, because a crash can occur after the Unity Player initializes, but before your C# code runs.
The following code sample shows how to call the `InstallCustomSignalHandlers` method from Java code. To add it to your project, you can either install the Java file as a **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) (refer to [Create a Java or Kotlin source plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html#CreateSourcePlugins)) or you can modify an existing Java file in an [exported project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html).
**Note** : Depending on where you call this method, it changes the behavior of crash handling. If you call it before Unity runtime initialization, which is a line of code that contains `mUnityPlayer = new UnityPlayer(this, this);`, then during the native crash Unity’s crash handler is executed first and then your signal handler is executed (if Unity forwards the signal). If you call `InstallCustomSignalHandlers` after Unity runtime initialization, then during the native crash your handler is executed first and it’s your responsibility to forward the signal.
**UnityPlayerActivity.java**
```
...
  public native void InstallCustomSignalHandlersFromJava();
  static
  {
      System.loadLibrary("il2cpp");
  }
  // Setup activity layout
  @Override protected void onCreate(Bundle savedInstanceState)
  {
      InstallCustomSignalHandlersFromJava();
      ...
      mUnityPlayer = new UnityPlayer(this, this);
      setContentView(mUnityPlayer);
      mUnityPlayer.requestFocus();
  }
...

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html)
Request runtime permissions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-quit.html)
Quit a Unity Android application
