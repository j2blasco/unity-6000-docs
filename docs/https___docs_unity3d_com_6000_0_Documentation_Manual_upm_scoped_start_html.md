* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-start.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Scoped registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html)
  * Get started with scoped registries


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html)
Scoped registries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html)
Use a scoped registry in your project
# Get started with scoped registries
As a package provider, you can host a scoped registry as a way to distribute custom packages to users. As a package consumer, you can access the packages in a scoped registry without leaving the Package Manager window. 
Here are some important concepts to help you understand scoped registries:
**Concept** | **Description**  
---|---  
**package registry server** | An application that keeps track of packages and provides a place to store them. In Unity’s Package Manager window, all packages registered on Unity’s registry appear in the [list panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html) when you select the [Unity Registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html#contexts) context.  
**package manager** | An application that tells the user what packages are available, and downloads and installs whatever package the user requests for their project. Unity has implemented its own version of a package manager, but there are several similar applications in other organizations.  
**scope** | Defines a package name or namespace (in reverse domain format), such as `com.example.mycompany.animation` or `com.example`. When a user requests a package, the Package Manager fetches the package from the registry that best matches the scope. For more information about scope, refer to [Manage scoped registries with the project manifest file](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html#manage-manifest).  
The way you interact with scoped registries depends on your role:
  * Package providers set up custom registry servers to host and distribute custom packages to a registry other than the [Unity registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Registry). For information about how to provide packages in a scoped registry, refer to [Host a scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-host.html).
  * Package consumers set up scoped registries in their project to access a custom package provider’s registry server. For information about consuming packages in a scoped registry, refer to [Use a scoped registry in your project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html).


## Benefits of scoped registries
Scoped registries can help to:
  * **Provide new functionality by distributing tools, libraries, and other assets**.
As a provider, you can create your own registry to distribute tools and **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) (or other types of assets) with version numbers that indicate how mature the package is. Version numbers also indicate whether updates introduce breaking API changes or minor fixes, based on [Semantic Versioning](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html). Your code can depend on code in other packages, because the Package Manager supports [package dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html).
As a consumer, you browse and install custom packages in the Package Manager the same way you browse Unity’s packages.
  * **Extend Unity’s existing package features**.
As a consumer, you can have a seamless experience where the custom package overrides the Unity package without having to manually change registries or explicitly install a different package version. This is because you can map packages to a specific registry so that Package Manager fetches from either the Unity registry or a custom package registry server.
  * **Access packages in a closed network environment**.
Some organizations work inside a closed network, which makes it difficult to access Unity’s package registry. In these cases, the organization can set up their own package registry on a server inside their closed network. The network administrators can then periodically synchronize with Unity’s package registry to make sure the scoped registry has the latest set of packages available.


## Additional resources
  * [Use a scoped registry in your project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html)
  * [Host a scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-host.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html)
Scoped registries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-use.html)
Use a scoped registry in your project
