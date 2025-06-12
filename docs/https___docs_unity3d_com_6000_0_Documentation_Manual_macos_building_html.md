* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/AppleMac.html)
  * [Building and delivering for macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-delivery.html)
  * Build a macOS application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-delivery.html)
Building and delivering for macOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html)
macOS build settings reference
# Build a macOS application
Refer to the following instructions and considerations on building your Unity application for macOS.
## Target architecture
Before you build an application for macOS, be aware of the chipset differences between Apple devices. Some Apple devices use Intel chipsets and others use Apple silicon. You can use Unity to create both architecture-specific builds and builds that target both Intel and Apple silicon. The available target architectures are:
**Architecture** | **Description**  
---|---  
**Intel 64-bit** | Use Intel 64-bit to build for Apple devices with Intel chipsets.  
**Apple silicon** | Select Apple silicon to build for Apple devices that use the silicon architecture.  
**Intel 64-bit + Apple silicon** | Use Intel 64-bit + Apple silicon to generate a macOS build that works on both Intel chipsets and Apple silicon.  
  
**Note** : This results in a build that’s larger than the individual architecture-specific builds, impacting the application size.  
You can set the target architecture for your application from the [macOS build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html) in the ****Build Profiles** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)** window.
## Build the application
To build your Unity application, use the following steps:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **macOS** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **macOS** platform.
  3. In the **Platform Settings** section, set **Architecture** to the architecture type you want Unity to build your application for.
  4. If you want to create an [Xcode project](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Projects.html) for your application, enable **Create Xcode Project**.
  5. Select **Switch Profile** to set the new build profile as the active profile.
  6. Click **Build**.


**Note** : If building a macOS application on Windows, you must set the executable flag for the binary before opening the application on macOS. 
### Duplicate native source files
When building for macOS, using multiple native source files as **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) with the same name that target the same build will cause a build failure.
For example, if two or more files with the same name target different architectures, such as macOS ARM64 and macOS x64, and you build a Universal app that includes both architectures, the build will fail. This is because both files are included in the build, causing build conflicts. 
As Xcode doesn’t support the use of files targeting different architectures, you need to merge your files into one or rename them to ensure they’re compatible with both architectures.
## Information property list file
macOS applications require an information property list file called `Info.plist` that has metadata and configuration information for the application. The file holds a list of key-value pairs.
When Unity builds your application, it creates the `Info.plist` file. Unity stores this file at **ApplicationName.app** > **Contents** > **Info.plist**. Unity displays required `Info.plist` configuration properties in the [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) window that you can set before building the application. These properties are in the **Other Settings** > **Mac App Store Options** section.
There are additional keys that you can add to your `Info.plist` file. To add them, build the application and use a text editor to edit the file. For information about the available keys, refer to [About Info.plist Keys and Values](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html).
## Entitlements
macOS applications require [entitlements](https://developer.apple.com/documentation/bundleresources/entitlements) to specify permissions and restrictions that control specific actions of your application. Your application must include entitlements that result in a [Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime). These entitlements protect your application from code injection, hijacking of dynamically linked libraries, and memory tampering.
To define entitlements, macOS applications use an XML file with the `.entitlements` file extension. macOS applications then use a process called [code signing](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building.html#code-signing) to bind the entitlements to an application.
If your application uses plug-ins that perform macOS platform-specific actions, you might need to add entitlements to enable those actions. For more information on what actions require entitlements, refer to [Apple Developer Entitlements](https://developer.apple.com/documentation/bundleresources/entitlements).
## Code signing & notarization
Code signing is the process of creating a code signature for an application. This signature guarantees the integrity of applications and safeguards from any tampering. Apple devices use an application’s code signature to detect changes made after the developer created the code signature. If an application doesn’t have a code signature, the device warns the end user before they open the application.
Notarization is the process Apple uses to check that Developer ID-signed applications don’t contain malicious content. Digital distribution services often require you to notarize your application before you can share it on their platform. The Mac App Store has a content validation system that’s similar to notarization, which means that applications distributed through the store don’t require prior notarization.
For more information on code signing and notarization, refer to [Code sign and notarize your macOS application](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building-notarization.html).
## Additional resources
  * [macOS build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html)
  * [Code sign and notarize your macOS application](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building-notarization.html)
  * [BuildOptions API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-delivery.html)
Building and delivering for macOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html)
macOS build settings reference
