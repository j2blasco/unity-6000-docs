* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Debugging and diagnostics](https://docs.unity3d.com/6000.0/Documentation/Manual/debugging-and-diagnostics.html)
  * Debug C# code in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/debugging-and-diagnostics.html)
Debugging and diagnostics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html)
The Debug class
# Debug C# code in Unity
You can use a debugger to inspect your source code while your application is running. Unity supports the following code editors to debug C# code:
  * Visual Studio (with the [Visual Studio Tools for Unity](https://docs.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/visual-studio-tools-for-unity) plug-in)
  * Visual Studio Code (with the [Unity for Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=visualstudiotoolsforunity.vstuc))
  * Jetbrains Rider


Although these code editors vary slightly in the debugging features they support, they all provide basic functionality such as break points, single stepping, and variable inspection. You can attach these code editors to the [Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#DebugInEditor) or [Unity Player](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#DebugInPlayer) to debug your code.
Managed code debugging in Unity works on all platforms except Web. It works with both the [Mono](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-mono.html)A scripting backend used in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mono) and [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) **scripting backends** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend).
##  Configure the IDE
For the requirements to configure each supported IDE for debugging in Unity, refer to [Integrated development environment (IDE) support](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html).
## Breakpoints
Breakpoints allow you to specify points in your code where you want to pause its execution. In your external code editor, you can set a breakpoint on a line of code where you want the debugger to stop. While the code editor is at a breakpoint, you can view the contents of variables step by step.
If you have attached your code editor to the Unity Editor (see [Attach your code editor to the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#AttachToEditor)), the Unity Editor becomes unresponsive until you choose the continue option in your code editor, or stop debugging mode.
To see how you can set breakpoints in Visual Studio see [Set breakpoints in Visual Studio](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#BreakpointsVS).
##  Debug in the Unity Editor
You can debug C# code as it runs in the Unity Editor while the Unity Editor is in Play Mode.
To debug in the Editor, you need to set the Editor’s Code Optimization mode to **Debug Mode** , then you can [attach a code editor with a debugging feature](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#AttachToEditor).
To change the Code Optimization mode, select the Debug Button in the bottom right of the **Unity Editor Status Bar**.
![The Debug Button in the bottom right of the Unity Editor Status Bar](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/debug-mode.png) The Debug Button in the bottom right of the Unity Editor Status Bar
Unity’s Code Optimization setting has two modes:
  * **Debug Mode** , which you can use to attach external debugger software, but gives slower C# performance when you run your Project in Play Mode in the Editor.
  * **Release Mode** , which gives faster C# performance when you run your Project in Play Mode in the Editor, but you cannot attach any external debuggers.


When you click the Debug button in the status bar, a small pop-up window opens which contains a button you can use to switch modes. The window also displays information about the current mode, and describes what happens if you switch modes.
![The Debug Mode popup, which shows the current mode, allows you to switch modes, and describes what happens if you switch mode.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/debug-popup.png) The Debug Mode popup, which shows the current mode, allows you to switch modes, and describes what happens if you switch mode.
To change which mode the Unity Editor starts up in, go to **Edit** (macOS: **Unity**) > **Preferences** > **General** > **Code Optimization On Startup**.
![In Preferences, you can change the Code Optimization mode that Unity starts in.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/code-op-startup.png) In Preferences, you can change the Code Optimization mode that Unity starts in.
To control these settings using a script, use the following API:
  * [ManagedDebugger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.ManagedDebugger.html)
  * [Compilation.CompilationPipeline-codeOptimization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-codeOptimization.html)
  * [Compilation.CodeOptimization.](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CodeOptimization.html)


You can also override the mode that the Editor starts up in, or turn off the debugger listen socket. To do this, use the following [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html) when you launch the Editor:
  * `-releaseCodeOptimization`. Starts the Editor in **Release** code optimization mode.
  * `-debugCodeOptimization`. Starts the Editor in **Debug** code optimization mode.
  * `-disableManagedDebugger`. Starts the Editor with the debugger listen socket disabled.


###  Attach your code editor to the Unity Editor
The way to attach your code editor to the Unity Editor depends on what code editor you use, and is often a different option from your code editor’s normal debugging process. Some code editors allow you to select an instance of Unity to debug. For instructions specific to your code editor, see [Code editor external documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#ExternalDocs). To see how you can do this in Visual Studio, see [Attach Visual Studio to the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#AttachVSToEditor).
When you have attached the code editor to the Unity Editor and you are ready to begin debugging, return to the Unity Editor and enter Play Mode.
##  Debug in the Unity Player
To compile a Unity Player for you to debug:
  1. Go to **File** > **Build Profiles**.
  2. Enable the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** and **Script Debugging** options before you build the Player. You could also enable the **Wait For Managed Debugger** option to make the Player wait for a debugger to be attached before the Player executes any script code.
  3. Select **Build And Run**.


### Attach your code editor to the Unity Player
To attach your code editor to the Unity Player, in your code editor, select the IP address (or machine name) and port of your Player. For an example of where to find this in Visual Studio, see [Attach Visual Studio to the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#AttachVSToEditor).
**Note** : Your code editor will show all instances of Unity that are available to debug. Make sure you attach the code editor to the correct instance of the Unity Player, and not to the Unity Editor if both are running. 
When you have attached the debugger, you can begin debugging normally. For instructions on how to attach the Unity Player to your specific code editor, see [Code editor external documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#ExternalDocs). For an example of how to attach a Unity Player that runs on a mobile device to Visual Studio, see [Debug Android and iOS devices with Visual Studio](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#DebugMobile).
##  Set breakpoints in Visual Studio
To set a breakpoint in Visual Studio, click on the column to the left of your code, on the line you want to stop the debugger. A red circle appears next to the line number and the line is highlighted.
![A breakpoint in Visual Studio.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/vs-breakpoint.png) A breakpoint in Visual Studio.
##  Attach Visual Studio to the Unity Editor
To attach the Unity Editor to your Visual Studio script, open Visual Studio, go to **Debug** > **Attach Unity Debugger** and select the instance of the Unity Editor you would like to debug.
In the following example image, there is one instance of Unity running in the Editor and one instance of Unity running as an Android Player
![Visual Studio lists the current instances of Unity that are available to debug.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/attach-vs-to-editor.png) Visual Studio lists the current instances of Unity that are available to debug.
##  Debug Android and iOS devices with Visual Studio
### Android
To debug a Unity Player running on an Android device, connect to the device using USB or TCP. For example, to connect to an Android device in Visual Studio, select **Debug** > **Attach Unity Debugger** option. A list of devices running a Player instance appears.
![Visual Studios Attach Unity Debugger interface displays a list of running Unity processes that the debugger can attach to.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/debug-android.png) Visual Studio’s Attach Unity Debugger interface displays a list of running Unity processes that the debugger can attach to.
In this example, the android device is connected using USB and Wi-Fi on the same network as the workstation running the Unity Editor and Visual Studio.
### iOS
To debug a Unity Player running on an iOS device, connect to the device using TCP. For example, to connect to an iOS device in Visual Studio for Mac, select **Debug** > **Attach Unity Debugger**. A list of devices running a Player instance appears.
![Visual Studio for Macs Attach Unity Debugger interface displays a list of running Unity processes that the debugger can attach to.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/debug-ios.png) Visual Studio for Mac’s Attach Unity Debugger interface displays a list of running Unity processes that the debugger can attach to.
Ensure that the device only has one active network interface (Wi-Fi recommended, turn off cellular data) and that there is no firewall between the IDE and the device blocking the TCP port (port number 56000 in the above screenshot).
**Important** : iOS doesn’t support debugging over USB.
## Troubleshoot the debugger
Most problems with the debugger occur because the code editor is unable to locate the Unity Editor or the Unity Player. This means that the Unity Editor or Player can’t attach the debugger properly. Because the debugger uses a TCP connection to the Editor or Player, connection issues are often caused by the network. Below are a few steps you can take to troubleshoot basic connection issues.
### Ensure you attach the debugger to the correct Unity instance
You can attach your code editor to any instance of the Unity Editor or Unity Player on the local network that has debugging enabled. When you attach the debugger, ensure that you attach it to the correct Unity instance. If you know the IP address or machine name of the device on which you are running the Unity Player, this helps to locate the correct instance.
### Verify the network connection to the Unity instance
The code editor uses the same mechanism to locate a Unity instance to debug as the Unity **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler). If the code editor can’t find the Unity instance you expect, try to attach the Unity Profiler to that instance. If the Unity Profiler cannot find the Unity instance either, there might be a firewall on the machine you are running the code editor or Unity instance on. If a firewall is in place, see [Check the firewall settings](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#Firewall).
### Ensure the device only has one active network interface
Many devices have multiple network interfaces. For example, a mobile phone might have both an active cellular connection and an active Wi-Fi connection. To properly connect the debugger to the Unity instance using TCP, the IDE needs to make a network connection to the correct interface on the device. If you plan to debug over Wi-Fi, for example, make sure you put the device in airplane mode to disable all other interfaces, then enable Wi-Fi.
You can determine which IP address the Unity Player tells the IDE to use by looking in the **Player Log** The .log file created by a Standalone Player that contains a record of events, such as script execution times, the compiler version, and AssetImport time. Log files can help diagnose problems. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html#player)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerLog). Look for a part of the log like this:
`Multi-casting "[IP] 10.0.1.152 [Port] 55000 [Flags] 3 [Guid] 2575380029 [EditorId] 4264788666 [Version] 1048832 [Id] iPhonePlayer(Example-iPhone):56000 [Debug] 1 [PackageName] iPhonePlayer" to [225.0.0.222:54997]...`
This message indicates the IDE will try to use the IP address 10.0.1.152 and port 56000 to connect to the device. This IP address and port must be reachable from the computer running the IDE.
###  Check the firewall settings
The Unity instance communicates with the code editor using a TCP connection. On most Unity platforms, this TCP connection occurs on an arbitrarily chosen port. Normally, you shouldn’t need to know this port, as the code editor should detect it automatically. If that doesn’t work, use a network analysis tool to determine which ports might be blocked either on the machine where you are running the code editor, or the machine or device where you are running the Unity instance. When you find the ports, make sure that your firewall allows access to the port on both the machine running the code editor, and the machine running the Unity instance.
### Verify the managed debugging information is available
If the debugger attaches to the Unity instance but breakpoints don’t load, the debugger might not be able to locate the managed debugging information for the code. Managed code debugging information is stored in files named .pdb, next to the managed assembly (.dll file) on the disk.
When you enable the correct preferences and build options (see [Configure the code editor](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#Configure)), Unity generates this debugging information automatically. However, Unity cannot generate debugging information for managed plugins in your project. You can only debug code from managed plugins if the associated .pdb files are next to the managed plugins in the Unity project on disk.
### Prevent the device from locking
Disable any screen locks on the device you are using to debug your application. Screen locks cause the debugger to disconnect, and prevent it from re-connecting. Don’t lock the screen during managed code debugging. If the screen locks, restart the application on the device so the debugger can connect again.
### Memory and thread leaks due to the debugger
The implementation of the managed debugger will leak some OS-level thread handles and some memory related to threads in order to handle some race conditions related to thread startup and shutdown. In practice these leaks are small, and should not impact the resource usage of an application. However, when many threads are created and destroyed, the leaks can be noticeable. This behavior can also make it difficult to track down actual memory leaks, so we recommend disabling scripting debugging when troubleshooting memory leaks.
##  Code editor external documentation
  * Visual Studio - [Using Visual Studio Tools for Unity (Windows)](https://docs.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/using-visual-studio-tools-for-unity?pivots=windows#unity-debugging)
  * Visual Studio Code - [Unity Development with VS Code](https://code.visualstudio.com/docs/other/unity)
  * Jetbrains Rider - [Debug Unity Applications](https://www.jetbrains.com/help/rider/Debugging_Unity_Applications.html)


## Additional resources
  * [Integrated development environment (IDE) support](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/debugging-and-diagnostics.html)
Debugging and diagnostics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html)
The Debug class
