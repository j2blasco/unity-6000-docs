* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [WebAssembly 2023](https://docs.unity3d.com/6000.0/Documentation/Manual/webassembly-2023.html)
  * Optimize your Web build with WebAssembly 2023


[](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-prereq.html)
Prerequisites for WebAssembly 2023
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-enable.html)
Enable WebAssembly 2023
# Optimize your Web build with WebAssembly 2023
The WebAssembly 2023 target contains features that can improve code performance, reduce generated code size, and reduce download times for your Web build on all supported browsers and platforms. 
If you enable the WebAssembly 2023 target, it automatically enables all of the following optimization features: 
**Section** | **Description**  
---|---  
[WebAssembly native exceptions](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html#native-exceptions) | Exception handling with less overhead than JavaScript-based exceptions.  
[Support for WebAssembly Single Instruction Multiple Data (SIMD)](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html#simd) | Improves the performance of applications that perform a lot of mathematical calculations or complex vertex manipulation.  
[Optimized data operations](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html#data-optimization) | Useful for large amounts of data manipulation.  
[Support for BigInt](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html#big-int) | Improves data exchange between WebAssembly and JavaScript code.  
[WebAssembly.Table](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html#wasm-table) | Improves interoperability between WebAssembly and JavaScript.  
[Speed up data type conversions](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-features.html#float-to-int) | Reduces code size and slightly improves performance.  
Your browser needs to support these features for them to work properly. To check supported browsers, refer to [prerequisites for WebAssembly 2023](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-prereq.html).
To learn how to enable WebAssembly 2023, refer to [Enable WebAssembly 2023](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-enable.html). 
## WebAssembly native exceptions
In the original WebAssembly MVP **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset), exception handling relied on JavaScript exception mechanisms. This form of exception handling resulted in relatively high overhead. Since then, WebAssembly has developed its own native exception handling support that reduces the overhead issue. 
If you enable WebAssembly 2023, it automatically enables the WebAssembly native exceptions language feature. These native exceptions can improve runtime performance and reduce `.wasm` code size.
## Support for WebAssembly Single Instruction Multiple Data (SIMD)
The WebAssembly SIMD feature enables Unity to use the SIMD instruction support the browser provides. Internally, the browser targets the SIMD instruction sets in x86 intel and ARM architectures. So, this feature works on both desktop and mobile browsers that are supported. For a list of supported browsers, refer to [Prerequisites for WebAssembly 2023](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-prereq.html).
WebAssembly SIMD support includes automatic vectorization support. If you have scalar arithmetic calculations in short loops in your code, auto-vectorization automatically converts it to WebAssembly SIMD data parallel form. In this form, code can perform faster because many calculations are processed simultaneously. 
The WebAssembly SIMD feature can make a significant difference if you have operations that perform heavy matrix mathematics, such as character **skinning** The process of binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed with an external tool, such as Blender or Autodesk Maya. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skinning) or animation **keyframe** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) and transform calculations. 
If your application performs a lot of mathematical calculations or complex vector manipulation, this feature could significantly improve runtime performance. 
## Optimized data operations
WebAssembly 2023 enables better code generation of `memcpy` and `memset` functions. This improved code generation results in better performance when your code copies or sets large amounts of data. 
## Support for BigInt
WebAssembly 2023 enables the `WebAssembly.BigInt` language feature. You can use `WebAssembly.BigInt` to access the JavaScript BigInt data type when you exchange data between JavaScript and WebAssembly code. You can then use the BigInt data type to send and receive 64-bit integers natively between JavaScript and WebAssembly code without the need to split 64-bit integers into high order and low order (HI/LO) pairs of 32-bit numbers.
This improved communication results in a better marshaling boundary between the two interfaces, which improves marshaling performance and also generates smaller code.
You can also enable `WebAssembly.BigInt` support without the other WebAssembly 2023 features. For more information about the feature and how to enable it separately, refer to [WebAssembly language features](https://docs.unity3d.com/Manual/class-PlayerSettingsWebGL#wasm-lang-features). 
**Note** : If you already have marshaling code between the JS and WebAssembly language boundaries that use 64-bit integers, adjust your code to the updated 64-bit marshaling mode that uses the JS BigInt feature. 
For example, if you have an integer like this:
```
const number = 12345678901234567;

```

Convert it to BigInt like this: 
```
const bigInt = BigInt(number);

```

For more information, refer to [Emscripten documentation](https://emscripten.org/docs/api_reference/index.html).
## The WebAssembly.Table language feature
The Unity WebAssembly 2023 feature set enables the Unity Emscripten toolchain to target the `WebAssembly.Table` language feature. This feature simplifies code generation whenever you invoke functions via pointers. Also, because the Emscripten compiler requires fewer passes during compilation, compilation times are faster. 
To invoke functions via pointers, use the `{{{ makeDynCall }}}` macro. 
For more information about the JavaScript object, refer to the Mozilla documentation on [WebAssembly.Table](https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/Table). 
You can also enable `WebAssembly.Table` support without the other WebAssembly 2023 features in **Player** settings. For more information about the feature and how to enable it separately, refer to [WebAssembly language features](https://docs.unity3d.com/Manual/class-PlayerSettingsWebGL#wasm-lang-features).
**Note** : The Emscripten functions `dynCall_*()` and `Module.dynCall()` are deprecated. If your JavaScript plugin code uses these functions, use the Emscripten `{{{ makeDynCall() }}}` macro instead. 
## Speed up data type conversions in your code
If you enable WebAssembly 2023, Unity implements the following conversions with a shorter low-level instruction sequence:
  * float to int
  * double to int


These conversions reduce code size and slightly improve runtime performance.
## Additional resources
  * [WebAssembly 2023](https://docs.unity3d.com/6000.0/Documentation/Manual/webassembly-2023.html)
  * [Prerequisites for WebAssembly](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-prereq.html)
  * [Enable WebAssembly 2023](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-enable.html)
  * [WebAssembly language features](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html#wasm-language-features)
  * [Web Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-prereq.html)
Prerequisites for WebAssembly 2023
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-enable.html)
Enable WebAssembly 2023
