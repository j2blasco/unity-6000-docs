* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * The Package Manager window


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-localpath.html)
Local folder or tarball paths
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-access.html)
Access the Package Manager window
# The Package Manager window
Access the Package Manager window from the Unity Editor’s **Window** menu.
Use the Package Manager window to:
  * View which [packages and feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html) are available for installation or already installed in your project.
  * Check [which package versions are available](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-find-ver.html).
  * Install, update, or remove [UPM packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) or [feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/fs-install.html)A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset).
  * Download and import, update, or remove [asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions-ap.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage).
  * [Disable built-in packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-disable.html).

![The Package Manager window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui.png) The Package Manager window
The Package Manager window displays:
**(A)** The experimental package indicator, which warns you if your project has [experimental packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-exp.html).
**(B)** The **install** ![The install button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconAdd.png) button, which you can click to [install a package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html) directly into your project by entering a git URL, a local path, or a package name.
**(C)** The [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html), which you can use to select a context to change what appears in the list panel **(H)**.
**(D)** The [Sort](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-sort.html) menu, which you can use to sort the list of packages and feature sets by name or date.
**(E)** The [Filter](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-filter2.html) menu, which you can use to narrow down which packages appear in the list panel **(H)**. The **Filters** menu and the **Clear Filters** button are disabled for the **Built-in** list. They’re also disabled for the **In Project** context (unless you have subscription-based packages), because that context in the navigation panel has a nested item for **Updates**.
![The Filters menu and the Clear Filters button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-asset-filters.png) The **Filters** menu and the **Clear Filters** button
**(F)** The [search box](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-search.html), which you can use to look for packages and feature sets by name.
**(G)** The **Advanced** menu ![The Advanced menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconSettings.png), which you can use to access the **project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) for the Package Manager, preferences, and more. Refer to [Advanced settings](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html#Advanced) for details.
**(H)** The [list panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html), which displays packages for the type you selected in the navigation panel, limited by any filter and search parameters you specified.
**(I)** The details panel, which displays information specific to the [package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html)A container that stores various types of features and assets for Unity, including Editor or Runtime tools and libraries, Asset collections, and project templates. Packages are self-contained units that the Unity Package Manager can share across Unity projects. Most of the time these are called _packages_ , but occasionally they are called **Unity Package Manager (UPM) packages**. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Package) or [feature set](https://docs.unity3d.com/6000.0/Documentation/Manual/fs-details.html) selected in the list panel.
**(J)** The package details tabs, which display further information about the selected package or feature set. The tabs are dynamic, based on the selected item. For information about these tabs, refer to [Details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html).
**(K)** Buttons to perform any of the following actions at the project level:
  * [Install or remove feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/fs-install.html)
  * [Install](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install.html), [update](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update.html), or [remove](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html) UPM packages
  * [Download and import](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html), [update](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update2.html), or [remove](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-asset.html) asset packages
  * [Disable or enable](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-disable.html) built-in packages
  * Install or remove [services](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityServices.html)A Unity facility that provides a growing range of complimentary services to help you make games and engage, retain and monetize audiences. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityServices.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Services)


**(L)** The [status bar](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html#StatusBar), which displays information when the Package Manager loads packages and feature sets. This information includes errors and warning messages, the number of **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) packages available, and a link to load more packages from the Asset Store.
**(M)** The **Refresh list** ![The Refresh list button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconReload.png) button lets you refresh the list of packages displayed. In the **My Assets** context, **Refresh list** is a menu, which has a **Check for updates** option. You can use **Check for updates** to check for updates to all packages on your computer, not just the ones that are visible in the **My Assets** context.
## Advanced settings
The advanced settings ![The advanced settings menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconSettings.png) menu allows you to perform these actions:
**Menu item** | **Action results**  
---|---  
**Project Settings** | Select this item to open the [Package Manager project settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html), where you can:  
  
- List [pre-release packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-preview.html) when browsing the Unity Registry.  
- Add, edit, and remove [scoped registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html) in your project.  
**Preferences** | Select this item to view and set [Preferences](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html) for the Unity Editor and related windows and tools.  
**Manual resolve** | Select this item to force the Package Manager to resolve the project’s packages. If needed, it re-installs altered or missing packages and removes extraneous packages.  
## Status bar
The Package Manager displays messages in the status bar at the bottom of the Package Manager window.
There are typically four status messages that the Package Manager might display:
  * The first time you open the Package Manager window in a new project, the **Refreshing list** message appears briefly:
![Message for refreshing packages and features](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-loading.png) Message for refreshing packages and features
This message also appears when you click **Refresh list** ![The Refresh list button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconReload.png)
  * When you select the **My Assets** context in the navigation panel, the load bar appears above the date. It displays the number of packages from the Asset Store. Select **Load** to load more packages.
![On the left, the load bar displays the number of My Assets packages loaded and the total number available.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-assets-loadbar.png) On the left, the load bar displays the number of **My Assets** packages loaded and the total number available.
  * Most of the time, the status bar displays the date and time of when the Package Manager window last refreshed its information. However, if the Package Manager [detects a problem](https://docs.unity3d.com/Manual/upm-errors.html), such as a network issue, the Package Manager prompts you to sign in:
![Network error message](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-errors.png) Network error message
  * If your network connection is working, but you aren’t signed into your [Unity account](https://id.unity.com/), the Package Manager doesn’t display any packages from the Asset Store. When you select **My Assets** in the navigation panel, the Package Manager prompts you to sign in:
![Logged out of Unity account](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-unityid.png) Logged out of Unity account
In the list panel, click **Sign in** to sign in to your Unity account through the [Unity Hub](https://docs.unity3d.com/hub/manual/index.html).


For information on how to resolve these errors and more, refer to [Package Manager troubleshooting](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html).   

## Additional resources
  * [Get started with packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Finding package documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-docs.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-localpath.html)
Local folder or tarball paths
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-access.html)
Access the Package Manager window
