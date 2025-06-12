* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/dependencies-lp.html)
  * Package version conflict and resolution


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html)
Package dependency and resolution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html)
Embedded dependencies
# Package version conflict and resolution
When you add a package to a **project manifest** Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectmanifest), Unity considers that package a [dependency](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html) of the project (a direct dependency). However, a package can also have dependencies on other packages, which create **indirect dependencies** An **indirect** , or transitive dependency occurs when your project requests a package which itself “depends on” another package. For example, if your project depends on the `alembic@1.0.7` package which in turn depends on the `timeline@1.0.0` package, then your project has an direct dependency on Alembic and an indirect dependency on Timeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Indirectdependency) in any projects that require that package. 
Since most projects require more than one package in order to develop games and apps, the Package Manager has to evaluate all the requested package versions to retrieve from the registry (whether direct or indirect), and decide which among those package versions to install. To do this, it computes the set of packages that satisfies all [direct and indirect dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html) in the project, starting with the project dependencies and recursively exploring each indirect dependency, collecting all the dependency information, then picking a set of packages that satisfies the dependency requirements without any conflict. For example, this dependency graph represents a project with four **direct dependencies** A **direct** dependency occurs when your project “requests” a specific package version. To create a direct dependency, you add that package and version to the **dependencies** property in your project manifest (expressed in the form `package_name@package_version`). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Directdependency) and all of their indirect dependencies:
![A graph of direct and indirect package dependencies for a project](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-conflicts.svg) A graph of direct and indirect package dependencies for a project
In this example:
  * The light blue nodes represent the project’s direct dependencies.
  * The dark blue nodes show the same package and version as indirect dependencies in this project.
  * The red nodes show two different versions of the same package, which is a conflict.


**Note** : Only package dependencies declared with versions need to be resolved. The Package Manager selects packages installed from other [sources](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Sources), such as [embedded packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html)An _embedded_ package is a mutable package that you store under the `Packages` directory at the root of a Unity project. This differs from most packages which you download from a package server and are immutable. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Embeddedpackage), and dependencies declared with [local paths](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-localpath.html), [Git URLs](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html), and [built-in](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-build.html) packages over version-based dependencies.
## Choosing the best solution
Depending on the set of packages defined in the project manifest, it could take a long time to evaluate all possible package combinations: a project could potentially depend on hundreds of packages, each of which depend on hundreds of other packages, most requiring different versions. 
### Lock files and resolutionStrategy
To provide the most efficient solution, the Package Manager prioritizes package versions that it previously used by tracking them in a [lock file](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts-auto.html). This guarantees that subsequent dependency resolution using the same inputs results in the same outputs. It also minimizes time-consuming operations such as downloading, extracting, or copying packages.
Sometimes, the Package Manager cannot find a solution that only includes locked packages. In this case, the Package Manager uses the solution with the least risky upgrades, preferring patch upgrades over minor or major upgrades, and minor upgrades over major upgrades by default. However, you can customize how aggressive you want the Package Manager to be when considering a higher version with the [resolutionStrategy](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html#resolutionStrategy) property.
## Example
In this example, there are multiple versions of the following packages requested:
  * `burst@1.2.2` (twice) and `burst@1.3.0-preview.3`
  * `collections@0.5.1-preview.11` and `collections@0.5.2-preview.8`
  * `jobs@0.2.4-preview.11` (twice) and `jobs@0.2.5-preview.20`


Using the set of [direct and indirect dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html), the Package Manager selects the highest version of the burst package (`burst@1.3.0-preview.3`), which satisfies the `collections@0.5.2-preview.8` package’s dependency:
![In the dependency graph, the blue nodes indicate which versions the Package Manager selected](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-resolution.svg) In the dependency graph, the blue nodes indicate which versions the Package Manager selected
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html)
Package dependency and resolution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html)
Embedded dependencies
