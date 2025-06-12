* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-macos.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/AppleMac.html)
  * [Developing for macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/macosdevelopment.html)
  * Deep linking for macOS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/macosdevelopment.html)
Developing for macOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macOSIL2CPPScriptingBackend.html)
Use IL2CPP with macOS
# Deep linking for macOS
Deep links are hyperlinks that take a user to a specific location within an app rather than a website. When a user clicks a deep link, the application opens from the designated location, such as a specific **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in a Unity application. There are two ways to enable deep links for macOS applications: URL schemes and universal links. 
For information on how to use deep links and handle them when your application opens, refer to [Using deep links](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking.html#using-deep-links).
## URL schemes
A URL scheme specifies a link structure that your macOS application refers to. The device opens the application when the user clicks a deep link that matches the URL scheme structure. To add a URL scheme, use the following:
  1. Go to **Edit** > **Project Settings** > **Player** > **Other Settings**.
  2. In the Mac Configuration section, set the following properties: 
     * **Size** property to `1`.
     * **Element 0** property to the URL scheme to use with your application. For example, use `unitydl` to open your application when the device processes a link that starts with `unitydl://`.

![Supported URL schemes settings for macOS.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/macos-supported-url.png) Supported URL schemes settings for macOS.
**Note** : To use multiple URL schemes in your project, increase the value of the **Size** property.
## Universal links
Universal links are similar to deep links because they open a specific location within an app. However, if the app isn’t installed, a universal link opens a URL in Safari. To enable universal links, refer to Apple’s documentation on [Allowing Apps and Websites to Link to Your Content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).
## Additional resources
  * [Deep linking](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macosdevelopment.html)
Developing for macOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macOSIL2CPPScriptingBackend.html)
Use IL2CPP with macOS
