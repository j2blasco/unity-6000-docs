* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-set-up.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application size restrictions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-size-restrictions.html)
  * [Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html)
  * Set up Play Asset Delivery


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)
Asset packs in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html)
Create a custom asset pack
# Set up Play Asset Delivery
[Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html) is the asset splitting solution for [Android App Bundles](https://developer.android.com/guide/app-bundle) (AAB). To use Play Asset Delivery, set up your project to:
  1. Use the AAB publishing format. For information on how to do this, refer to [Publishing format](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html#publishing-format).
  2. Split the application binary. For information on how to do this, refer to [Splitting the application binary](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-distribution-size.html#splitting-the-application-binary). If **Split Application Binary** is grayed out, it means your current Unity Editor version doesn’t support Play Asset Delivery. To resolve this, update the Unity Editor.


When you build your application, Unity creates an AAB that includes your application split into a [base module](https://developer.android.com/guide/app-bundle/configure-base) and asset packs. For more information, refer to [Asset packs in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html).
**Important** : Unity uses `PLAY_ASSET_PACKS` [Gradle template variable](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-template-variables.html) to specify which asset packs to include in the Android App Bundle. When you build a Unity project with Play Asset Delivery support, Unity automatically generates values for this variable. If you’re upgrading from a Unity version without Play Asset Delivery support and using a custom **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) template, it’s recommended to recreate the template file and reapply the modifications. Otherwise, your project build will not include the asset packs.
## Additional resources
  * [Asset packs in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)
  * [Create a custom asset pack](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html)
  * [Manage asset packs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)
Asset packs in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html)
Create a custom asset pack
