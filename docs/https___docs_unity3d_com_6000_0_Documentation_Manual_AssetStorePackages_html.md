* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePackages.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Unity's Asset Store](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)
  * Asset Store packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)
Unity's Asset Store
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesPurchase.html)
Purchase or download a package from the Asset Store
# Asset Store packages
Asset Store packages are collections of files and data from Unity projects, or elements of projects. An **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) package type is either a **UPM package** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) or an **asset package** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) (`.unitypackage` format). When you add an Asset Store package to your project, the Unity Package Manager unpacks the package and maintains its directory structure and metadata about assets. This metadata includes information such as import settings and links to other assets.
To get an Asset Store package from Unity or a third-party publisher, start by [searching the Unity Asset Store](https://assetstore.unity.com/) to find assets that meet your needs. When you find an Asset Store package you want to use, [buy or download](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesPurchase.html) it in the Asset Store. You can also make it easier to locate packages you get from the Asset Store by [organizing your assets with labels](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesLabels.html) and hiding deprecated or unused packages. Refer to [hiding Asset Store packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesOrganize.html).
In the Unity Package Manager, select the [My Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html#contexts) context to view your [list of available Asset Store packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html). You can [search by name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-search.html) for Asset Store packages. When you find the Asset Store package you want to use, you can add it to your project by using the Package Manager window. For asset packages, refer to [Download and import an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html). For UPM packages, refer to [Install a UPM package from Asset Store](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install2.html). If your Asset Store package has a newer version available, you can also update it directly in the Package Manager window. To update an asset package, refer to [Updating an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update2.html). To update a UPM package, refer to [Switch to another version of a UPM package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update.html).
Unity users can become publishers on the Asset Store, and sell the content they have created. Follow the instructions in [Publishing to the Asset Store ](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePublishing.html) for [creating a package draft](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreCreatePkg.html) and [uploading your assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreUpload.html) for publication on the [Unity Asset Store](https://assetstore.unity.com/).
## Location of downloaded asset package files
**Note** : This information applies only to asset packages you get from the Asset Store. It doesn’t apply to UPM packages you get from the Asset Store.
You can use the Package Manager window to manage your Asset Store packages within your project. However, if you need to access files from an asset package directly, you can find them in the cache for asset packages. This cache, which is separate from the [global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html), makes reusing and sharing asset packages more efficient. You can find the cache for asset packages in the following paths (which might be within hidden folders depending on your computer settings):
  * macOS: `~/Library/Unity/Asset Store-5.x`
  * Windows: `C:\Users\accountName\AppData\Roaming\Unity\Asset Store-5.x`
  * Linux: `~/.local/share/unity3d/Asset Store-5.x`


These folders contain subfolders that correspond to particular Asset Store vendors and are available after download and import. The Package Manager stores asset files inside the subfolders using a structure defined by the Asset Store package publisher.
You can override the default location of the cache for asset packages. For information, refer to [Customize the asset package cache location](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-cache-as.html).
## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)
Unity's Asset Store
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesPurchase.html)
Purchase or download a package from the Asset Store
