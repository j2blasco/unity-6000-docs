* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL.html

# WebGL
class in UnityEditor
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
### Description
WebGL specific player settings.
### Static Properties
Property | Description  
---|---  
[closeOnQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-closeOnQuit.html) | If enabled, the Unity Player will close the browser running it when the application quits.  
[compressionFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-compressionFormat.html) | CompressionFormat defines the compression type that the WebGL resources are encoded to.  
[dataCaching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-dataCaching.html) | Enables automatic caching of unityweb files.  
[debugSymbolMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-debugSymbolMode.html) | Enables generation of debug symbols file in the build output directory. Supported options: embedded debug symbols and debug symbols in external file.  
[decompressionFallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-decompressionFallback.html) | Include decompression fallback code for build files in the loader.  
[exceptionSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-exceptionSupport.html) | Exception support for WebGL builds.  
[geometricMemoryGrowthStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-geometricMemoryGrowthStep.html) | Heap memory growth factor.  
[initialMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-initialMemorySize.html) | Initial size of the WASM heap memory in MB.  
[linearMemoryGrowthStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-linearMemoryGrowthStep.html) | Heap memory growth step in MB.  
[linkerTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-linkerTarget.html) | Allows you to specify the web build format that is used when you build your project.  
[maximumMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-maximumMemorySize.html) | Maximum size of the WASM heap memory in MB.  
[memoryGeometricGrowthCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-memoryGeometricGrowthCap.html) | Upper limit for heap growth step in MB.  
[memoryGrowthMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-memoryGrowthMode.html) | The growth mode for WASM heap memory.  
[memorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-memorySize.html) | Memory size for WebGL builds in Megabyte.  
[nameFilesAsHashes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-nameFilesAsHashes.html) | Enables using MD5 hash of the uncompressed file contents as a filename for each file in the build.  
[powerPreference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-powerPreference.html) | The power preference hint to provide to the WebGL context to help decide which GPU to use in multi-gpu systems. Note that this is just a hint, and some WebGL implementations may choose to ignore it.  
[showDiagnostics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-showDiagnostics.html) | Displays a diagnostics overlay on the Unity application page.  
[template](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-template.html) | Path to the WebGL template asset.  
[threadsSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-threadsSupport.html) | Multithreading support in WebGL.  
[wasm2023](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-wasm2023.html) | If enabled, generated WebAssembly code will target "WebAssembly 2023", a Unity-coined name for a selection of newer WebAssembly language features. These features include: sign-extension opcodes, non-trapping fp-to-int instructions, bulk memory, JS BigInt integration, WebAssembly.Table, native WebAssembly exceptions and SIMD. Requires Chrome ≥ 91 (May 2021), Firefox ≥ 89 (June 2021) or Safari ≥ 16.4 (March 2023). If disabled, targets the original WebAssembly "MVP" feature set.   
[wasmArithmeticExceptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-wasmArithmeticExceptions.html) | The trapping mode for WebAssembly code.  
[webAssemblyBigInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-webAssemblyBigInt.html) | If enabled, generated WebAssembly code will rely on the BigInt ABI for function signatures containing 64-bit variables. Enable this to achieve faster build times and slightly smaller code size. The Wasm BigInt feature requires at least Chrome 85 (Aug 25, 2020), Firefox 78 (Jun 30, 2020), Safari 14.5 (Apr 26, 2021), or newer. Disable this option to target older browsers that do not support the Wasm BigInt feature. It is recommended to enable this option for new projects and if you prefer fast build iteration times, and to disable it if targeting backward compatibility with older browsers is important.  
[webAssemblyTable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-webAssemblyTable.html) | If enabled, targets the WebAssembly.Table language feature, which results in faster JS-Wasm interop and faster build times. WebAssembly.Table is not backwards compatible with the older dynCalls interop model. If disabled, Unity targets the old deprecated Emscripten -sDYNCALLS flag for backwards compatibility with older Unity Web platform JS plugin code. It is recommended to enable this option for new projects that do not utilize any older incompatible JavaScript plugins, and when you prefer fast build iteration times, and to disable it if utilizing .jslib files that rely on the older dynCall() mechanism.  
* * *
