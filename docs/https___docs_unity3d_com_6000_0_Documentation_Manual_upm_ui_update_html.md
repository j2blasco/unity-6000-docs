* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Package management with the Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-packages-window.html)
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)
  * Switch to another version of a UPM package


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html)
Install a UPM package by name
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html)
Remove a UPM package from a project
# Switch to another version of a UPM package
Use the information on this page to update **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) that you installed from the [Unity Registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install.html) or a [scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html), or from a [local source](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-local.html). The information on this page also applies to packages you [installed from the Asset Store](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install2.html), if they’re in the UPM format.
If you want to install a specific version of a package, refer to [install the package by name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html) and follow its optional step to specify a version.
If you want to update packages that you installed from a Git URL, you can use any of the following methods:
  * Locate the package in the **Package Manager** window, select it, then click the **Update** button.
  * [Reinstall the package as a Git dependency](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-giturl.html) using a new revision. For more information about how to specify revisions with **Git dependencies** The Package Manager retrieves Git dependencies from a Git repository directly rather than from a package registry. Git dependencies use a Git URL reference instead of a version, and there’s no guarantee about the package quality, stability, validity, or even whether the version stated in its `package.json` file respects Semantic Versioning rules with regards to officially published releases of this package. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Git)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gitdependency), refer to [Targeting a specific revision](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html#revision).
  * Reinstall the package from the Unity Registry.


To update a package:
  1. Open the **Package Manager** window and select **In Project** , **Unity Registry** , or **My Registries** from the [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html). You can also select the **Updates** entry, which lists all packages in your project that have updates available. An arrow icon appears next to packages that have updates available.
  2. Select the installed package you want to update from the [list of packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html). The package information appears in the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html). 
  3. The lock icon indicates that this package and version is locked to an installed **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset). To unlock the package and select another version, click the **Unlock** button.
**Note** : The package is temporarily unlocked. If you select a different context in the [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html), or close either the **Package Manager** window or the Unity Editor, the package reverts to a locked state. However, if you change versions when the package is unlocked (for example, with the [Install a package from a registry by name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html) method), the package stays unlocked.
  4. Select a package in the [list of packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html).
  5. In the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html), select the **Version History** tab. If multiple versions are available, expand the entries to view information specific to each version.
  6. Click the **Update to #.#** button, or click the **Update** button beside the version listed in the **Version History** tab.
When the progress bar finishes, any new functionality is immediately available.


**Notes:**
  * If you switch to an older version of a package, you might have to run the [API Updater](https://docs.unity3d.com/6000.0/Documentation/Manual/APIUpdater.html) on the package contents.
  * You can switch versions for multiple packages with one click by using the multiple select feature. For more information, refer to [Perform an action on multiple packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-multi.html).


## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html)
Install a UPM package by name
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html)
Remove a UPM package from a project
