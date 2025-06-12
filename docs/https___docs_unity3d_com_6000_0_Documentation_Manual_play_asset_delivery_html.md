* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application size restrictions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-size-restrictions.html)
  * Play Asset Delivery


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-host.html)
Host APK expansion files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)
Asset packs in Unity
# Play Asset Delivery
Play Asset Delivery (PAD) is the asset splitting solution for the [Android App Bundle](https://developer.android.com/guide/app-bundle) (AAB) publishing format. PAD uses asset packs to store additional assets such as textures, sounds, and meshes. Google hosts and serves asset packs on Google Play, which means you don’t need to create a content delivery network to send application resources to users. For more information about PAD, refer to Android documentation on [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery).
PAD is only available for Google Play and enables applications to be larger than the Google Play application size limit of 200MB.
**Important** : If you have a large application and want to publish it to [digital distribution services](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution.html) that don’t support the AAB publishing format, you must use the **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK) publishing format and [APK expansion files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-OBBsupport.html).
**Topic** | **Description**  
---|---  
[Asset packs in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html) | Learn how asset packs work in Unity.  
[Set up Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-set-up.html) | Configure your Unity project to produce an AAB that contains asset packs.  
[Create a custom asset pack](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html) | Create a custom asset pack to store additional assets for an application.  
[Manage asset packs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html) | Download and access asset packs at runtime.  
**Notes:**
  * All versions of Unity from 2021.3 support Play Asset Delivery.
  * Unity doesn’t support [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery).


## Additional resources
  * [Android application publishing format](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html#publishing-format)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-host.html)
Host APK expansion files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)
Asset packs in Unity
