* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html

# Android
class in UnityEditor
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
### Description
Android specific Player settings.
Use these settings to configure how Unity builds and displays your final application for the Android platform.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AndroidPlayerSettingsSamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)/Set Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html) Player settings")]
    public static void SetAndroidPlayerSettings()
    {
        // Set autoRotation behaviour value to user or sensor
        PlayerSettings.Android.autoRotationBehavior[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-autoRotationBehavior.html) = AndroidAutoRotationBehavior.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.User.html);
        // Log the current value of autoRotationBehavior
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"autoRotationBehavior: {PlayerSettings.Android.autoRotationBehavior[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-autoRotationBehavior.html)}");
        
        // Set min aspect ratio to 2.0f
        PlayerSettings.Android.minAspectRatio[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minAspectRatio.html) = 2.0f;
        // Log the minimum aspect ratio
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"minAspectRatio: {PlayerSettings.Android.minAspectRatio[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minAspectRatio.html)}");
        
        // Set minimum SDK version
        PlayerSettings.Android.minSdkVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minSdkVersion.html) = AndroidSdkVersions.AndroidApiLevel30[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidSdkVersions.AndroidApiLevel30.html);
        // Log the minimum SDK version
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"minSdkVersion: {PlayerSettings.Android.minSdkVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minSdkVersion.html)}");
        
        // Set targetSdkversion
        PlayerSettings.Android.targetSdkVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetSdkVersion.html) = AndroidSdkVersions.AndroidApiLevel30[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidSdkVersions.AndroidApiLevel30.html);
        // Log the targetSdkVersion setting
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"targetSdkVersion: {PlayerSettings.Android.targetSdkVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetSdkVersion.html)}");
        
        // Set textureCompressionFormats to ETC2 and ASTC texture formats
        PlayerSettings.Android.textureCompressionFormats[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-textureCompressionFormats.html) = new TextureCompressionFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionFormat.html)[]
        {
            TextureCompressionFormat.ETC2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionFormat.ETC2.html),
            TextureCompressionFormat.ASTC[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionFormat.ASTC.html)
        };
        // Log each configured texture compression format
        foreach (TextureCompressionFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionFormat.html) format in PlayerSettings.Android.textureCompressionFormats[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-textureCompressionFormats.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Configured Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Compression Format: {format}");
        }
    }
}

```

### Static Properties
Property | Description  
---|---  
[androidIsGame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-androidIsGame.html) | Publish the build as a game rather than a regular application.   
[androidTVCompatibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-androidTVCompatibility.html) | Provide a build that is Android TV compatible.  
[androidVulkanAllowFilterList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-androidVulkanAllowFilterList.html) | Specifies a list of AndroidDeviceFilterData parameters to allow Android devices to always use Vulkan API when running Unity applications.  
[androidVulkanDenyFilterList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-androidVulkanDenyFilterList.html) | Specifies a list of AndroidDeviceFilterData parameters to restrict Android devices from using Vulkan API when running Unity applications.  
[applicationEntry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-applicationEntry.html) | Application entry classes to include.Note: You can specify multiple application entries for development purposes, this will cause two application icons to appear on Android device. You should always specify a single entry when publishing your app to a store.  
[ARCoreEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.ARCoreEnabled.html) | Enable support for Google ARCore on supported devices.  
[autoRotationBehavior](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-autoRotationBehavior.html) | Indicate whether your application window rotates based on device orientation settings (User) or device orientation sensor (Sensor), when default orientation is Auto Rotation.  
[blitType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-blitType.html) | Choose how content is drawn to the screen.  
[buildApkPerCpuArchitecture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-buildApkPerCpuArchitecture.html) | Create a separate APK for each CPU architecture.  
[bundleVersionCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-bundleVersionCode.html) | Android bundle version code.  
[defaultWindowHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-defaultWindowHeight.html) | The default vertical size of the Android Player window in pixels.  
[defaultWindowWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-defaultWindowWidth.html) | The default horizontal size of the Android Player window in pixels.  
[disableDepthAndStencilBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-disableDepthAndStencilBuffers.html) | Disable Depth and Stencil Buffers.  
[enableArmv9SecurityFeatures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-enableArmv9SecurityFeatures.html) | Enable Armv9 security features, including Pointer Authentication (PAuth, PAC) and Branch Target Identification (BTI) for Arm64 builds.  
[forceInternetPermission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-forceInternetPermission.html) | Force internet permission flag.  
[forceSDCardPermission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-forceSDCardPermission.html) | Force SD card permission.  
[fullscreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-fullscreenMode.html) | The display mode for Android Player builds of your application.  
[keyaliasName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasName.html) | Android key alias name.  
[keyaliasPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasPass.html) | Password for the key used for signing an Android application.  
[keystoreName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystoreName.html) | Contains the path to the Android keystore file.  
[keystorePass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystorePass.html) | Android keystore password.  
[maxAspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-maxAspectRatio.html) | Maximum aspect ratio which is supported by the application.  
[minAspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minAspectRatio.html) | Minimum aspect ratio which is supported by the application.  
[minifyDebug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minifyDebug.html) | Enable to minify debug build.  
[minifyRelease](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minifyRelease.html) | Enable to minify release build.  
[minimumWindowHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minimumWindowHeight.html) | The minimum vertical size of the Android Player window in pixels.  
[minimumWindowWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minimumWindowWidth.html) | The minimum horizontal size of the Android Player window in pixels.  
[minSdkVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-minSdkVersion.html) | The minimum API level required for your application to run.  
[optimizedFramePacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-optimizedFramePacing.html) | Enable optimized frame pacing.  
[predictiveBackSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-predictiveBackSupport.html) | Enable to use Android's OnBackInvokedCallback for handling back events on Android 13 and above.  
[preferredInstallLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-preferredInstallLocation.html) | Preferred application install location.  
[renderOutsideSafeArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-renderOutsideSafeArea.html) | Extends rendering layout into display cutout area, utilizing all of the available screen space.  
[reportGooglePlayAppDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-reportGooglePlayAppDependencies.html) | Indicates whether to track application dependencies for Google Play Store verification.  
[resizeableActivity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-resizeableActivity.html) | Indicates whether your Android application is resizable.  
[runWithoutFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-runWithoutFocus.html) | Allows your application to continue to run even when it’s not in focus.  
[showActivityIndicatorOnLoading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-showActivityIndicatorOnLoading.html) | Application should show ActivityIndicator when loading.  
[splashScreenScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-splashScreenScale.html) | Android splash screen scale mode.  
[splitApplicationBinary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-splitApplicationBinary.html) | Split application binary into modules.  
[startInFullscreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-startInFullscreen.html) | Start in fullscreen mode.  
[targetArchitectures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetArchitectures.html) | A set of CPU architectures for the Android build target.  
[targetSdkVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetSdkVersion.html) | The target API level of your application.  
[textureCompressionFormats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-textureCompressionFormats.html) | Target texture compression formats.  
[useCustomKeystore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-useCustomKeystore.html) | Enable application signing with a custom keystore.  
* * *
