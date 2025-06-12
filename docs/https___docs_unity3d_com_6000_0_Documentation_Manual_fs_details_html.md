* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/fs-details.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [The Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html)
  * Details panel reference (feature sets)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html)
Details panel reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-find.html)
Find packages and feature sets
# Details panel reference (feature sets)
In the Package Manager window, when you select a [feature set](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset) from the list panel, the details panel on the right displays details for the selected feature set. The details panel presents the contents of the feature set as a kind of miniature Package Manager window:
![For a feature set, the details panel shows a brief description, a link to the QuickStart guide, and a list of included packages](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/fs-details.png) For a feature set, the details panel shows a brief description, a link to the QuickStart guide, and a list of included packages
**(A)** When you select a feature set from the [list panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html), its information appears in the details panel.
**(B)** The display name of the feature set. 
**(C)** The name of the feature set.
**(D)** A button to **Install** or **Remove** the feature set.
**(E)** A link to the **QuickStart** guide for this feature set, containing details of how you can use this set of packages together.
**(F)** Feature set details tabs:
  * **Description** : A brief overview of the feature set.
  * **Packages Included** : This tab displays the following information: 
    1. The list of included packages.
    2. The details of the selected package. The information shown includes the display name of the package, the recommended or installed version for the feature set, and its description.
    3. A shortcut to load the selected package in the Package Manager window. Selecting this shortcut replaces the feature set in the list panel and details panel. When you access details from the package directly, the Package Manager window provides more information than when you access them from inside the feature set. For example, the package details view shows dependency information and any samples the package has.


## Package version overrides
Feature sets are collections of packages that work well together for a specific version of Unity, which means the Package Manager installs specific package versions that your feature set requires. However, there are a couple of reasons why the Package Manager might actually install a different version (override the requested version):
  * Another package or feature set requires a different version of the same package and the [Package Manager resolved](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts.html) the package version by overriding it.
  * You requested a different package version and it didn’t conflict with the version that the feature set requires. In this case, a **Reset** button displays, which you can click to return to the version that the feature set requires (recommended). 
    * **Note** : The **Reset** button displays only when the major or minor number in the package version changes. The **Reset** button doesn’t display when the patch number in the package version changes. For more information on semantic version schemes, refer to [Versioning](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html).


If the Package Manager installs a version other than the one you requested, an information message explains the reason for the change.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html)
Details panel reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-find.html)
Find packages and feature sets
