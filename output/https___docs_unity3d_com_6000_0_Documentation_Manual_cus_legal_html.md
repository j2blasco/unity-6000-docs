* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/cus-legal.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Create custom packages](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
  * Custom package legal requirements


[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-asmdef.html)
Assembly definition and packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-document.html)
Document your package
# Custom package legal requirements
You can use the `Third Party Notices.md` and `LICENSE.md` files to make sure your package meets any legal requirements. For example, here’s a sample license file from the Unity Timeline package:
```
Unity Timeline copyright © 2017-2019 Unity Technologies ApS

Licensed under the Unity Companion License for Unity-dependent projects--see [Unity Companion License](http://www.unity3d.com/legal/licenses/Unity_Companion_License).

Unless expressly provided otherwise, the Software under this license is made available strictly on an “AS IS” BASIS WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. Please review the license for details on these and other terms and conditions.


```

## Third Party Notices
If your package has third-party elements, you can include the licenses in a `Third Party Notices.md` file. You can include a **Component Name** , **License Type** , **Version Number** , and **Provide License Details** section for each license you want to include. For example:
```
This package contains third-party software components governed by the license(s) indicated below:

Component Name: Semver

License Type: "MIT"

[SemVer License](https://github.com/myusername/semver/blob/master/License.txt)

Component Name: MyComponent

License Type: "MyLicense"

[MyComponent License](https://www.mycompany.com/licenses/License.txt)


```

**Note** : Point the **Provide License Details** section’s URL to a location that contains the reproduced license and the copyright information (if applicable). If the license governs a specific version of the component, give the URL of that version, if possible.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-asmdef.html)
Assembly definition and packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-document.html)
Document your package
