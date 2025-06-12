* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-Downloadable-Content.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * Prepare your application for in-app purchases


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-authorizations-in-unity.html)
iOS authorizations in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/net-SocialAPI.html)
Social API
# Prepare your application for in-app purchases
In-app purchases (IAP) allow you to offer additional downloadable content in your application, such as new levels or character cosmetics. You must integrate with the StoreKit API within your application using a [native code plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html) before you can set up in-app purchases. For more information, refer to [StoreKit](https://developer.apple.com/documentation/storekit) (Apple).
**Note** : The [Unity IAP package](https://docs.unity3d.com/Packages/com.unity.purchasing@latest) can be used to implement in-app purchases for iOS and other platforms you might want to develop for.
## Organize your assets
The [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/) package provides a ready-made system to manage and organize [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html) in your project. It’s recommended to use the Addressables package rather than manage AssetBundles yourself.
## Download your assets
If you are managing AssetBundles yourself, it’s recommended to use [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html) to access any remote assets. If using the [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/) package, this will handle asset downloads for you. 
**Note** : Apple might change the folder locations where you’re permitted to write data. Make sure to check the latest Apple guidelines for the most up-to-date information.
## Additional resources
  * [StoreKit](https://developer.apple.com/documentation/storekit) (Apple)
  * [Unity IAP package](https://docs.unity3d.com/Packages/com.unity.purchasing@4.11/manual/Overview.html)
  * [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/)
  * [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-authorizations-in-unity.html)
iOS authorizations in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/net-SocialAPI.html)
Social API
