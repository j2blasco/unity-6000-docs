* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-overview.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Get started with packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
  * How Unity works with packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html)
Introduction to packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
Package types
# How Unity works with packages
When Unity opens a Project, the Unity Package Manager reads the [Project manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectmanifest) (**1**) to figure out what packages to load in the Project. Then it sends a request (**2**) to the [package registry server](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Registry) (**3**) for each package that appears as a dependency in the manifest. The package registry then sends the requested information and data back to the Package Manager (**4**), which then installs those packages (**5**) in the Project. Each Project has its own manifest which lists the packages to load as “dependencies” of the Project.
![How the Unity Package Manager installs packages](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-overview.png) How the Unity Package Manager installs packages
Adding a package to a project requires an update to the project manifest, to ensure the Package Manager includes the package in the list of dependencies. Although you can modify the project manifest directly, it’s safer and easier to work with the [Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html), which manages the project manifest modifications for you.
## Additional resources
  * [Get started with packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
  * [Introduction to packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html)
Introduction to packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
Package types
