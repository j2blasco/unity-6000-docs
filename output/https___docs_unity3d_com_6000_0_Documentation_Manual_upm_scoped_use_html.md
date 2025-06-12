* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Scoped registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html)
  * Use a scoped registry in your project


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-start.html)
Get started with scoped registries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-scoped.html)
Scoped registry authentication
# Use a scoped registry in your project
Add a scoped registry to your project to access custom packages. 
## Integrity and security of scoped registries
Whenever you add a scoped registry to your project, use the same level of caution that you use when installing any other third-party software:
  * Install scoped registries only from trusted sources, because the packages in those registries can contain executable code.
  * Beware of third-party registries that might be harmful or capture data without appropriate controls. Also beware of third parties that falsely claim to be Unity or to have Unity’s approval or support.


## Manage scoped registries for a project
You can use the [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#manage-window)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) window or the [project manifest file](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#manage-manifest) to manage scoped registries in your project.
### Manage scoped registries with the Project Settings window
You can add, modify, and remove a scoped registry for your project in the [Package Manager panel](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html) within the **Project Settings** window. The **Scoped Registries** group displays a list of scoped registries added to the current project on the left of the settings group, and the details of the selected registry on the right.
#### Add a registry
To add a new scoped registry to your project by using the [Package Manager panel](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html) of the **Project Settings** window:
  1. Select the **Add (+)** button at the bottom of the list of scoped registries. A new entry appears in the list as **New Scoped Registry** with blank values for the details on the right.
  2. Enter values for the [Name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#name), [URL](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#url), and [Scope(s)](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#scopes) properties.
  3. If you want to specify more than one scope, select the **Add (+)** button underneath the last **Scope(s)** value to display another **Scope(s)** text field.
  4. After you enter the information for the selected scoped registry, select **Save**. To cancel adding the new scoped registry, select **Cancel**.


**Note** : You might experience one or more of the following issues when you add a scoped registry:
  * The **My Registries** [context](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html#contexts) doesn’t display in the navigation panel.
  * The scoped registry isn’t listed under the **My Registries** context.


These issues might occur because because the package registry server you added doesn’t implement the `/-/v1/search` or `/-/all` endpoints. Unity’s Package Manager requires these endpoints.
#### Modify a registry
To modify an existing scoped registry by using the [Package Manager panel](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html) of the **Project Settings** window:
  1. Select the registry you want to modify from the list on the left. The information for the existing scoped registry displays on the right.
  2. Modify any of the [Name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#name), [URL](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#url), and [Scope(s)](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#scopes) properties.
  3. After you update the information for the selected scoped registry, select **Apply**. To cancel your updates, select **Revert**.


#### Remove a registry
To delete an existing scoped registry by using the [Package Manager panel](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html) of the **Project Settings** window:
  1. Select the registry you want to delete from the list.
  2. Select the **Remove (-)** button underneath the list. A dialog prompts you to confirm the removal.
  3. Select **OK** to remove the registry or **Cancel** to leave it intact.


### Manage scoped registries with the project manifest file
The [project manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectmanifest) uses a [scopedRegistries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html#scopedRegistries) property, which contains an array of scoped registry configuration objects. Each object has the following properties:
**Property** | **JSON Type** | **Description**  
---|---|---  
**name** | String | The scope name as it appears in the user interface. The Package Manager window displays this name in the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html).   
  
For example, `"name": "Tools"`.  
**url** | String | The URL to the npm-compatible registry server.   
  
For example, `"url": "https://mycompany.example.com/tools-registry"`  
  
**Note** : Not all registry providers are compatible with Unity’s Package Manager. Make sure the package registry server you’re trying to add implements the `/-/v1/search` or `/-/all` endpoints.  
**overrideBuiltIns** | Boolean | A `true` or `false` value that determines which version of a built-in package to use, if the package exists in a scoped registry.   
  
If set to `false`, the Package Manager uses the built-in version included with the Unity Editor. This is the default value.  
  
If set to `true`, and the built-in package also exists in a scoped registry, the Package Manager downloads the version in the scoped registry.  
  
The scope of this property applies to all packages identified in the **url** property.  
**scopes** | Array of strings | Array of scopes that you can map to a package name, either as an exact match on the package name, or as a namespace. Wildcards and other glob patterns aren’t supported.  
  
For example, `"scopes": [ "com.example", "com.example.tools.physics" ]`   
  
**Note** : This configuration type assumes that packages follow the [Reverse domain name notation](https://en.wikipedia.org/wiki/Reverse_domain_name_notation). This ensures that `com.unity` is equivalent to any package name that matches the `com.unity` namespace, such as `com.unity.timeline` or `com.unity.2d.animation`.  
  
**Warning:** Unity doesn’t support npm’s `@scope` notation.  
#### Project manifest example
In the following project manifest, there are two scoped registries, `General` and `Tools`:
```
{
    "scopedRegistries": [
        {
            "name": "General",
            "url": "https://example.com/registry",
            "overrideBuiltIns": false,
            "scopes": [
                "com.example", "com.example.tools.physics"
            ]
        },
        {
            "name": "Tools",
            "url": "https://mycompany.example.com/tools-registry",
            "overrideBuiltIns": true,
            "scopes": [
                "com.example.mycompany.tools"
            ]
        }
    ],
    "dependencies": {
        "com.unity.animation": "1.0.0",
        "com.example.mycompany.tools.animation": "1.0.0",
        "com.example.tools.physics": "1.0.0",
        "com.example.animation": "1.0.0"
    }
}


```

When the Package Manager decides which registry to fetch a package from, it compares the package `name` to the `scopes` values and finds the registry whose `scopes` value is the closest match. The following scenarios show the logic that the Package Manager uses when assessing the `General` and `Tools` registries from the previous JSON file:
  * When the Package Manager looks up the `com.example.animation` package, it finds that the `com.example` namespace is the closest match to its name, and fetches that package from the `General` registry.
  * When the Package Manager looks up the `com.example.tools.physics` package, the `General` registry has a scope that exactly matches the package name.
  * When the Package Manager looks up the `com.example.mycompany.tools.animation` package, the Package Manager finds that the `com.example.mycompany.tools` namespace is the closest match to its name and fetches that package from the `Tools` registry. Although it also matches the `General` scope, the `com.example` namespace isn’t as close a match.
  * When the Package Manager looks up the `com.unity.animation` package, the Package Manager doesn’t find a match in any of the scoped registries. In this case, it fetches the package from the default registry.


If the `General` and `Tools` registries have **built-in packages** _Built-in_ packages allow users to toggle Unity features on or off through the Package Manager. Enabling or disabling a package reduces the run-time build size. For example, most projects don’t use the legacy Particle System. By removing the abstracted package of this feature, the related code and resources are not part of the final built product. Typically, these packages contain only the package manifest and are bundled with Unity (rather than available on the package registry).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Built-inpackage) that also exist in the Unity Editor, the Package Manager resolves them as follows:
  * The Package Manager skips the built-in packages in the `General` scoped registry because the `overrideBuiltIns` value is `false`. Instead, the Package Manager uses the built-in version included with the Unity Editor.
  * The Package Manager uses the built-in packages in the `Tools` scoped registry instead of the Editor because the `overrideBuiltIns` value is `true`.


## Import scoped registries
If you work in a shared project, and another user adds a scoped registry to the project, Unity warns you that another user added a new scoped registry.
![Unity warns you if theres a change to the list of scoped registries for your project](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-PackageManager-scoped.png) Unity warns you if there’s a change to the list of scoped registries for your project
When you select **Close** , the Package Manager [project settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html) window appears so you can [manage scoped registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#manage-window) for your project.
If you select **Read more** , Unity opens [Scoped registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html) in your default web browser.
**Tip:** To access the Package Manager project settings window at any time, use the main menu in Unity (**Edit > Project Settings**, then the **Package Manager** category). You can also select **Advanced Project Settings** from the [advanced settings](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html#Advanced) menu in the Package Manager window.
## Authenticate with a scoped registry
If you want to access a scoped registry that requires authentication, you must configure your Package Manager user configuration file with npm authentication. For more information, refer to [Scoped registry authentication](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-scoped.html).
## Additional resources
  * [Scoped registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-start.html)
Get started with scoped registries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-scoped.html)
Scoped registry authentication
