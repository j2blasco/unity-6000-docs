* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-BuildProcess.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Building and delivering for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-building-and-delivering.html)
  * Build an iOS application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-building-and-delivering.html)
Building and delivering for iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettingsiOS.html)
iOS build settings reference
# Build an iOS application
The process of building an iOS application with Unity has two main steps:
  1. Unity generates an Xcode project.
  2. Xcode builds the generated project into the application.


For further information on how Unity builds iOS applications, refer to [How Unity builds iOS applications](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-ios-applications.html).
**Note** : To build an iOS application locally, your development machine must run macOS as Xcode is available only on macOS devices. If you don’t have a macOS device, you can use [Unity Build Automation](https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-build-automation)A continuous integration service for Unity projects that automates the process of creating builds on Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-build-automation)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UnityBuildAutomation) to build your applications in the cloud.
Before you build your Project for iOS, make sure that you set the **Bundle Identifier** in the iOS [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html#other)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) (menu: **Edit** > **Project Settings** > **Player Settings**). You can also choose whether your app targets the simulator or an actual device. To do this, change the **SDK version** field.
## Build an Xcode project from the Unity Editor
To build an Xcode project for iOS, use the following steps:
  1. Select **File** > **Build Profiles**.
  2. Select **Add**Build Profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)** to open the Platform Browser window.
  3. From the list of platforms in the **Platform** pane, select **iOS**. If **iOS** isn’t an option, select **Install with Unity Hub** and follow the installation instructions.
  4. Select **Add Build Profile**.
  5. Select **Switch Profile** to set the new build profile as the active profile.
  6. Set any [build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettingsiOS.html) your project requires.
  7. Choose either **Build** or **Build and Run**. If you select **Build and Run** and use a macOS device, Xcode builds the generated project into the application and then installs the application to a connected iOS device.
  8. Choose or create a directory for Unity to build the Xcode project in. If an Xcode project already exists in the target directory, an alert displays with options on how to proceed. For information on the options available, refer to [Replace and append mode](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-BuildProcess.html#replace-and-append-mode).


**Tip** : After you specify the target directory for the first time, you can use **Cmd+B** to build and run the application. Unity uses the **Append** mode to regenerate the Xcode project.
For more information on running an Xcode project in Xcode, refer to [Building and running an app](https://developer.apple.com/documentation/xcode/building-and-running-an-app)(Apple Developer).
### Replace and append mode
If you build a project in a directory that already contains another Xcode project, Unity displays an alert and a choice on how to proceed. There are two options:
  * **Replace** : Unity removes everything in the target Xcode project directory. It then generates the new Xcode project in the now empty directory.
  * **Append** : Unity removes all files in the target Xcode project root directory and in the `Data` and `Libraries` subdirectories. It then fills these directories with newly generated Xcode project content. Unity then updates the Xcode project file according to the latest Unity project changes. Unity only supports this mode for the existing Xcode projects generated with the same Unity iOS version. You can store custom built-in code in the `classes` subdirectory, as files here aren’t removed.


## Run an Xcode project from the command line
After Unity generates the Xcode project, you can build and run the Xcode project from the command line. To do this, use the following steps:
  1. Open a Terminal window.
  2. Navigate to the Xcode project directory.
  3. Find the device ID of the device you want to run the application on. You can find this in Xcode under **Window** > **Devices and Simulators**.
  4. Enter the following command into the Terminal where `<device-id>`is your device ID.

```
unity$ xcodebuild test -destination "platform=iOS,id=<device-id>" -scheme Unity-iPhone

```

### Specify build settings for specific targets
When you use command line arguments to specify build settings, they apply to all [targets](https://docs.unity3d.com/6000.0/Documentation/Manual/StructureOfXcodeProject.html#Xcode-project-targets) in your Xcode project. To prevent this, some build settings have suffixed versions which you can use to specify which target your build settings affect. You can implement this through **User-Defined** settings in **Xcode** > **Build Settings**. The `APP` suffix is used for the application targets and the `FRAMEWORK`suffix is used for the framework targets. 
When building with xcodebuild, use suffixed versions for the following build settings:
**Xcode build setting** | **Suffixed version**  
---|---  
PRODUCT_NAME | PRODUCT_NAME_APP  
PROVISIONING_PROFILE | PROVISIONING_PROFILE_APP  
PROVISIONING_PROFILE_SPECIFIER | PROVISIONING_PROFILE_SPECIFIER_APP  
OTHER_LDFLAGS | OTHER_LDFLAGS_FRAMEWORK  
Based on your custom build pipeline, you can extend the list to cover other settings.
## Additional resources
  * [How Unity builds iOS applications](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-ios-applications.html)
  * [Structure of a Unity Xcode project](https://docs.unity3d.com/6000.0/Documentation/Manual/StructureOfXcodeProject.html)
  * [iOS build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettingsiOS.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-building-and-delivering.html)
Building and delivering for iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettingsiOS.html)
iOS build settings reference
