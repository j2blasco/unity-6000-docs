* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-deprecated.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * Replace deprecated browser interaction code


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-js-interface.html)
JavaScript interface in Unity Web builds
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-native-plugins-with-emscripten.html)
Web native plug-ins for Emscripten
# Replace deprecated browser interaction code
Some code involved with web browser script interactions is deprecated and has been replaced with alternative code.
If your code contains any of the deprecated code, you need to update the code with the replacement code to prevent unexpected behavior or broken code.
## Deprecated code quick reference
The following code is deprecated and you need to replace it with the replacement code. 
Deprecated code | Replacement code  
---|---  
[dynCall()](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-deprecated.html#dyncall) | `makeDynCall()`  
[Pointer_stringify()](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-deprecated.html#pointer_stringify) | `UTF8ToString()`  
[unity.Instance()](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-deprecated.html#unity-instance) | `CreateUnityInstance()`  
[gameInstance](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-deprecated.html#gameinstance) | `unityInstance`  
## Change dynCall to makeDynCall
The `dynCall` function is deprecated. If you have any code that uses `dynCall`, replace it with `makeDynCall`. Make this change whether you have `WebAssembly.Table` enabled or not. 
For example, change:
```
dynCall('vii', callback, [1, 2])

```

to:
```
{{{ makeDynCall('vii', 'callback') }}}(1, 2)

```

## Change Pointer_stringify() to UTF8ToString
The `Pointer_stringify()` function is deprecated. If your code contains calls to `Pointer_stringify()`, replace the calls with `UTF8ToString()`. 
For example, change:
```
var stringMessage = Pointer_stringify(message);

```

to:
```
var stringMessage = UTF8ToString(message);

```

## Change unity.Instance to CreateUnityInstance
`unity.Instance` is deprecated. If your code uses `unity.Instance`, use `CreateUnityInstance` instead. 
For example, change: 
```
var MyGameInstance = null;
  script.onload = () => {
    unity.Instance(canvas, config, (progress) => { /*...*/ }).then((unityInstance) => {

```

to:
```
var MyGameInstance = null;
  script.onload = () => {
    createUnityInstance(canvas, config, (progress) => { /*...*/ }).then((unityInstance) => {

```

## Change gameInstance to unityInstance
The `gameInstance` property is deprecated. If your code uses `gameInstance`, use `unityInstance` instead. 
For example, change: 
```
MyGameInstance = gameInstance;

```

to: 
```
MyGameInstance = unityInstance;

```

## Additional resources
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * [Set up your JavaScript plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js.html)
  * [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
  * [Call Unity C# script functions from JavaScript](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html)
  * [Call C/C++/C# functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-js-interface.html)
JavaScript interface in Unity Web builds
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-native-plugins-with-emscripten.html)
Web native plug-ins for Emscripten
