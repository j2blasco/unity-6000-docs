* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [The Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html)
  * Navigation panel reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-access.html)
Access the Package Manager window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html)
List panel reference
# Navigation panel reference
Use the Package Manager’s navigation panel to select which subset of packages you want to view.
![The navigation panel \(A\), the list panel \(B\), and the details panel \(C\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-nav.png) The navigation panel **(A)** , the list panel **(B)** , and the details panel **(C)**
Select a context from the navigation panel **(A)** to list those types of packages in the list panel **(B)**. When you select a package from the list panel, its details display in the details view **(C)**.
## Context list
Select the context you want from the navigation panel. You can select from these options:
**Context** | **Description**  
---|---  
**In Project** | Displays all feature sets and packages installed in your project, including [local](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-localpath.html), [git](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html), and [embedded](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html) packages, and packages installed from any registry. The list also includes any packages from the Asset Store that you added from the **My Assets** context.   
**In Project** has a nested entry, **Updates** , which lists all packages in your project that you can update, including Asset Store packages.  
**Unity Registry** | Displays all **feature sets** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset) and packages on the [Unity package registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Registry), regardless of whether they’re already installed in your project. This doesn’t include packages installed from any other location or from any [scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html).  
**My Assets** | Displays all [Asset Store packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePackages.html) that you have purchased using the Unity ID you’re currently logged in with.  
**Built-in** | Displays only built-in Unity packages, which represent core Unity features. You can use these packages to [turn Unity modules on and off](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-disable.html).  
  
**Tip** : You can find out more about what each built-in package (module) implements in the [Unity Scripting API](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-api.html). Each module assembly page lists which APIs the built-in package implements.  
**Services** A Unity facility that provides a growing range of complimentary services to help you make games and engage, retain and monetize audiences. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityServices.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Services) | Displays integrated [services](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityServices.html) to help you to engage, retain, and monetize audiences.  
**My Registries** | Displays any packages available from any [scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html) installed in this project.  
  
This context appears only if you installed a scoped registry in this project.  
  
If you installed a scoped registry but it’s not listed in the **My Registries** context or the **My Registries** context isn’t available at all, it might be because the package registry server you added doesn’t implement either of the `/-/v1/search` or `/-/all` endpoints, which means that it’s not compatible with Unity’s Package Manager.  
**Note** : If you entered text in the [search box](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-search.html) or set [filters](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-filter2.html), the list panel displays only feature sets and packages which match the context, search criteria, and active filters.
## Additional information
  * [List panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html)
  * [Details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-access.html)
Access the Package Manager window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html)
List panel reference
