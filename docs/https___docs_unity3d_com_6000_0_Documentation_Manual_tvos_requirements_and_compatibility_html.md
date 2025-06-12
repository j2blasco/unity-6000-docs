* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-requirements-and-compatibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [tvOS](https://docs.unity3d.com/6000.0/Documentation/Manual/tvOS-introducing.html)
  * Requirements and compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvOS-introducing.html)
tvOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-player-settings.html)
tvOS Player Settings
# Requirements and compatibility
Although the Apple TV platform (tvOS) is similar to the iOS platform, there are some differences between the two. Before developing your application for tvOS, review the requirements, compatibility notes, and known limitations. 
## Xcode version support
When developing for iOS, it’s recommended to use Xcode version 15+. For more information, refer to [Xcode](https://developer.apple.com/support/xcode/).
## Compatibility
It’s best practice to create a separate branch or copy of your application and port that to Apple TV. tvOS only supports a subset of the iOS framework. This means that **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) that are compatible with iOS might not be compatible with tvOS.
If your app uses more than 4 GB on disk, break it into smaller parts and use On Demand Resources.
**Note:** Bitcode is included with tvOS builds, which adds around 130 MB to your executables. App Store servers strip this code, so it doesn’t affect your distribution size. To estimate Bitcode size, analyze the [LLVM](https://en.wikipedia.org/wiki/LLVM) sections in your executable from the command line with `otool -1`.
## Implementing support for On Demand Resources
tvOS limits how much disk space your application can reserve. The main application installation bundle size can’t be larger than 4 GB. The limits for additional downloadable content are up to 2 GB for in-use assets, and up to 20 GB of total downloadable content. Apple recommends the use of On Demand Resources (ODR) for tvOS downloadable content, which is the best disk space management for tvOS. Unity supports ****ODR** On-demand resources (ODR) is a feature available for the iOS and tvOS platforms, from version 9.0 of iOS and tvOS onwards. It allows you to reduce the size of your application by separating the core assets (those that are needed from application startup) from assets which may be optional, or which appear in later levels of your game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AppThinning.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ODR)** via **Asset Bundles**.
## Known limitations
  * The on-screen keyboard is limited to single line entries.
  * [tvOS Simulator](https://developer.apple.com/documentation/xcode/running-your-app-in-the-simulator-or-on-a-device/) doesn’t emulate the Apple TV Remote as an app controller, which means apps can’t access its input.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvOS-introducing.html)
tvOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-player-settings.html)
tvOS Player Settings
