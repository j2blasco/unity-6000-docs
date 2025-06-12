* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-unity-version.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Branch in a shader via built-in macros](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html)
  * Branch based on Unity version


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-platform.html)
Branch based on platform features
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-pass.html)
Branch based on shader pass or shader stage
# Branch based on Unity version
`UNITY_VERSION` contains the numeric value of the Unity version.
This can be used for version comparisons if you need to write shaders that use different built-in shader functionality. For example, use `#if UNITY_VERSION >= 202200` if you want the preprocessor check to pass only on Unity versions 2022 or later.
## Unity 2023 or earlier
Use the format `YYYYMP`, where:
  * `YYYY` is the major version.
  * `M` is the minor version.
  * `P` is the patch version.


For example, for Unity 2022.3.0, use `202230`.
You can use only values up to 9 for the minor and patch versions. This means you can’t check for a Unity version with a minor version larger than 9 or a patch version larger than 9.
## Unity 6.0 Preview
Use the format `6000PPPP`, where:
  * `6000` is Unity 6.
  * `PPPP` is the patch version with leading zeroes, for example `1234` for Unity 6000.0.1234.


For example, for Unity 6000.0.2, use `60000002`.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-platform.html)
Branch based on platform features
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-pass.html)
Branch based on shader pass or shader stage
