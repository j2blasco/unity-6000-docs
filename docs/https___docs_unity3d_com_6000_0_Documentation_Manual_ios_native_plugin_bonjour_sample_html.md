* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ios-native-plugin-bonjour-sample.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * [Native plug-ins for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForIOS.html)
  * [Use your native plug-in for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-native-plugin-use.html)
  * Bonjour browser sample


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-native-plugin-automated-integration.html)
Automated plug-in integration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-iOS.html)
Integrating Unity into native iOS applications
# Bonjour browser sample
For a simple example of how to use a native **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), download the [Bonjour Browser Sample](https://docs.unity3d.com/6000.0/Documentation/uploads/Examples/iPhoneNativeCodeSample.zip).
This example demonstrates how you can invoke Objective-C code from a Unity iOS application. This application implements a simple Bonjour client and consists of:
  * A Unity iOS Project where `Plugins\Bonjour.cs` is the C# interface to the native code, and `BonjourTest.cs` is the script that implements the application logic.
  * Native code (located in `Assets/Plugins/iOS`) that will be added to the built Xcode project as described in [Automated plug-in integration](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-native-plugin-automated-integration.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-native-plugin-automated-integration.html)
Automated plug-in integration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-iOS.html)
Integrating Unity into native iOS applications
