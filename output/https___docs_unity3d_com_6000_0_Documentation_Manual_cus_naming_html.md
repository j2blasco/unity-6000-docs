* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/cus-naming.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Create custom packages](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
  * Name your package


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
Create custom packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-layout.html)
Package layout
# Name your package
There are two names for a package. The first name is the [official name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html#name), which is an identifier that you register the package with. The second name is the user-facing [display name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html#displayName) that appears in the Unity Editor.
Keep the display name brief, yet informative enough so that users can tell what it contains. The Unity Package Manager doesn’t impose any restrictions on the display name.
## Guidelines and restrictions for the official name
The official name must conform to the following guidelines and restrictions:
  * The name must use reverse domain name notation, which means it must start with **< domain-name-extension>.<company-name>**, such as `com.example` or `net.example`. This restriction applies even if your company or website name begins with a digit. Following this naming convention prevents name collisions between packages from separate companies.
  * Don’t use `com.unity` at the beginning of your own package names.
  * Don’t use `unity` anywhere in your package name.
  * The name can contain only lowercase letters, digits, hyphens(-), underscores (_), and periods (.)
  * The recommended name length is 50 or fewer characters. The Unity Package Manager imposes a strict limit of 214 characters.
  * To indicate nested namespaces, suffix the namespace with an additional period followed by an identifier.


**Note** : These naming restrictions apply only to the package names themselves and don’t need to match the namespace in your code. For example, you can use `Project3dBase` as a namespace in a package called `net.example.3d.base`.
## Examples
  * com.company.input
  * com.company.2d.physics
  * com.company.2d.tools


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
Create custom packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-layout.html)
Package layout
