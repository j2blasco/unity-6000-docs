* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * Modify URP source code


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html)
Injection points reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)
Compatibility Mode in URP
# Modify URP source code
For advanced customizations, it might not be enough to extend or override APIs defined in URP. You might need to modify URP source code to change certain methods.
To prepare URP source code for modifications:
  1. In the root folder of your project, go to `Library/PackageCache`.
  2. Copy the following folders into the `Packages` folder at the root of your project:
```
com.unity.render-pipelines.universal
com.unity.render-pipelines.universal-config

```



Now Unity uses the URP source code from the `Packages` folder of your project, and you can make changes to that code.
## Plan the upgrade process
After you copy the URP source code into the `Packages` folder, this code becomes part of your project and is no longer part of a Unity install. If you upgrade the Unity version later, Unity doesn’t update the URP source automatically. You need to apply the changes to source code manually.
To make this process easier, document all the changes you make to the URP source code in your project.
## Additional resources
  * [Custom lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/custom-lighting-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html)
Injection points reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)
Compatibility Mode in URP
