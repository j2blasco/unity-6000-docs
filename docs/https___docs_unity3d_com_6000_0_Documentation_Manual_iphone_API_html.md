* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-API.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * iOS Scripting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
Developing for iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-input.html)
Input for iOS devices
# iOS Scripting
Most features of the iOS devices are exposed through the [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) and [Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html) classes. For cross-platform projects, **UNITY_IPHONE** is defined for conditionally compiling iOS-specific C# code.
## Device properties
There are a number of device-specific properties that you can access. See the script reference pages for:
  * [SystemInfo.deviceUniqueIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html)
  * [SystemInfo.deviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceName.html)
  * [SystemInfo.deviceModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceModel.html)
  * [SystemInfo.operatingSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystem.html)


## Anti-piracy check
A common way of hacking an application is by removing the AppStore DRM protection and then redistributing it for free. Use Unity’s anti-piracy check to find out if your application was altered after it was submitted to the AppStore.
Check if your application is genuine (not hacked) with the [Application.genuine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuine.html) property. If the property returns `false`, you can warn users they are using a hacked app, or you can disable certain functions.
**Note:** Use [Application.genuineCheckAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuineCheckAvailable.html) along with `Application.genuine` to verify application integrity. Because accessing the [Application.genuine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuine.html) property is a resource-intensive operation, you shouldn’t perform it during frame updates or other time-critical code.
## Vibration support
You can trigger a vibration by calling [Handheld.Vibrate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.Vibrate.html). Devices without vibration hardware ignore this call.
## Activity indicator
Mobile operating systems have built-in activity indicators you can use during slow operations. See [Handheld.StartActivityIndicator docs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.StartActivityIndicator.html) for examples.
## Screen orientation
You can control the screen orientation of your application on both iOS and Android devices. By detecting a change in orientation or forcing a specific orientation, you can create app behaviors that depend on how the user holds the device. 
To retrieve device orientation, access the [Screen.orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html) property. Orientation can be one of the following:
**Orientation** | **Behavior**  
---|---  
**Portrait** | The device is in portrait mode, with the device held upright and the home button at the bottom.  
**PortraitUpsideDown** | The device is in portrait mode but upside down, with the device held upright and the home button at the top.  
**LandscapeLeft** | The device is in landscape mode, with the device held upright and the home button on the right side.  
**LandscapeRight** | The device is in landscape mode, with the device held upright and the home button on the left side.  
Set [Screen.orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html) to one of the above orientations or use [ScreenOrientation.AutoRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.AutoRotation.html) to control the screen orientation. When you enable autorotation, you can still disable some orientations on a case-by-case basis. 
For more information, refer to the following API documentation:
  * [Screen.autorotateToPortrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortrait.html)
  * [Screen.autorotateToPortraitUpsideDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortraitUpsideDown.html)
  * [Screen.autorotateToLandscapeLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeLeft.html)
  * [Screen.autorotateToLandscapeRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeRight.html)


The screen orientation of your application may vary depending on the device orientation set by the user, regardless of your application’s default orientation setting.
The following table shows the default screen orientation set for your application and the actual orientation the application loads in based on the device orientation.
| **Default screen orientation: Autorotate** | **Default screen orientation: Portrait** | **Default screen orientation: Landscape**  
---|---|---|---  
**Device orientation: Autorotate** | The application screen loads in portrait and can rotate between portrait, landscape right, and landscape left orientations (excluding portrait upside down orientation).  
**Note** : On an iPad, the application screen loads in portrait or landscape orientation based on the device orientation. The screen can rotate between portrait, portrait upside down, landscape right, and landscape left orientations. | The application screen loads and remains locked in portrait orientation. Although portrait upside down orientation is allowed, the screen doesn’t rotate to that orientation.  
**Note** : On an iPad, the application screen loads in portrait and can rotate between portrait and portrait upside down orientations. The splash screen can load in landscape orientation if the device orientation is landscape on launch. | The splash screen loads in the same orientation as the device orientation. The application screen loads in landscape when the scene loads and can rotate between landscape left or landscape right orientations.   
**Note** : On an iPad, the application screen loads in landscape, and can rotate between landscape left and landscape right orientations. The splash screen can load in portrait if the device orientation is portrait on launch.  
**Device orientation: Portrait lock** | The application screen loads and remains locked in portrait orientation.   
**Note** : Whilst in portrait orientation, if you set the [ScreenOrientation.AutoRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.AutoRotation.html) property for portrait to false, the application screen rotates to landscape orientation. If you now set the [ScreenOrientation.AutoRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.AutoRotation.html) property for landscape to false, the screen orientation remains unchanged. | The application screen loads and remains locked in portrait orientation. | The splash screen loads in portrait orientation, but the application screen loads in landscape when the scene loads. By default, the application screen remains locked in landscape left orientation.   
**Note** : On an iPad, the splash screen loads in portrait orientation and the scene loads in landscape orientation. The application screen remains locked in landscape orientation.  
**Device orientation: Landscape lock** | Not applicable as iPhones don’t have landscape lock setting. If the user turns off the device autorotation setting whilst the application is in landscape, the application screen rotates to and remains locked in portrait orientation.   
**Note** : On an iPad, the application loads and remains locked in landscape orientation. | Not applicable as iPhones don’t have landscape lock setting. The application remains locked in portrait orientation.   
**Note** : On an iPad, the splash screen loads in landscape and the scene loads in portrait orientation. The application screen remains locked in portrait orientation. | Not applicable as iPhones don’t have landscape lock setting. The application screen loads in landscape and can remain locked in both landscape left or landscape right orientations when the application loads.  
**Note** : On an iPad, the application screen loads in landscape and remains locked in either landscape left or landscape right orientation depending on the device orientation.  
## Determining device generation
Different device generations have varied performance and support different functionalities. Use the [iOS.DeviceGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration.html) property to query the device’s generation.
## Display cutout
On some displays, certain areas of the screen might be obscured or non-functional because of other hardware occupying that space. Use [Screen.cutouts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-cutouts.html) to return a list of bounding boxes surrounding each cutout.
iOS devices don’t provide a native API to get the display cutout information, so the cutouts are hardcoded in the Xcode project for each available iOS device. You can modify existing data or add additional devices in the Unity Xcode project `ReportSafeAreaChangeForView` function, which is in the `UnityView.mm` file.
## Recording a replay of your game
You can use [ReplayKit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.ReplayKit.ReplayKit.html) to record the audio and video of your game, along with audio and video commentary captured from the device’s microphone and **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
Developing for iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-input.html)
Input for iOS devices
