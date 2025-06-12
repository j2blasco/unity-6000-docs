* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * Deploy a Web application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-build-configuration.html)
Web template build configuration and interaction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-server-configuration-code-samples.html)
Server configuration code samples
# Deploy a Web application
To deploy a Web build, you must configure your server and make sure you’re using the correct response headers, so that the browser receives a proper response and processes it correctly.
There are two main settings in Unity that affect how you set up the server:
  * ****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) Format**: Determines how Unity compresses files during the build step.
  * **Decompression Fallback** : Determines how Unity processes downloaded files when the build runs in the browser.


## Compression Format
Choose the compression type from the Web Player Settings window (menu: **Edit** > **Project Settings** > **Player** , then select **Web** and expand the **Publishing Settings** section):
![Image of Web Publishing window ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WebGLPublishingWindow.png) Image of Web Publishing window  Compression method | Description  
---|---  
gzip | This is the default option. Gzip files are bigger than Brotli files, but faster to build, and natively supported by all browsers over both HTTP and HTTPS.  
Brotli | Brotli compression offers the best compression ratios. Brotli compressed files are smaller than gzip, but take a longer time to compress, which increases your iteration times on release builds. Chrome and Firefox only natively support Brotli compression over HTTPS.  
Disabled | Disables compression. Use this option if you want to implement your own compression in **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). You should also use it if you plan to use static compression on the hosting server.  
For more information on browser support for selected compression methods, refer to the documentation on [Web browser compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browsercompatibility.html).
**Note** : The **Compression Format** setting applies only to release builds. **Development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild) aren’t compressed.
## Web server configuration
You might need to adjust your server configuration to match your specific build setup. In particular, there might be issues if you already have another server-side configuration to compress hosted files, which could interfere with this setup. To make the browser perform decompression natively while it downloads your application, append a [Content-Encoding header](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html#content_encoding_header) to the server response. This header must correspond to the type of compression Unity uses at build time. For code samples, refer to [Server Configuration Code Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-server-configuration-code-samples.html).
## Decompression fallback
The decompression fallback option enables Unity to automatically embed a JavaScript decompressor into your build. This decompressor corresponds to your selected compression method, and decompresses your content if the browser fails to do so.
### Enable decompression fallback
Enable decompression fallback from the **Player Settings** window (menu: **Edit** > **Project Settings** > **Player** , then select **Web** and expand the **Publishing Settings** section).
When you enable decompression fallback, Unity adds a `.unityweb` extension to the build files. You should consider using **Decompression Fallback** if you have less experience with server configuration, or if server configuration is unavailable to you.
**Note** : Enabling decompression fallback results in a large loader size and a less efficient loading scheme for the build files.
### Disable decompression fallback
The **Decompression Fallback** option is disabled by default. Therefore, by default, build files include an extension that corresponds to the compression method you select.
There are two compression methods to choose from: gzip or Brotli. For further information refer to the [compression format](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html#compression_format) section.
To enable browsers to natively decompress Unity build files while they’re downloading, you need to configure your web server to serve the compressed files with the appropriate HTTP headers. This is called native browser decompression. It’s faster than the JavaScript decompression fallback, which can reduce your application’s startup time.
The setup process for native browser decompression depends on your web server. For code samples, see [Server Configuration Code Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-server-configuration-code-samples.html).
## Content-Encoding headers
A Content-Encoding header tells the browser which type of compression Unity has used for the compressed files. This allows the browser to decompress the files natively.
Set the Content-Encoding response header to the compression method selected in the **Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings).
Compression method | File extension | Response header  
---|---|---  
gzip | .gz | `Content-Encoding: gzip`  
Brotli | .br | `Content-Encoding: br`  
## WebAssembly streaming (higher level header)
WebAssembly streaming allows the browser to compile the WebAssembly code while it’s still downloading the code. This significantly improves loading times.
For WebAssembly streaming compilation to work, the server needs to return WebAssembly files with an `application/wasm` MIME type. To use WebAssembly streaming, you need to serve WebAssembly files with the `Content-Type: application/wasm` response header. A Content-Type header tells the server which media type the content is. This value should be set to `application/wasm` for WebAssembly files.
File extension | Response header  
---|---  
.wasm, .wasm.gz, .wasm.br | `Content-Type: application/wasm`  
**Note** : WebAssembly streaming doesn’t work together with JavaScript decompression when the Decompression Fallback option is enabled. The downloaded WebAssembly file must first go through the JavaScript decompressor because the browser can’t stream it during download.
## Additional headers
If your file contains JavaScript, you should add the `application/javascript` Content-Type header. Some servers might include this automatically, while others don’t.
File extension | Response header  
---|---  
.js, .js.gz, js.br | `Content-Type: application/javascript`  
* * *
  * Updated page to account for server configuration in 2020.1
  * 2019–09–04  WebAssembly streaming added in 2019.2 


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-build-configuration.html)
Web template build configuration and interaction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-server-configuration-code-samples.html)
Server configuration code samples
