* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-building-your-application.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [tvOS](https://docs.unity3d.com/6000.0/Documentation/Manual/tvOS-introducing.html)
  * Build your application for tvOS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-debugging.html)
Debugging your tvOS application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
Universal Windows Platform
# Build your application for tvOS
To build your Unity application for tvOS, use the following steps:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **tvOS** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **tvOS** platform.
  3. In the **Platform Settings** section, set **Architecture** to the architecture type you want Unity to build your application for.
  4. If you want to create an [Xcode project](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Projects.html) for your application, enable **Create Xcode Project**.
  5. Select **Switch Profile** to set the new **build profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) as the active profile.
  6. Click **Build**.


Similar to iOS, building your application to a tvOS device involves two steps:
  1. Unity builds an [Xcode project](https://docs.unity3d.com/2021.2/Documentation/Manual/StructureOfXcodeProject.html).
  2. Xcode builds that project to your device.


To select the device that Xcode builds to, follow these steps:
  1. Connect the device to your computer.
  2. From Xcode’s main menu, go to **Product** > **Destination** , and select your device from the Devices list.


tvOS build settings are the exact same as those for iOS. Refer to [iOS build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettingsiOS.html) to check which settings you can configure for your build.
## Incremental build pipeline
Unity uses the [incremental build pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html) when it builds the Player for tvOS. This means that Unity incrementally builds/generates files such as [Information Property List](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html) (plist) files and [Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements) files. If you implement callbacks that modify or move any iOS file or asset that the incremental build pipeline uses, see [Creating non-incremental builds](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html#creating-non-incremental-builds).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-debugging.html)
Debugging your tvOS application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
Universal Windows Platform
