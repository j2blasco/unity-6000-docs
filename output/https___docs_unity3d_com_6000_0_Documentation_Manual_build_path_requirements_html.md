* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/build-path-requirements.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * Build path requirements for target platforms


[](https://docs.unity3d.com/6000.0/Documentation/Manual/XcodeFrameDebuggerIntegration.html)
Xcode frame debugger Unity integration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
Graphics API support
# Build path requirements for target platforms
When you’re building Players for target platforms using [command-line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html) or C# APIs, such as [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html), you must specify the path for the build location. For certain platforms, this path must also include the build file extension specific to the platform. 
The following table lists such platforms that require you to include build file extensions when building Players using command-line arguments or C# APIs.
**Platform** | **Build file extension**  
---|---  
**Android** | • **Android Package** : `.apk`  
• **Android App Bundle** :`.aab`  
  
**Note** : The file extension isn’t required for the following conditions:  
• When building a Gradle project using **Export Project** build setting   
• When building the Android App Bundle using **Export for App Bundle** build setting.   
  
Instead, specify the folder name for the exported Gradle project or Android App Bundle in the build path.  
**Windows (Standalone and Server)** |  `.exe`  
  
**Note** : The file extension isn’t required when generating a Visual Studio Solution using the **Create Visual Studio Solution** build setting. Instead, specify the folder name for the generated Visual Studio Solution in the build path.  
**macOS (Standalone)** |  `.app`  
  
**Note** : The file extension isn’t required when generating an Xcode project using the **Create Xcode Project** build setting. Instead, specify the folder name for the generated Xcode project in the build path.  
**Linux (Standalone and Server)** | `.x86_64`  
## Additional resources
  * [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)
  * [Command-line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/XcodeFrameDebuggerIntegration.html)
Xcode frame debugger Unity integration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
Graphics API support
