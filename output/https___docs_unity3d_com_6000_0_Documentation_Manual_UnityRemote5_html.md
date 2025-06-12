* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * Unity Remote


[](https://docs.unity3d.com/6000.0/Documentation/Manual/mobile-accessibility.html)
Accessibility for mobile applications
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
Android
# Unity Remote
Unity Remote is a downloadable application that you can use for Android, iOS, and tvOS development. **Unity Remote** connects your target device to the Unity Editor and displays the visual output from the Editor on the target device’s screen at a reduced frame rate. It also sends live inputs from the target device back to the running project in Unity. Use Unity Remote to understand how an application looks and performs on the target device without creating a build.
The target device streams the following input data back to the Unity Editor:
  * Touch and stylus input
  * Accelerometer
  * Gyroscope
  * Device **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) streams
  * Compass
  * GPS
  * Joystick names and input


The Unity Editor still performs the application’s actual processing on the desktop computer. This means the performance of the application isn’t an accurate reflection of how the built application will perform on the target device. For an exact assessment of the application’s performance, build the application and test the build on the target device.
If you use [platform-specific conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html), ensure you have an active [build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) that matches the target device platform running Unity Remote on.
## Requirements and compatibility
Unity Remote supports Android, iOS, and tvOS devices. To use Unity Remote on an Android device, the Android SDK must be installed on your development computer. For more information, refer to [Android environment setup](https://docs.unity3d.com/6000.0/Documentation/Manual/android-sdksetup.html).
**Note** : Unity Remote replaces the iOS Remote and Android Remote applications from earlier versions of Unity. Unity no longer supports these older applications.
## Set up Unity Remote
To set up Unity Remote, follow these steps:
  1. [Install Unity Remote on the target device](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html#install-unity-remote)
  2. [Connect the target device to your development computer](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html#connect-device-computer)
  3. [Connect the Unity Editor to Unity Remote](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html#connect-editor-unity-remote)


### 1. Install Unity Remote
Download and install the Unity Remote application on the target device using the following links.
  * **Android** : [Google Play](https://play.google.com/store/apps/details?id=com.unity3d.mobileremote)
  * **iOS** : [App Store](https://apps.apple.com/gb/app/unity-remote-5/id871767552).


### 2. Connect the target device to your development computer
To connect your target device and the development computer, follow these steps:
  1. Run Unity Remote on the target device.
  2. Connect the target device to your computer via USB. 
     * For Android devices, make sure to enable USB debugging. For information on how to do this, refer to [Debug on Android devices](https://docs.unity3d.com/6000.0/Documentation/Manual/android-debugging-on-an-android-device.html).
     * For iOS or tvOS devices, if using a Windows computer, make sure to install [iTunes](https://support.apple.com/en-gb/118290).


### 3. Connect the Unity Editor to Unity Remote
Once the target device is connected to your computer, the Unity Editor should be able to detect it. To connect Unity Remote on the target device to the Unity Editor:
  1. Open the [Editor settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html) (menu: **Edit** > **Project Settings** > **Editor**).
  2. In the **Unity Remote** section, set **Device** to the target device you want to use.


If the **Device** list doesn’t include the target device, first disconnect and reconnect the target device. If that doesn’t work, make sure that the USB connection is set up correctly. To test this, you can build and run your application to check whether Unity is able to install it on the target device. For information on how to build for Android, refer to [Build your application for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html) and for iOS, refer to [Build an iOS application](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-BuildProcess.html).
**Important** : Unity doesn’t support Unity Remote on multiple connected Android devices. To resolve this, Unity automatically picks the first Android device it finds. You can have multiple iOS/tvOS devices and one Android device connected at the same time. All these connected devices appear in the **Device** list.
## Preview an application in Unity Remote
In the Unity Editor, click the Play button to run the application on the target device and in the Game view. As the application runs, Unity Remote streams input back to the Editor and your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) handle the inputs as if the scripts were running on the target device itself.
## Performance
When you use Unity Remote, the application actually runs in the Editor, and Unity streams the visual content to the target device. The bandwidth between the Editor and the device is limited so Unity compresses the stream for transmission. The default **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) method is JPEG which is a lossy compression method that reduces the image quality. 
### Change the compression method
You can improve image quality on the Unity Remote application by changing the compression method to PNG. PNG is a lossless compression method that uses more bandwidth but doesn’t reduce the image quality. To change the compression method to PNG, use the following steps:
  1. Open the [Editor settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html) (menu: **Edit** > **Project Settings** > **Editor**).
  2. In the **Unity Remote** section, set **Compression** to **PNG**.


### Change the resolution
By default, when Unity streams the application to Unity Remote, it downsizes the application’s resolution. This reduction in image quality creates a lower bandwidth requirement and produces better runtime performance. To preview your application at the application’s full resolution, follow these steps:
  1. Open the [Editor settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html) (menu: **Edit** > **Project Settings** > **Editor**).
  2. In the **Unity Remote** section, set **Resolution** to **Normal**.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/mobile-accessibility.html)
Accessibility for mobile applications
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
Android
