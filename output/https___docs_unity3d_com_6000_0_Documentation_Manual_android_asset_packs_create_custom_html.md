* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application size restrictions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-size-restrictions.html)
  * [Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html)
  * Create a custom asset pack


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-set-up.html)
Set up Play Asset Delivery
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html)
Manage asset packs at runtime
# Create a custom asset pack
To create a custom asset pack, create a directory with a name that ends with `.androidpack`. You can place this directory anywhere in your project’s Assets directory, or any subdirectory.
**Important** : Unity doesn’t import assets from `.androidpack` directories, so you can’t use assets in custom asset packs directly in Unity **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). To use assets from custom asset packs, you must manually access and load them dynamically at runtime. For information on how to do this, refer to [Manage asset packs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html).
The following steps explain how to create a custom asset pack named **MyAssets1** :
  1. Go to the directory you want to create the asset pack in. This can be directly in **Assets** or a subdirectory like **Assets/CustomAssetPacks**.
  2. Create a new directory and call it `MyAssets1.androidpack`. This is the root folder of your new asset pack. The contents of the asset pack must match the structure that Android Studio expects or builds of your project will fail. For information on the expected structure, refer to [Integrate asset delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-java). The only exception is that you don’t need to add a `build.gradle` file.  
**Note** : Asset pack names must begin with a letter and consist of English alphanumeric characters or an underscore. If you’re creating more than one custom asset pack, make sure you choose a unique name for each asset pack. Asset pack names that are similar, such as `Assets1.androidpack` and `MyAssets1.androidpack`, cause Android App Bundle (AAB) build failure.
  3. To add assets to the asset pack, place them at the following folder path within the asset pack: `src/main/assets`.
  4. By default, the delivery mode is `on-demand`, which means that if you don’t change the delivery mode, you need to manually download the asset pack at runtime. For information on how to do this, refer to [Manage asset packs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html).
  5. To use a different delivery mode, create a file called `build.gradle` inside the custom asset pack directory. Paste the following into the file:

```
apply plugin: 'com.android.asset-pack'
assetPack {
    packName = "MyAssets1"
    dynamicDelivery {
        deliveryType = "fast-follow"
    }
}

```

This sets the delivery mode to `fast-follow`, which means Google Play automatically downloads the asset pack after it installs the application. For information on the format of this file, refer to [Integrate asset delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
**Note** : The `packName` you specify in the `build.gradle` file must match the asset pack directory name you set without the `.androidpack` extension.
## Additional resources
  * [Asset packs in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)
  * [Manage asset packs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-set-up.html)
Set up Play Asset Delivery
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html)
Manage asset packs at runtime
