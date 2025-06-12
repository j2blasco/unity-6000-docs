* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ios-environment-setup.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Getting started with iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-GettingStarted.html)
  * iOS environment setup


[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-GettingStarted.html)
Getting started with iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html)
iOS Player settings
# iOS environment setup
To create a Unity application for iOS, you first need to set up your Unity project to support iOS. This information is also relevant to the iPadOS, macOS, and tvOS platforms. To support iOS and other Apple operating systems, a Unity project requires:
  * The iOS Build Support module.
  * [Xcode](https://developer.apple.com/xcode/) or [Unity Build Automation](https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-build-automation)A continuous integration service for Unity projects that automates the process of creating builds on Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-build-automation)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UnityBuildAutomation).


Before you get started, check Unity’s [Requirements and compatibility documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-requirements-and-compatibility.html) for iOS to make sure you’re aware of any limitations for developing a Unity application for this platform.
## Install dependencies
Unity distributes dependencies as [modules](https://docs.unity3d.com/hub/manual/AddModules.html) which means you use the [Unity Hub](https://docs.unity3d.com/hub/manual/index.html) to install them. The module you need is iOS Build Support. You can install it either when you install a new Unity Editor version, or add it to an existing Unity Editor install. To install modules:
  * At install time, refer to [Downloading and installing Editors and modules with the Unity Hub](https://docs.unity3d.com/hub/manual/InstallEditors.html).
  * To an existing install, refer to [Add modules](https://docs.unity3d.com/hub/manual/AddModules.html).


## Install Xcode or set up Unity Build Automation
To build iOS applications, Unity generates an Xcode project and then Xcode builds this project into the final application. This means that if you want to build an application locally, you must install Xcode. Xcode is only available for macOS, so if your development machine doesn’t run macOS, you can’t build an application locally. However, Unity Build Automation can build applications for you which makes it possible for you to develop an iOS application on a non-macOS machine.
  * For information on how to install Xcode, refer to the [Xcode documentation](https://developer.apple.com/xcode/).
  * For information on how to set up Unity Build Automation, refer to [Unity Build Automation](https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-build-automation).


## Set up an Apple ID or join the Apple Developer Program
To test your build on an iOS device, you need a free [Apple ID](https://appleid.apple.com/). However, to distribute your app on the App Store, and to use services such as Game Center or In-App Purchases, you need to register with the [Apple Developer Program](https://developer.apple.com/). For more information about the differences between an Apple ID and Apple Developer Program membership, refer to the Apple’s documentation on [Choosing a Membership](https://developer.apple.com/support/compare-memberships/).
### Add your Apple ID to Xcode
To add your Apple ID to Xcode, follow the steps in Apple’s documentation on [Adding an Apple ID account to Xcode](https://help.apple.com/xcode/mac/current/#/devaf282080a).
## Additional resources
  * [iOS Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-GettingStarted.html)
Getting started with iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html)
iOS Player settings
