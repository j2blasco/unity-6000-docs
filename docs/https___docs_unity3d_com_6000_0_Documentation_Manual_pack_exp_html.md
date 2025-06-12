* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/pack-exp.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages-all.html)
  * Experimental packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.modules.xr.html)
XR 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-keys.html)
Packages by keywords 
# Experimental packages
Experimental packages are new packages or experimental modifications made to mature packages. Unity doesn’t support Experimental packages because they’re in the early stages of development.
**Note:** Before Unity Editor version 2021.1, the Package Manager used the “Preview” state to describe packages that are experimental or risky but otherwise mature. The Package Manager used the “Preview” state to describe packages that had not yet been fully validated as safe to use in production. Starting with 2021.1, the “Preview” state no longer exists, and packages can either be “Experimental” or “Pre-release.” This provides a clearer distinction between packages that are mature but risky to use, and packages that are almost fully mature. 
Experimental packages can go through many changes before they’re ready for release in a specific version of Unity. At some point in the future, they might pass [the verification requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-safe.html) but they might also become deprecated instead. Because there is no guarantee for future support, you shouldn’t use experimental packages in production.
Packages in experimental state don’t usually appear in the [Unity Registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html#contexts) context of the Package Manager, even though they’re on Unity’s official package registry server. These packages aren’t discoverable in the Package Manager window because:
  * They’re too risky to use in production. Some of these packages require a lot of training and expertise and are recommended only in specific circumstances.
  * They provide shared or additional functionality to existing packages. You shouldn’t use them on their own because they’re “support” packages only.


Experimental packages that aren’t discoverable can still appear in the Package Manager window if you already installed them in your project or installed them as dependencies of supported packages. However, they’re hidden so that you don’t discover them by accident and use them without realizing the risks. If they do appear in the Editor, they’re always marked in the Package Manager window with the ![Experimental](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconExperimental.png) label (details view) and the ![Exp](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconExp.png) label (list view). Also, the following menu appears as a warning in the Editor:
![The Experimental Packages In Use menu appears as a warning in the toolbar](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-lifecycle.png) The **Experimental Packages In Use** menu appears as a warning in the toolbar
You can open the **Experimental Packages In Use** menu and select **Dismiss** if you don’t want to see this warning for this project. You can also open the menu and select **Show Experimental Packages** to open the Package Manager with a filtered list of the experimental packages in your project.
For a list of stable packages verified for this release, see [Released packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-safe.html).
For more information about package states, see [Package states and lifecycle](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-lifecycle.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.modules.xr.html)
XR 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-keys.html)
Packages by keywords 
